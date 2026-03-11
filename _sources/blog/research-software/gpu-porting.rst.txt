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

Performance Portability Libraries
================================================================================

Performance portability libraries include `Kokkos <https://kokkos.org>`_ and `Raja <https://raja.readthedocs.io>`_.

Metadata
================================================================================

Started: 11 Mar 2026

Last edited: 11 Mar 2026
