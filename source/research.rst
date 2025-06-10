Research Statement
********************************************************************************

Open Source Scientific Software for Modern HPC Hardware
--------------------------------------------------------------------------------

Highly accurate physics based numerical simulations are important in a wide range of modern science and engineering applications.
These simulations allow us to investigate many different scenarios where it is impractical or unsafe to conduct a large number of physical experiments or act as a prelude to a more limited and focused set of experiments.
However, high fidelity simulations require a large amount of computational power.
If these simulations are being used in uncertainty quantification or optimization workflows, then the amount resources required is amplified.
It is important to innovate algorithmically to best use modern computing resources in support of our research goals.

Many fluid dynamics and solid mechanics applications use finite-element like discretizations of the physically based PDEs in simulations modeling behavior of interest.
High-order matrix-free finite element-like operators on elements with tensor-product bases offer superior performance on modern high performance computing (HPC) hardware when compared to the standard industry approach of assembled sparse matrices, both with respect to the number of floating point operations needed for operator evaluation and the memory transfer needed for a matrix-vector product.
However, matrix-free operators require iterative solvers, such as Krylov subspace methods, and these iterative solvers converge slowly for high-order operators because these operators are increasingly ill-conditioned as polynomial order of the bases increases.
Preconditioning techniques can significantly improve the convergence of these iterative solvers for high-order matrix-free finite element operators.

In my research, I focus on using high-order matrix-free methods with appropriate preconditioners to achieve high performance on modern HPC hardware.
I build core computational infrastructure and preconditioners to support a variety of application areas.
To this end, my research efforts are centered around building open source software packages while enabling and accelerating the research of students and researchers who are using these packages.
This works allows us to complete simulations in hours or days that could take weeks to complete with older approaches.


High-Order Matrix-Free
--------------------------------------------------------------------------------

In order to innovate algorithmically and best use modern HPC resources, we must understand the constraints of the hardware.
Two key performance metrics for HPC hardware are Floating Point Operations per Second (FLOPs) and memory and network bandwidth.
FLOPs is the more widely popularized of these two metrics, but memory and network bandwidth is a common bottleneck in HPC application codes.
As discussed in McCalpin's Supercomputing 2016 invited talk :cite:`mccalpin2016memory`, the maximum FLOP rates for new HPC hardware have improved approximately twice as much as memory and network bandwidth, for both CPUs and GPUs.
The ratio of FLOPs to memory bandwidth required for high-order matrix-free finite element-like operators on elements with tensor-product bases is closer to the capabilities of modern HPC hardware.

The maximum FLOP rate given by the Top 500 :cite:`meuertop500` list is measured by High-Performance Linpack (HPL) :cite:`petitethpl`.
High-Performance Geometric Multigrid (HPGMG) :cite:`adams2014hpgmg` and High-Performance Conjugate Gradient (HPCG) :cite:`dongarra2016high` measure performance with a benchmark problem that is more representative of scientific simulations.
Conventional sparse matrix implementations can struggle to achieve more than 1% of the maximum FLOP rate due to their inefficient usage of the limited memory bandwidth, which highlights the need for matrix-free implementations.

High-order finite elements also offer the high accuracy needed for modern simulations as well as exponential convergence for sufficiently smooth problems.
While the smoothness of the solution for practical problems may prevent exponential convergence, high-order finite elements still offer convergence that is no worse than a comparable low-order mesh with a larger number of elements.
For discussion of the convergence of high-order methods, see :cite:`babuvska1994p,babuska1982rates,guo1986hp`, among others.

Although the benefits of high-order matrix-free implementations on modern HPC hardware are well understood, a significant amount of software development and research can be required for the specific model and preconditioners needed in a simulation.
For example, matrix-free implementations can expose numerical stability issues in alternate formulations of the same underlying physics :cite:`stablenumerics2024` and the preconditioners may require parameter tuning or novel implementations.


Open Source Scientific Software
--------------------------------------------------------------------------------

Transparency and reproducibility are the lifeblood of scientific and software advancement.
I strive to make all of my software open source and freely available while utilizing best practices for modern software development, such as documentation and continuous integration testing.
Closed source or lower quality software inhibits reproducibility and can slow research expanding upon previous work.

Implementations of the high-order matrix-free finite element-like operators can be found in the `libCEED GitHub repository <https://www.github.com/CEED/libCEED>`_, along with fluid dynamics and solid mechanics mini-applications.
libCEED :cite:`libceed, libceed-user-manual` is a low-level library for the efficient high-order discretization methods developed by the ECP co-design Center for Efficient Exascale Discretizations (CEED).
LibCEED has multiple backends that can be selected at runtime, and these backends target CPU architectures :cite:`libxsmm`, NVIDIA GPUs :cite:`CUDAwebsite`, AMD GPUs :cite:`HIPwebsite`, and Intel GPUs.

LibCEED is based around separate hardware specific implementations of the API being selectable at runtime.
As lead maintainer, I provide new features for my research and code review and features to accelerate the work of other researchers. 
The gap between a CPU and GPU implementation can be difficult to bridge for many HPC applications; to this end I developed a libCEED CPU backend implementation that replicates many of the common issues discovered while porting CPU code to GPU implementations, such as memory synchronization and dual memory spaces representing host and device memory, helping contributors and collaborators more quickly identify errors in their codes when moving to GPU implementations.

An excessive number of kernel launches and intermediate data structures can slow GPU performance, so I have refactored and expanded the code generation backends for GPU hardware.
While metaprogramming reduces the runtime of our simulations and allows us to put significantly larger portions of the problem on a single device, writing software that writes source code for JiT is inherently more complex to reason about.
As a result, I focus on code consistency, clarity, and documentation so that it is easier for contributors to add new GPU implementations.

