GPU Porting
********************************************************************************

High performance software with FLOP heavy but parallelization workloads can benefit from using GPU hardware.
It is easier to develop a project with GPU support from the beginning; however it can be impractical to restart an existing project from scratch, especially a large project with hundreds of thousands or millions of lines of code representing years or decades of development effort.

In this post, we explore different approaches to extending existing software to run on GPU hardware.
There are two general families of approaches under consideration here - native support via the hardware specific language, such as `CUDA <https://developer.nvidia.com/cuda>`_, `ROCm <https://www.amd.com/en/products/software/rocm>`_, or `SYCL <https://www.khronos.org/sycl>`_, and performance portability libraries, such as `Kokkos <https://kokkos.org>`_ or `Raja <https://raja.readthedocs.io>`_.

Note: ROCm and SYCL have the ability to target different hardware rather than just `AMD devices (ROCm) <https://rocm.docs.amd.com/projects/HIP>`_ or `Intel devices (SYCL) <https://github.com/AdaptiveCpp/AdaptiveCpp>`_ so in some sense they can be thought of having some capabilities in common with a performance portability library.
However, that capability will not be the full focus of our discussion here, as the ability to target different hardware is not the only distinction under consideration.

We will outline some pros and cons to consider when deciding what approach to take when extending existing software to run on GPU hardware.


Native GPU Support
================================================================================

Hardware specific languages include `CUDA <https://developer.nvidia.com/cuda>`_, `ROCm <https://www.amd.com/en/products/software/rocm>`_, or `SYCL <https://www.khronos.org/sycl>`, or `SYCL <https://www.khronos.org/sycl>`_.
These packages allow more direct control over usage of the device and how  the kernels are launched.
As a drawback however, these languages are more intrusive to integrate into your code.
Additionally, these languages are often paired with specific hardware, though this requirement is sometimes relaxed.


Performance Portability Libraries
================================================================================

Performance portability libraries include `Kokkos <https://kokkos.org>`_ and `Raja <https://raja.readthedocs.io>`_.
With these libraries, incorporating GPU capabilities is less obtrusive, and these libraries typically  support a wider variety of hardware instead of only hardware from a particular manufacturer.
Also, the specifics of some of the common details, such of memory management and synchronization, are handled for the users.
However, these libraries typically do not offer as direct of control over the configuration of the device kernels, as a natural byproduct of their generality and flexibility.

Additionally, using one of these performance portability libraries requires both the appropriate dependency for the hardware (CUDA, ROCm, SYCL, etc) and the performance portability library.
This means that the dependency stack is deeper, which adds more to configure and manage, especially for legacy software projects which may already have a heavy dependency stack.


Metadata
================================================================================

Started: 11 Mar 2026

Last edited: 16 Jul 2026
