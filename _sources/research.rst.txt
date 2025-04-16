Research Statement
********************************************************************************

Open Source Scientific Software for Modern HPC Hardware
--------------------------------------------------------------------------------

Many fluid dynamics and solid mechanics applications use finite-element like discretizations of the physically based PDEs in simulations modeling behavior of interest.
High-order matrix-free finite element-like operators on elements with tensor-product bases offer superior performance on modern high performance computing (HPC) hardware when compared to assembled sparse matrices, both with respect to the number of floating point operations needed for operator evaluation and the memory transfer needed for a matrix-vector product.
However, matrix-free operators require iterative solvers, such as Krylov subspace methods, and these iterative solvers converge slowly for high-order operators because these operators tend to be increasingly ill-conditioned as polynomial order of the bases increases.
Preconditioning techniques can significantly improve the convergence of these iterative solvers for high-order matrix-free finite element operators.

In my research, I focus on using high-order matrix-free methods with appropriate preconditioners to achieve high performance on modern HPC hardware.
I build core computational infrastructure and preconditioners to support a variety of application areas.
To this end, my research efforts are centered around building open source software packages while enabling and accelerating the research of students and researchers in our group and among our collaborators who are using these packages for fluid dynamics and solid mechanics applications.


High-Order Matrix-Free
--------------------------------------------------------------------------------

Two key performance metrics for HPC hardware are Floating Point Operations per Second (FLOPs) and memory and network bandwidth.
FLOPs is the more widely popularized of these two metrics, but memory and network bandwidth is a common bottleneck in HPC application codes.

The ratio of FLOPs to memory bandwidth required for high-order matrix-free finite element-like operators on elements with tensor-product bases is closer to the capabilities of modern HPC hardware than the ratio for assembled sparse matrices.
While generation of high quality hexahedral meshes for tensor-product finite elements is a time intensive process when compared to the generation of simplex meshes, it is possible to generate meshes comprised predominately, but not necessarily exclusively, of high quality hexahedral elements with little additional effort when compared to the creation of a simplex mesh.
Thus, the performance benefits of high-order matrix-free finite-like operators with tensor-product structure can be realized without the substantial additional effort required to generate a mesh exclusively composed of high quality hexahedral elements.

Over the last thirty years, the maximum FLOP rates for new HPC hardware have been increasing more rapidly than memory bandwidth and network bandwidth, for both CPUs and GPUs.
As discussed in McCalpin's Supercomputing 2016 invited talk :cite:`mccalpin2016memory`, maximum FLOPs per socket have been increasing at a rate of 50-60\% per year while memory bandwidth has only been increasing at a rate of approximately 23\% per year and network bandwidth has only been increasing at a rate of approximately 20\% per year.
This means that FLOPs have improved approximately twice as much as memory and network bandwidth over the last thirty years.
This problem is exacerbated by network latency, which is decreasing at a rate of approximately 20% per year, and memory latency, which is *increasing* at a rate of approximately 20% per year.
Additionally, communication between the host and device for GPU based systems introduces yet another source of communication latency.

The Top 500 :cite:`meuertop500` list tracks the 500 supercomputers with the highest maximum FLOPs, as measured by High-Performance Linpack (HPL) :cite:`petitethpl`.
HPL measures the system performance when solving random dense linear systems in double precision via LU factorization and provides the maximum achievable FLOPs for the machine.
The machines on the Top 500 list have exascale FLOP rates, :math:`10^{18}` FLOPs.

Other benchmarks, such as High-Performance Geometric Multigrid (HPGMG) :cite:`adams2014hpgmg` and High-Performance Conjugate Gradient (HPCG) :cite:`dongarra2016high`, measure performance based upon solving a more complex benchmark problem.
The Top 500 :cite:`meuertop500` HPCG list achieves far lower maximum FLOP rates than the maximum FLOP rates seen in the Top 500 HPL list.

The disparity between the FLOPs achieved in benchmarks such as HPGMG and HPCG and the maximum FLOPs measured by HPL is partially explained by the growing gap between FLOPs and memory and network bandwidth on modern HPC hardware.
This is particularly noticeable on many GPU based HPC machines.
Using high-order matrix-free finite element-like operators for simulations on meshes populated predominately with elements with tensor-product bases allows scientific simulations to run closer to the maximum achievable FLOPs for the machine.

High-order finite elements also offer high accuracy and exponential convergence for sufficiently smooth problems.
Often exponential convergence is not required to meet engineering tolerances and the smoothness of the solution may prevent exponential convergence from being achieved in practical problems.
However, high-order finite elements will still offer convergence that is no worse than the convergence on a comparable low-order mesh with a larger number of elements.
For these problems, high-order finite elements implemented in a matrix-free fashion still offer the memory bandwidth and FLOPs benefits detailed above.
For further discussion of the convergence of high-order methods, see :cite:`babuvska1994p,babuska1982rates,guo1986hp`, among others.

Although the benefits of high-order matrix-free implementations are well understood on modern HPC hardware, a significant amount of software development and research may be required to for a specific model needed in a simulation.
Direct solvers like LU factorization are no longer available and iterative solvers with appropriate preconditioners are required.