These simulations rely upon the the linear and nonlinear solver and preconditioning infrastructure found in `PETSc <https://www.mcs.anl.gov/petsc/>`_ :cite:`petsc-user-ref`, the Portable, Extensible Toolkit for Scientific Computation.
PETSc is a suite of data structures and routines for the scalable, parallel solution of scientific applications modeled by partial differential equations.
As libCEED's lead developer, I make contributions to PETSc to help ensure compatibility between libCEED and PETSc.

`HONEE <https://gitlab.com/phypid/honee>`_ (High-Order Navier-stokes Equation Evaluator) is a fluids dyamics library based on libCEED and PETSc with a particular focus on supporting Intel GPUs.
HONEE uses the Navier-Stokes equations :cite:`shakib1991femcfd` with continuous-Galerkin stabilized finite element methods, namely SUPG :cite:`hughesetal2010`, focusing on scale-resolving simulations.
Effort is made to maintain flexibility in state variable choice, boundary conditions, time integration scheme (both implicit and explicit).
I developed the original libCEED fluid dynamics mini-app that HONEE was based on and maintain and expand core infrastructure in libCEED to support HONEE.

`Ratel <https://gitlab.com/micromorph/ratel>`_ is a solid mechanics library that provides material models and boundary conditions implemented using libCEED and PETSc.
Ratel supports both finite element (FEM) and implicit material point method (iMPM) :cite:`MPM_Coombs2020, moresi2003lagrangian` simulations; with users being able to compare output for both methods with supported models.
Ratel's material model library includes finite-strain hyperelastic, elastoplastic, viscoelastic, poroelastic, and fracture models, including stable mixed formulations for near-incompressible regimes.
Ratel users can take advantage of the packages and algorithms supported by PETSc, including Hypre :cite:`falgout2021porting` and Kokkos :cite:`trott2022kokkos`, highlighting the benefits of leveraging open source software in research applications.

As the architect for Ratel, I work with the researchers and students implementing and using the material models to ensure the software best supports ongoing research.
Development of iMPM models is a particularly innovative feature, as matrix-free implicit MPM on GPU hardware for CU Boulder's PSAAP Multidisciplinary Simulation Center offers an ability to run simulations with this technology significantly faster than other currently available software packages, allowing a larger number of runs to be completed and incorporated into more complex analysis of the results, such as uncertainty quantification.
Also, preconditioning for iMPM operators offers unique challenges compared to FEM operators and is a particularly rich area for research.

All of these software efforts allow me to work with a wide range of contributors and support the work of an even larger range of collaborators.
Additionally, while code review is designed to strengthen the end quality of software products, it also provides a natural vehicle for mentoring students in research practices.


Preconditioning
--------------------------------------------------------------------------------

The iteration count to reach convergence for Krylov subspace methods is based, in part, upon condition number of the operator :cite:`luenberger1973introduction`, and high-order finite element operators have notoriously poor condition numbers :cite:`hu1998bounds`.
Preconditioners help control the condition number of high-order finite elements implemented in a matrix-free fashion and therefore reduce total iteration count and total time to solution for these operators.

Multigrid methods are popular multi-level techniques that provide resolution independent convergence rates.
:math:`p`-type multigrid, developed by Ronquist and Patera :cite:`ronquist1987spectral`, is a natural choice for high-order finite elements on an unstructured mesh, can be implemented in a matrix-free fashion, and can offer more flexibility than :math:`h`-multigrid on meshes for complex problems.

Local Fourier Analysis (LFA) provides a tool to predict the convergence of preconditioning techniques for finite element and finite difference methods.
LFA :cite:`brandt1977multi` was originally developed in the context of analyzing :math:`h`-multigrid methods for finite difference methods, but since then LFA has been used to analyze finite element methods and a variety of preconditioning techniques.
I wrote the Julia package `LFAToolkit.jl <https://www.github.com/jeremylt/LFAToolkit.jl>`_ :cite:`thompson2021toolkit`, a toolkit for analyzing the performance of preconditioners a priori for arbitrary, user provided weak forms of second order PDEs.
While this technique is not designed for complex meshes use in many research simulations, it offers good intuition on how preconditioners will perform on more complex meshes and offers a rigorous way to compare the performance of different preconditioners and parameter values for the same problem.

With appropriate parameter tuning, these preconditioning techniques can greatly improve the total iteration count and therefore the end to end runtime for scientific simulations in HONEE and Ratel.
This allows us to make better us of resources and complete more simulations with the same allocation of HPC resources.


Future Work
--------------------------------------------------------------------------------

I thrive in large research projects, such as the Center for Efficient Exascale Discretizations (CEED) as part of the Exascale Computing Project (ECP) and the Center for Micromorphic Multiphysics Porous and Particulate Materials Simulations within Exascale Computing Workflows as part of the Predictive Science Academic Alliance Program (PSAAP), and have helped make connections between libCEED and larger open source software packages, such as PETSc, MFEM, and deal.II.
My work in libCEED is partially funded in the FASTMath Institute of the Scientific Discovery through Advanced Computing (SciDAC).
I am working to use the relationships I have established via this work to help identify funding for myself and graduate students.

I have contributed to the proposal for the renewal FASTMath for SciDAC-6 and intend to pursue further partnerships as part of the upcoming SciDAC applications call.
I have participated in a Small Business Innovation and Research (SBIR) proposal and anticipate future funding diversification will require a mix of government lab and industry partnerships.
As computational needs grow and hardware technology continues to advance, performance portable software will continue to be an important area of research with wide range of stakeholders.


References
--------------------------------------------------------------------------------

.. bibliography::
   :filter: {"research"} & docnames
