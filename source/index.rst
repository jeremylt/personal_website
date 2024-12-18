################################################################################
|icon| Jeremy L Thompson
################################################################################

.. meta::
   :description: Jeremy L Thompson, personal webpage

.. |icon| image:: img/Icon.webp
    :alt: JeremyLT icon
    :width: 50px

.. |fa-email| raw:: html

    <i class="fa-fw fas fa-envelope"></i>

.. |fa-pronouns| raw:: html

    <i class="fa-fw fa-solid fa-user"></i>

.. |fa-github| raw:: html

    <i class="fa-fw fab fa-github"></i>

.. |fa-gitlab| raw:: html

    <i class="fa-fw fab fa-gitlab"></i>

.. |fa-linked| raw:: html

    <i class="fa-fw fab fa-linkedin"></i>

.. |fa-fcc| raw:: html

    <i class="fa-fw fab fa-free-code-camp"></i>

.. |fa-orcid| raw:: html

    <i class="fa-fw fab fa-orcid"></i>

.. |fa-gscholar| raw:: html

    <i class="fa-fw fa-brands fa-google-scholar"></i>

.. |fa-research| raw:: html

    <i class="fa-fw fab fa-researchgate"></i>

.. |fa-d20| raw:: html

    <i class="fa-fw fas fa-dice-d20"></i>

.. |fa-mech| raw:: html

    <i class="fa-fw fa-solid fa-robot"></i>

.. |fa-discord| raw:: html

    <i class="fa-fw fa-brands fa-discord"></i>

.. |fa-bluesky| raw:: html

    <i class="fa-fw fa-brands fa-bluesky"></i>

.. |fa-language| raw:: html

    <i class="fa-fw fa-solid fa-language"></i>

.. |fa-book| raw:: html

    <i class="fa-fw fa-solid fa-book"></i>


Contact
********************************************************************************

| |fa-gitlab|   GitLab:             `jeremylt <https://www.gitlab.com/jeremylt>`__
| |fa-github|   GitHub:             `jeremylt <https://www.github.com/jeremylt>`__

| |fa-bluesky|  Bluesky:            `jeremylt <https://bsky.app/profile/jeremylt.bsky.social>`_
| |fa-discord|  Discord:            `jeremylt <https://discordapp.com/users/513148167923957761>`_
| |fa-linked|   LinkedIn:           `jeremylt <https://www.linkedin.com/in/jeremylt/>`__

| |fa-fcc|      freeCodeCamp:       `jeremylt <https://www.freecodecamp.org/jeremylt>`__
| |fa-fcc|      freeCodeCamp forum: `jeremylt <https://forum.freecodecamp.org/u/jeremylt/summary>`__

| |fa-orcid|    ORCiD:              `0000-0003-2980-0899 <https://orcid.org/0000-0003-2980-0899>`_
| |fa-research| ResearchGate:       `Jeremy L Thompson <https://www.researchgate.net/profile/Jeremy-Thompson>`__
| |fa-gscholar| Google Scholar:     `Jeremy L Thompson <https://scholar.google.com/citations?user=UCKh6wcAAAAJ>`__

| |fa-pronouns| pronouns:           he/they
| |fa-email|    email:              `jeremy (at) jeremylt.org <mailto:jeremy@jeremylt.org>`__
| |fa-language| languages:          English (native), German (A2-B1)


Background
********************************************************************************

I am a research software engineer, applied mathematician, and STEM educator.
My experience includes `performance portable software development <https://ceed.exascaleproject.org/>`_ for `physics based simulations <https://micromorph.gitlab.io/>`_ on exascale hardware as part of centers funded by grants from the Department of Energy and statistical analysis for the `U.S. Air Force <https://en.wikipedia.org/wiki/49th_Test_and_Evaluation_Squadron>`_.
I have professional experience in C, Rust, Python, C++, CUDA, Julia, Fortran, and R, among other languages.
I have taught at the `U.S. Air Force Academy <https://www.usafa.edu/department/mathematics/>`_ and `University of Colorado at Boulder <https://www.colorado.edu/amath/>`_, and I am a mentor online at `freeCodeCamp <https://www.freecodecamp.org/>`_ and help moderate the `freeCodeCamp Discord <https://www.freecodecamp.org/news/freecodecamp-discord-chat-room-server/>`_ and `freeCodeCamp Forums <https://forum.freecodecamp.org/>`_.


Software
********************************************************************************

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


Publications and Presentations
********************************************************************************

A list of my publications can be found on `ORCiD <https://orcid.org/0000-0003-2980-0899>`_, `ResearchGate <https://www.researchgate.net/profile/Jeremy-Thompson>`_, and `Google Scholar <https://scholar.google.com/citations?user=UCKh6wcAAAAJ>`_.
The source and PDFs of my presentations can be found on `GitHub <https://github.com/jeremylt/Presentations>`_.


Hobbies
********************************************************************************

BattleTech
--------------------------------------------------------------------------------

.. figure:: img/COBattleTechLogo.webp
    :alt: Colorado BattleTech logo
    :width: 250px

I enjoy playing BattleTech and run demos as part of the `Catalyst Demo Team <https://sites.google.com/view/catalystdemoteam/home>`_.
It is especially important to me for new players to feel safe and welcome joining this hobby space.
See the `Colorado BattleTech <https://coloradobt.org>`_ website to find BattleTech players in Colorado.
I also help moderate the `Catalyst Game Labs Discord <https://discord.com/invite/catalystgamelabs>`_ community.

.. figure:: img/BattleTechOutworldsWastesLogo.webp
    :alt: BattleTech Outworlds Wastes logo
    :width: 250px

I've developed a lightweight narrative league and event framework with simplified logistics rules, BattleTech: Outworlds Wastes.

| |fa-mech| `BattleTech: Outworlds Wastes <https://outworlds-wastes.jeremylt.org>`_: lightweight narrative league and event framework

.. figure:: img/MercenarysPrideLogo.webp
    :alt: Mercenary's Pride logo
    :width: 250px

Mercenary's Pride is a fun project retelling Jane Austin's Pride and Prejudice as a series of BattleTech scenarios and comm logs.

| |fa-book| `Mercenary's Pride <https://mercenarys-pride.jeremylt.org/>`_: retelling Pride and Prejudice in BattleTech

Dungeons & Dragons
--------------------------------------------------------------------------------

The lore for my home D&D games can be found here:

| |fa-d20| `Theaceae <https://theaceae.jeremylt.org/>`_:    the land of tea, treasure, and adventure
| |fa-d20| `Astral Sea <https://astralsea.jeremylt.org/>`_: the realm between realms, full of intrigue and mystery