Open Source Scientific Software
--------------------------------------------------------------------------------

Transparency and reproducibility are the lifeblood of scientific and software advancement.
I strive to make all of my software open source and freely available, utilizing best practices for modern software development.

The implementation of the high-order matrix-free finite element-like operators can be found in the `libCEED GitHub repository <https://www.github.com/CEED/libCEED>`_, along with fluid dynamics and solid mechanics mini-applications.
libCEED :cite:`libceed, libceed-user-manual` is a low-level library for the efficient high-order discretization methods developed by the ECP co-design Center for Efficient Exascale Discretizations (CEED).
LibCEED has multiple backends that can be selected at runtime, and these backends target CPU architectures :cite:`libxsmm`, NVIDIA GPUs :cite:`CUDAwebsite`, AMD GPUs :cite:`HIPwebsite`, and Intel GPUs.
While the focus is on high-order finite elements, the approach used in libCEED is mostly algebraic and thus applicable to other discretizations in factored form.
LibCEED is the core component of my research efforts, with core implementations for the PDE based operators required for our fluid dynamics and solid mechanics simulations.

These simulations rely upon the the linear and nonlinear solver and preconditioning infrastructure found in `PETSc <https://www.mcs.anl.gov/petsc/>`_ :cite:`petsc-user-ref`, the Portable, Extensible Toolkit for Scientific Computation.
PETSc is a suite of data structures and routines for the scalable, parallel solution of scientific applications modeled by partial differential equations.
As libCEED's lead developer, I make contributions to PETSc to help ensure compatibility between libCEED and PETSc.

`HONEE <https://gitlab.com/phypid/honee>`_ (High-Order Navier-stokes Equation Evaluator) is a fluids dyamics library based on libCEED and PETSc with a particular focus on supporting Intel GPUs.
HONEE uses the Navier-Stokes equations :cite:`shakib1991femcfd` with continuous-Galerkin stabilized finite element methods, namely SUPG :cite:`hughesetal2010`, focusing on scale-resolving simulations.
Effort is made to maintain flexibility in state variable choice, boundary conditions, time integration scheme (both implicit and explicit), and other solver choices.
I developed the original libCEED fluid dynamics mini-app that HONEE was based on and maintain and expand core infrastructure in libCEED to support HONEE.

`Ratel <https://gitlab.com/micromorph/ratel>`_ is a solid mechanics library that provides material models and boundary conditions implemented using libCEED and PETSc.
Ratel supports both finite element (FEM) and implicit material point method (iMPM) :cite:`MPM_Coombs2020, moresi2003lagrangian` simulations; with users being able to compare output for both methods with supported models.
Ratel's material model library includes finite-strain hyperelastic, elastoplastic, viscoelastic, poroelastic, and fracture models, including stable mixed formulations for near-incompressible regimes.
Ratel users can also take advantage of all the packages and algorithms supported by PETSc, including Hypre :cite:`falgout2021porting` and Kokkos :cite:`trott2022kokkos`, which highlights the benefits of leveraging open source software in research applications.
As the architect for Ratel, I work with the researchers and students implementing and using the material models in Ratel to ensure the software best supports our ongoing research.


Preconditioning
--------------------------------------------------------------------------------

The iteration count to reach convergence for Krylov subspace methods is based, in part, upon condition number of the operator :cite:`luenberger1973introduction`, and high-order finite element operators have notoriously poor condition numbers :cite:`hu1998bounds`.
Preconditioners help control the condition number of high-order finite elements implemented in a matrix-free fashion and therefore reduce total iteration count and total time to solution for these operators.

Multigrid methods are popular multi-level techniques that provide resolution independent convergence rates.
:math:`p`-type multigrid, developed by Ronquist and Patera :cite:`ronquist1987spectral`, is a natural choice for high-order finite elements on an unstructured mesh and can be implemented with operators implemented in a matrix-free fashion.
Additionally, :math:`p`-multigrid can offer more flexibility with respect to meshes in comparison to :math:`h`-multigrid as it does not require aggregation of multiple elements into larger elements, which can be difficult on more complex geometry.

Local Fourier Analysis (LFA) provides a tool to predict the convergence of preconditioning techniques for finite element and finite difference methods.
LFA :cite:`brandt1977multi` was originally developed in the context of analyzing :math:`h`-multigrid methods for finite difference methods, but since then LFA has been used to analyze finite element methods and a variety of preconditioning techniques.
Our development of LFA of :math:`p`-multigrid and Balancing Domain Decomposition by Constraints for single high-order finite element subdomains for general finite element operators is a novel addition to the field.
I wrote the Julia package `LFAToolkit.jl <https://www.github.com/jeremylt/LFAToolkit.jl>`_ :cite:`thompson2021toolkit`, a toolkit for analyzing the performance of preconditioners a priori for arbitrary, user provided weak forms of second order PDEs.

Analyzing and implementing new preconditioning techniques can greatly improve the total iteration count and therefore the end to end runtime for scientific simulations in HONEE and Ratel.
This allows us to make better us of resources and complete more simulations with the same allocation of HPC resources.


References
--------------------------------------------------------------------------------

.. bibliography::
