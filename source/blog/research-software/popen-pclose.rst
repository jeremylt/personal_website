Popen and pclose bufer
********************************************************************************

In C, `popen <https://pubs.opengroup.org/onlinepubs/9799919799/functions/popen.html>`_ and `pclose <https://pubs.opengroup.org/onlinepubs/9799919799/functions/pclose.html>`_ are system functions in the standard C library that allow users to create a pipe and invoke the shell.
We ran into a subtle bug related to correct usage of `popen` and `pclose`.


Issue
================================================================================

libCEED can use either NVRTC or `Clang <https://llvm.org/docs/CompileCudaWithLLVM.html>`_ to do JiT compilation of programmatically generated code to produce specific kernels that match the user parameters in order to offer the best performance.
This feature was specifically designed to support kernel fusion of user code written in Rust with programmatically generated wrapping code written in CUDA.
In order to support this feature, both the Rust and CUDA code is compiled to `LLVM IR <https://en.wikipedia.org/wiki/LLVM#Intermediate_representation>`_ and then combined via link time optimization to produce similar performance to code written in a single generated kernel containing only C/CUDA.

The CUDA backends use `popen` to run commands to determine the LLVM version used in the Rust toolchain for compilation of the user Rust code to LLVM IR so that the same version of `clang++` is invoked while compiling the generated CUDA code to LLVM IR.
This process was not working as intended, resulting in incompatible versions of Rust and `clang++` being used together.


Diagnosis
================================================================================

In order to determine the version of LLVM used in the Rust toolchain, we first read the environment variable `RUST_TOOLCHAIN` (or assume `nightly` if not defined, as we rely upon unstable features for this process) and then use `popen` to execute the command `$(find $(rustup run [RUST_TOOLCHAIN] rustc --print sysroot) -name llvm-link) --version`.
This command produces a large amount of output, which we read from the buffer of the pipe and search for the string `"LLVM version"`, followed by the version number, given as `[major].[minor]`.

Once we have LLVM major version number, we attempt to invoke the associated C++ compiler via `clang++-[major]` with `popen`.
We assume that if we `pclose` with a clean error code, then the invocation was successful and can use `clang++-[major]`, otherwise we default to `clang++`.

When we used `pclose`, we got a non-zero error code and defaulted to `clang++`.
Unfortunately, in our CI environment `clang++` defaulted to `clang++-21` while Rust was using LLVM version 22.
`clang++-21` errored while attempting to compile our generated code while `clang++-22` did not.


Root Cause
================================================================================

We were using the command `clang++-[major] --version 2>&1` to determine if the version of `clang++` specified was valid.
As we did not care about the output of the command, only the exit code, we did not check the contents of the buffer for the pipe.

The documentation for `pclose` states that the termination status of the command language interpreter is returned if successful, otherwise `pclose` returns `-1` on error and sets `errno` to set the error.

This means that return values other than zero can indicate a successful execution.
Specifically, when we were calling `pclose` without reading the contents of the buffer, then a positive number will be returned from `pclose` instead of zero or `-1`.


Fix
================================================================================

We could either read the contents of the buffer or modify our check for a non-zero return value to be a check that the return value is not `-1`.
We opted to read the buffer and check for a non-zero return value.
Then we optionally write the contents out as debugging information if debugging output is enabled for libCEED.

The full details of the fix are in this `pull request <https://github.com/CEED/libCEED/pull/1966>`_.


Metadata
================================================================================

Started: 20 May 2026

Last edited: 20 May 2026
