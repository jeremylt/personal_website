Weak Symbols on MacOS
********************************************************************************

In C libraries, `weak symbols <https://en.wikipedia.org/wiki/Weak_symbol>`_ are a common way to provide default implementations that can be conditionally overridden based upon the files compiled into the library.


Issue
================================================================================

libCEED is based upon the `bridge pattern <https://en.wikipedia.org/wiki/Bridge_pattern>`_ where different hardware (CPU, GPU, etc) is supported with different backend implementations.
When a user attempts to use an implementation but the associated dependency is not available (CUDA, ROCm, SYCL, etc), then the library defaults to a weak symbol with an error message directing the user to consult the installation instructions to build the library with the required dependency.

For libCEED on MacOS using a static build of the library, the build system was `failing to properly link all backends <https://github.com/CEED/libCEED/issues/1694>`_.
Compiled backends were erroneously using the weak symbol instead of the strong symbol for supported 'backends'.


Diagnosis
================================================================================

Debugging was complicated by the fact that I do not have access to a MacOS machine, so my only environment for testing was the project CI.
I had to add MacOS to our `GitHub Action <https://github.com/CEED/libCEED/blob/0031f6c0bccfe00da73710d243af119549bbab9e/.github/workflows/rust-test-with-style.yml#L13>`_ for testing the Rust interface of libCEED to verify the issue and debug.

There is a lot of information out there on using weak symbols for `Mach-O <https://en.wikipedia.org/wiki/Mach-O>`_, but this information is largely available for dynamic libraries.
Nevertheless, I tried the different weak symbol markers and linkers recommended online, the problem persisted.

After frustrating attempts at 'fancy' solutions, I attempted a 'simple' solution.
I removed the weak symbols for backends I knew would always be successfully complied.
This resulted in a successful build, but this was not feasible for actually supporting the conditional compilation and error message outline above.

I created a separate file with the weak symbols only for the backends that are always compiled, and the library still found the correct symbol in this case.
The fix is to create separate files for the weak symbols of the backends based upon each dependency package.
This was difficult to diagnose, as most of the information available online was unrelated to the true root cause.


Root Cause
================================================================================

Once MacOS loads an object file for a static library, all of the object definitions in that file are considered valid symbols, even if they are weak symbols.
For static libraries, if the object file containing the weak symbols is loaded before an object file containing the strong symbols, MacOS will stop searching for additional symbols and use the weak symbol it has loaded.
This issue was not detected earlier because MacOS will search for additional symbols and load the object files containing the strong symbols when using a dynamic library.


Fix
================================================================================

Separate the fallback weak symbols into separate files for each group of backends requiring the same dependency.
Then, when one of the weak symbol files is loaded, it only contains weak symbols that will be used, and none corresponding to backends that were successfully compiled.

The full details of the fix are in this `pull request <https://github.com/CEED/libCEED/pull/1919>`_.


Metadata
================================================================================

Started: 10 Mar 2026

Last edited: 10 Mar 2026
