CUDA SM Versions
********************************************************************************

When compiling CUDA code, you can target specific hardware by specifying the 'compute capability' of the NVIDIA hardware you are working with.
This is known as the SM or Streaming Multiprocessor version.
CUDA publishes a `list of compute capability for common NVIDIA hardware <https://developer.nvidia.com/cuda/gpus>`_.

When compiling and testing the 4C library, I received the following error message for a GPU enabled test:

.. code-block:: console

   C++ exception with description "(cuda_instance->cuda_func_get_attributes_wrapper(&attr, func)) error( cudaErrorNoKernelImageForDevice): no kernel image is available for execution on the device /home/thompson/Dev/4C-dependencies/tk_cuda/include/kokkos/Cuda/Kokkos_Cuda_KernelLaunch.hpp:141" thrown in the test fixture's constructor.


Issue
================================================================================

The effort to trace the exact problem is complicated by the fact that I am building 4C, which relies upon Trilinos with Kokkos where the CUDA backend is enabled, and this version of Kokkos is being used in Mirco to compile the offending kernel.
Somewhere along the line the correct SM appears to be not set.


Diagnosis
================================================================================

This followed issues getting the CUDA toolkit set up on this machine, so I first investigated if CUDA and the NVIDIA drivers were correctly configured.
The commands `nvidia-smi` and `nvcc --version` verify that CUDA and the NVIDIA drivers are correctly configured.

.. code-block:: console

   $ nvidia-smi
   Thu Jul 16 08:58:16 2026       
   +-----------------------------------------------------------------------------------------+
   | NVIDIA-SMI 595.71.05              Driver Version: 595.71.05      CUDA Version: 13.2     |
   +-----------------------------------------+------------------------+----------------------+
   | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
   | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
   |                                         |                        |               MIG M. |
   |=========================================+========================+======================|
   |   0  NVIDIA RTX A1000 6GB Lap...    Off |   00000000:01:00.0 Off |                  N/A |
   | N/A   66C    P0            312W /   35W |      14MiB /   6144MiB |      8%      Default |
   |                                         |                        |                  N/A |
   +-----------------------------------------+------------------------+----------------------+
   
   +-----------------------------------------------------------------------------------------+
   | Processes:                                                                              |
   |  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
   |        ID   ID                                                               Usage      |
   |=========================================================================================|
   |    0   N/A  N/A            3291      G   /usr/lib/xorg/Xorg                        4MiB |
   +-----------------------------------------------------------------------------------------+

.. code-block:: console

   $ nvcc --version
   nvcc: NVIDIA (R) Cuda compiler driver
   Copyright (c) 2005-2026 NVIDIA Corporation
   Built on Tue_Jun_09_02:43:40_PM_PDT_2026
   Cuda compilation tools, release 13.3, V13.3.73
   Build cuda_13.3.r13.3/compiler.38244171_0

CUDA and NVIDIA drivers are correctly installed, which was also verified by running the test suite on a simpler library, so the problem must lie elsewhere.


Root Cause
================================================================================

I was having trouble locating the exact root cause of the issue, and putting the error message into a search engine was not giving helpful results.
I provided the error message as an input to Copilot, and while the result was not terribly useful, the output did include the suggestion to try the `cuobjdump` command.
With this command, I could verify that Kokkos was built to target my SM, `sm_86`, but I could not locate the compiled test case to determine what SM that test case was being compiled to target.

However, I did at this point recall that we were using a compiler wrapper `clangcuda++`, and this wrapper was using `clang++` in place of `nvcc` with some extra logic to inject the correct compiler flags if the file should be compiled to target GPU hardware.
This compiler wrapper relies upon the environment variable `CLANGCUDA_ARCH` being set to the correct SM, and it has a default value of `sm_90` if the environment variable is not set.
Changing this default to `sm_86`, the SM for my hardware, fixed the issue.

This indicated that the environment variable was in fact not correctly set and being passed to the build system.
It turned out there was an issue with my `.bashrc` file.
However, this highlighted a vulnerability with the `clangcuda++` compiler wrapper assuming a SM to target.
Cross compilation (targeting different hardware for runtime than is present on the hardware where the library is built) is desirable, but it can lead to a silent error where the user appears to have a successful build but it is targeting different hardware than they have.


Fix
================================================================================

There are a few possible fixes in this case

1) Warn or error when the user has not set the environment variable `CLANGCUDA_ARCH`

2) Attempt to query the hardware via `nvidia-smi` to determine the supported SM

3) Set a more general default

The first option is the most reliable but does require user interaction.
The second could fail but can fall back to the first option upon failure.
I found a nice `stackoverflow answer <https://stackoverflow.com/a/72854145>`_ that extracts the compute capacity out of the output of `nvidia-smi`.
The third option does not really address the core issue of possibly setting an unsupported default.

The full details of the related work are in this `pull request <https://github.com/4C-multiphysics/4C/pull/2012>`_.


Metadata
================================================================================

Started: 16 Jul 2026

Last edited: 16 Jul 2026
