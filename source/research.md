Research Statement
********************************************************************************

High-order matrix-free finite element operators offer superior performance on modern high performance computing (HPC) hardware when compared to assembled sparse matrices, both with respect to the number of floating point operations needed for operator evaluation and the memory transfer needed for a matrix-vector product.
However, high-order matrix-free operators require iterative solvers, such as Krylov subspace methods, and these iterative solvers converge slowly for the ill-conditioned operators that come from high-order discretizations.
Preconditioning techniques can significantly improve the convergence of these iterative solvers for high-order matrix-free finite element operators.

In my research, I focus on using high-order matrix-free methods to acchieve high performance on modern HPC hardware.
I build core computational infrastructure and preconditioners to support a variety of application areas.
To this end, my research efforts are centered around building open source software packages while enabling and accelerating the research of students and researchers in our group and among our collaborators who are using these packages for fluid dynamics and solid mechanics applications.


High-Order Matrix-Free
--------------------------------------------------------------------------------

The developments in HPC hardware over the last thirty years make high-order matrix-free finite element operators increasingly attractive.
Two key performance metrics for HPC hardware are Floating Point Operations per Second (FLOPs) and memory and network bandwidth.
FLOPs is the more widely popularized of these two metrics, but memory and network bandwidth is a common bottleneck in HPC application codes.

Over the last thirty years, the maximum FLOP rates for new HPC hardware have been increasing more rapidly than memory bandwidth and network bandwidth, for both CPUs and GPUs.
As discussed in McCalpin's Supercomputing 2016 invited talk {cite}`mccalpin2016memory`, maximum FLOPs per socket have been increasing at a rate of 50-60\% per year while memory bandwidth has only been increasing at a rate of approximately 23\% per year and network bandwidth has only been increasing at a rate of approximately 20\% per year.
This means that FLOPs have improved approximately twice as much as memory and network bandwidth over the last thirty years.
This problem is exacerbated by network latency, which is decreasing at a rate of approximately 20% per year, and memory latency, which is increasing at a rate of approximately 20% per year.
Additionally, communication between the host and device for GPU based systems introduces yet another source of communication latency.

The Top 500 {cite}`meuertop500` list tracks the 500 supercomputers with the highest maximum FLOPs, as measured by High-Performance Linpack (HPL) {cite}`petitethpl`.
HPL measures the system performance when solving random dense linear systems in double precision via LU factorization and provides the maximum achievable FLOPs for the machine.
The machines on the Top 500 list have exascale FLOP rates, $10^{18}$ FLOPs.

Other benchmarks, such as High-Performance Geometric Multigrid (HPGMG) {cite}`adams2014hpgmg` and High-Performance Conjugate Gradient (HPCG) {cite}`dongarra2016high`, measure performance based upon solving a more complex benchmark problem.
The Top 500 {cite}`meuertop500` HPCG list achieves far lower maximum FLOP rates than the maximum FLOP rates seen in the Top 500 HPL list.
The disparity between the FLOPs achieved in benchmarks such as HPGMG and HPCG and the maximum FLOPs measured by HPL is partially explained by the growing gap between FLOPs and memory and network bandwidth on modern HPC hardware.


Open Source Scientific Software
--------------------------------------------------------------------------------


High-Order Matrix-Free
--------------------------------------------------------------------------------

