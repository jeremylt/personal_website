Software
********************************************************************************

.. |fa-github| raw:: html

    <i class="fa-fw fab fa-github"></i>

.. |fa-gitlab| raw:: html

    <i class="fa-fw fab fa-gitlab"></i>

| |fa-gitlab|   GitLab:             `jeremylt <https://www.gitlab.com/jeremylt>`__
| |fa-github|   GitHub:             `jeremylt <https://www.github.com/jeremylt>`__


`libCEED <https://www.github.com/CEED/libCEED>`_
--------------------------------------------------------------------------------

.. figure:: img/libCEEDLogo.webp
    :alt: libCEED logo
    :width: 225px

libCEED provides fast algebra for element-based discretizations, designed for performance portability, run-time flexibility, and clean embedding in higher level libraries and applications. It offers a C99 interface as well as bindings for Fortran, `Python <https://pypi.org/project/libceed/>`_, `Julia <https://juliapackages.com/p/libceed>`_ , and `Rust <https://lib.rs/crates/libceed>`_.
While our focus is on high-order finite elements, the approach is mostly algebraic and thus applicable to other discretizations in factored form.

`Ratel <https://gitlab.com/micromorph/ratel>`_
--------------------------------------------------------------------------------

.. figure:: img/RatelLogo.webp
    :alt: Ratel logo
    :width: 350px

Ratel provides solid mechanics solvers based on `libCEED <https://www.github.com/CEED/libCEED>`_ and `PETSc <https://petsc.org>`_.
The library provides hyperelastic, plasticity, damage, and poroelasticity formulations, with static, quasistatic, and fully dynamic examples.
Most examples use high order finite elements, but Ratel also provides Material Point Method (MPM) in a matrix free fashion many of the material models.

.. figure:: img/SolidsTwist.webp
    :alt: Static elasticity example, twisting beam
    :width: 748px

    Solid mechanics example of beam deforming under twisting force.

`HONEE <https://gitlab.com/phypid/honee>`_
--------------------------------------------------------------------------------

HONEE provides fluid dynamics solvers based on `libCEED <https://www.github.com/CEED/libCEED>`_ and `PETSc <https://petsc.org>`_.
The library solves the compressible Navier-Stokes equations in three dimensions using explicit or implicit time integration.

.. figure:: img/FluidsVortices.webp
    :alt: Fluid dynamics example, cold air vortices
    :width: 748px

    Fluid dynamics example of vortices from falling cold air bubble.

`LFAToolkit.jl <https://www.github.com/jeremylt/LFAToolkit.jl>`_
--------------------------------------------------------------------------------

Local Fourier Analysis is a tool commonly used in the analysis of multigrid and multilevel algorithms for solving partial differential equations via finite element or finite difference methods.
This analysis can be used to predict convergence rates and optimize parameters in multilevel methods and preconditioners.
This package provides a toolkit for analyzing the performance of preconditioners for arbitrary, user provided weak forms of partial differential equations.

.. figure:: img/LFAToolkit.webp
    :alt: Local Fourier Analysis, p-multigrid on high-order element
    :width: 320px

    Local Fourier Analysis of p-multigrid for high-order finite element.
