4C Initial GPU Porting
***************************************************************************

I am starting the `4C <https://github.com/4C-multiphysics/4C>`_ GPU porting, beginning with the `particle` module.
We have selected to use `Kokkos <https://github.com/kokkos/kokkos>`_, as 4C has `Trilinos <https://github.com/trilinos/trilinos>`_ as a mandatory dependency, and Trilinos depends upon Kokkos.
The initial work enabling 4C to build with CUDA enabled Kokkos in Trilinos and target files for GPU compilation was done by Philip Pekrun in `this PR <https://github.com/4C-multiphysics/4C/pull/2012>`_, and this work will build upon that initial capability.
That work focused on supporting the optional dependency `MIRCO <https://github.com/imcs-compsim/MIRCO>`_, which supplies 'the boundary element algorithm for linear elastic frictionless normal contact between a rigid rough indentor and an elastic half-space'.

I am going to start by researching the basic structure of the 4C `particle` module to identify a few key pieces of information.
Ideally, this GPU porting, in its final form, will have nearly all computation inside of the `particle` module occurring on the device, with memory synchronization only occurring on the 'boundary' of the `particle` module where it interacts with other modules.
To this end, I need to identify that boundary and the important locations where data crosses that boundary.

I could, in theory, simply allocate a new Kokkos view on the device and transfer data to the device and the back to the host everywhere I wish to move computation to the device.
That would be technically correct but would be wasteful in terms of performance, as each allocation takes time, and the transfers themselves take time.
To that end, I want to identify where I can create persistent Kokkos views that mirror the CPU side data arrays and only pull down data from the device to the CPU side arrays when required.
The typical pattern I have seen for this is to place access to the data behind a getter and specify if the access is read-only or read-write and also specify if the access is on the host or device.
Then only the getter needs to manage synchronization between the two memory spaces.

I also need to identify the best portions of the code for GPU parallelization.
As a general rule, the best candidates are loops where the body of the loops ideally has regular data read and write access.
The write access can be across overlapping regions of data, but the write access should avoid writing to the same location in arrays, as this operation inherently must be done in serial, which bottlenecks the code.
Ideally, I want to identify regions that are reasonably good candidates which are close enough together in the control flow so that I am able to keep the data largely on the device as much as possible in the region of the code I am currently porting to the GPU.


Past efforts
===========================================================================

Rémi Bourgeois details porting TRUST to GPU with Kokkos `here <https://rbourgeois33.github.io/posts/post1>`_.
My initial reading of the blog post reinforces the idea that managing the amount of data transfers between host and device will be one of my most productive paths forward initially.
I plan on cross checking my experiences with this blog as I go along with the 4C particle module GPU porting efforts.


Initial plan
===========================================================================

This section is informed by the following sections; however, I wanted to put the most relevant information to readers earlier in this post.

- Phase 1: Update state value memory management

  - Update the `container` to use dual memory spaces
  - Will need to update getter, as below
  - Also need to update internals as needed, such as utils to resize
  - Will want to lazy allocate on device as not all device views will be needed at first
  - Need to identify any other memory to manage similarly, such as for rigid body

- Phase 2: Initial loops

  - Select candidate interaction loops to port
  - Start small and expand along control flow in regions that reduce memory movement
  - Need minimal and important test cases to consider

- Phase 3: Profiling

  - Identify major performance bottlenecks
  - Anticipate main issues will be
    - Memory transfer costs
    - Atomic operations to updates from particle pairs
  - Begin mitigation, as needed, to reduce worst bottlenecks

- Phase 4: Rinse and repeat

  - Repeat Phase 2 and Phase 3 to expand the portions of code and models
  - Lots of content in the `algorithms` and `interactions` to incrementally target


Memory movement
===========================================================================

In this section I trace the memory movement to identify important parts of the memory to manage for GPU and host movement.

Particle module external interface
---------------------------------------------------------------------------

In the particle code, the `algorithm` submodule holds a `particle engine` instance and has full access to all methods and data.
Some external modules can access the particle `engine` submodule via the `4C_particle_engine_interface.hpp` header.
`ParticleObjShrdPtr` objects can be accessed externally in some cases, as well as vectors of index values.
I do not see in this header access to the state data.

This identifies an area where I need to ensure that I sync data down to the host to ensure compatibility with other 4C modules.
   

Particle module interfaces used
---------------------------------------------------------------------------

I am surveying the headers to other 4C modules used inside of the `particle` module to identify areas where significant data is communicated between the modules.
This would indicate places where memory synchronization logic is especially important.
The following 4C header files are used in various files inside of the `particle` module, listed by submodule:

Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <details> <summary>Click to expand</summary>

- 4C

  - config
  - global_data
  - adapter_algorithmbase
  - comm

    - mpi_utils
    - utils

  - io

    - .
    - input_parameter_container
    - pstream

  - utils

    - exceptions
    - function
    - function_of_time
    - parameter_list
    - parameter_list.fwd
    - result_test

- Teuchos

  - ParameterList
  - StandardParameterEntrValidators
  - TimeMonitor

.. raw:: html

   </details>

Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <details> <summary>Click to expand</summary>

- 4C

  - config
  - binstrategy
  - global_data
  - comm

    - mpi_utils
    - pack_helpers
    - parobject
    - parobjectactory
    - utils_factory

  - io

    - control
    - input

      - file
      - spec
      - spec_builders

    - pstream
    - value_parser
    - visualization_manager

  - linalg

    - fixedsizedmatrix
    - map
    - vector

  - utils

    - exceptions
    - parameter_list

- Teuchos

  - RCPStdSharedPtrConversions
  - Time
  - TimeMonitor

.. raw:: html

   </details>


Interaction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <details> <summary>Click to expand</summary>

- 4C

  - config
  - global_data
  - comm

    - exporter
    - mpi_utls
    - pack

      - buffer
      - helpers

    - parobject

  - fem

    - general

      - element
      - extract_values
      - utils_fem_shapefunctions

    - geometry

      - element_coordtrafo
      - position_array
      - searchtree

        - nearestobject
        - service

  - linalg

    - fixedsizematrx
    - serialdensevector

  - io

    - .
    - control
    - pstream
    - runtime_csv_writer
    - visualization_manager

  - mat

    - par_bundle
    - particle

      - base
      - dem
      - sph

        - boundary
        - fluid

      - wall_dem

  - utils

    - exceptions
    - function_of_time
    - parameter_list.fwd
    - std23_unreachable

- Teuchos

  - ParameterList
  - StandardParameterEntryValidators
  - TimeMonitor

.. raw:: html

   </details>

Rigid Body
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <details> <summary>Click to expand</summary>

- 4C

  - comm

    - mpi_utils
    - pack

      - buffer
      - helpers

    - parobject

  - io

    - .
    - control
    - input_parameter_container
    - visualization_manager

  - global_data
  - utils

    - exceptions
    - function
    - parameter_list.fwd
    - result_test

- Teuchos

  - TimeMonitor

.. raw:: html

   </details>

Wall
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <details> <summary>Click to expand</summary>

- 4C

  - config
  - global_data
  - comm

    - mpi_utils

  - fem

    - condition_utils
    - discretization
    - dofset_transparent
    - general

      - element
      - extract_values
      - node

    - geometry

      - searchtree_service

  - io

    - .
    - control
    - discretization_visualization_writer_mesh
    - input_parameter_container
    - pstream
    - visualization_parameters

  - linalg

    - fixedsizematrix
    - utils_sparse_algebra_manipulation
    - vector

  - mat

    - material_factory

  - solid_ele
  - utils

    - parameter_list.fwd
    - result_test

- Teuchos

  - ParameterList
  - RCPStdSharedPtrConversions

.. raw:: html

   </details>


Many of these headers seem to be related to basic utilities that I am not initially concerned about, such as configuration information.
It appears that the largest amount of data would need to be synced to the host when using the `linalg` and `mat` modules.
It also appears that some of the data from the `fem` module may be important to have access to on the device.

Synchronization will be needed before any MPI communication and file IO, as both of those tasks are CPU side.
`Kokkos does support CUDA-Aware MPI <https://kokkos.org/kokkos-core-wiki/usecases/MPI-Halo-Exchange#cuda-aware-mpi>`_, but I do not yet want to attempt to tackle any changes to 4C's MPI interface.


Particle methods
---------------------------------------------------------------------------

The method `container->get_ptr_to_state()` will need to return device or host memory, as appropriate.
Only setting `const` on the returned pointer seems to be the way to determine if this is read-only or read-write access.

The following approach, I believe, allows this `const`-ness to be tracked to facilitate memory sync

.. code:: c++

   enum MemorySpace
   {
     Default = 0, // Current Kokkos ExecutionSpace, which could be CPU
     Host = 1,    // Just CPU side
     Both = 2,    // Default and Host in sync
   }

   inline void sync_space(ParticleState state, MemorySpace space)
   {
     if (space == MemorySpace::Both) FOUR_C_THROW("pick one memory space to use at a time");
     if ((sync_[state] != space && sync_[state] != MemorySpace::Both) {
       // Copy from currently up to date space to target space
       Kokkos::deep_copy(states_[state][space], states_[state][sync_[state]]);
       sync_[state] = MemoryState::Both;
     }
   };

   inline const Kokkos::View<double *> get_state_view(ParticleState state, MemorySpace space = MemorySpace::Default)
   {
     sync_space(state, space);
     return const states_[state][space];
   };

   inline const Kokkos::View<double *> get_state_view(ParticleState state, MemorySpace space = MemorySpace::Default)
   {
     sync_space(state, space);
     sync_[state] = space; // Flag writable state as only one up to date
     return states_[state][space];
   };

Kokkos has a `DualView`; however, we are using Kokkos 4.7.4 and the `DualView` had changes in Kokkos 5.0.
As a result, I'm not sure if we want to roll our own version (above) or use theirs.
This point will require further research, especially since it is not clear to me how to specifically request the host and device views in Kokkos 5.0.

In any case, the code above shows the basic idea of the synchronization, as we want to keep track of when memory is modified and not.
Using the current getter allows us to be minimally intrusive and focus our changes in one location.
As an additional benefit, using the existing getter like this means we can change the internal implementation, such making changes to usage of a `DualView` for Kokkos 5.0, without it requiring changes in the rest of the code.

The proposed snippet above keeps the same approach of using separate Views (vectors) for each state, which would be synced and managed separately.
This could mean multiple separate copies from the device to the host inside of one function, but overall less data in each copy.
If the number of copies becomes a bottleneck, we can revisit that decision.
I do not know if Kokkos has some way to smartly manage multiple copies requested on back to back lines or if putting these Views inside of a getter affects any such capability.


Control flow
===========================================================================

In this subsection I look at the basic control flow of the time loop and attempt to locate candidates for parallelization and any potential issues that may arise.
The time loop has the following control flow:

1. prepare

.. raw:: html

   <details> <summary>Click to expand</summary>

- incrementing time
- set new time
- set timestep size
- set flags for writing output, restart files

.. raw:: html

   </details>


2. pre_evaluate

.. raw:: html

   <details> <summary>Click to expand</summary>

- particle interaction

  - SPH

    - prescribe open boundary states, if needed

.. raw:: html

   </details>

3. integrate

.. raw:: html

   <details> <summary>Click to expand</summary>

- intergrator specific pre-interaction routine
- update connectivity

  - check particle interaction distance wrt bin size

    - Note: need MPI communication

  - check wall nodes are in bounding box, if wall nodes present

    - Note: parallelization candidate, loop over all wall nodes

  - check if load transfer needed

    - transfer load between processors

      - Note: need CPU sync for MPI communication in `communicate_particle`

    - check redistribution
    - update ghost particles

      - Note: need CPU sync for MPI communication in `ghost_particles()`

    - build global to local index map
    - rebuild potential neighbor list, if particle interaction

      - Note: need tweak to parallelize, as modifies single `potentialparticleneighbors_` vector

  - if no load transfer needed

    - update ghost particle data

      - Note: still need CPU sync for MPI communication in `ghost_particles()`

- evaluate time step

  - clear rigid body forces and torques, if rigid body

    - Note: parallelize once rigid body computed on device

  - set gravity acceleration, if gravity

    - Note: parallelize once downstream computation is also on device
    - Note: `set_state_specific_container()` may want to set state in currently most up to date memory space or have optional argument to target specific space

  - evaluate interactions, if particle interaction

    - Note: modifies `particlepair` data, would need to tweak editing of single `particlepairdata_` vector

    - DEM

      - clear force and moment states

        - Note: parallelize once downstream is on device

      - evaluate neighbor pairs

        - Note: parallelization candidate, writes to individual pair data instead of to each particle

      - evaluate adhesion for neighbor pairs, if adhesion

        - Note: parallelization candidate, writes to individual pair data instead of to each particle

      - check critical time step, for contact
      - add force and moment contribution, for contact
 
        - Note: involves writing to both members of pairs, so atomic which may bottleneck

      - add force contribution from adhesion, if adhesion
 
        - Note: involves writing to both members of pairs, so atomic which may bottleneck

      - compute acceleration
      
        - Note: parallelization candidate

      - update history pairs

    - SPH

      - evaluate neighbor pairs

        - Note: parallelization candidate, writes to individual pair data instead of to each particle

      - evaluate peridynamics neighbor pairs, if peridynamics

        - Note: parallelization candidate, writes to individual pair data instead of to each particle

      - initialize positions of virtual wall particles, if virtual wall

        - Note: parallelize once downstream is on device

      - compute density

        - Note: parallelization complicated by particle pairs writing to each other

      - compute pressure

        - Note: parallelization candidate

      - compute surface tension interface, if surface tension

        - Note: parallelization complicated by particle pairs writing to each other

      - compute temperature field, if temperature

        - Note: parallelization complicated by particle pairs writing to each other

      - interpolate open boundary states
      - initialize boundary particle states, if boundary particles

        - Note: parallelize once downstream is on device

      - initialize states at wall contact points, if virtual wall

        - Note: parallelize once downstream is on device

      - add momentum contribution to acceleration
      
        - Note: parallelization candidate

      - add surface tension contribution to acceleration, if surface tension

        - Note: parallelization complicated by particle pairs writing to each other

      - add rigid particle contact contribution to force, if rigid body

        - Note: parallelization complicated by particle pairs writing to each other

      - add peridynamics contribution to acceleration, if peridynamics

        - Note: parallelization complicated by particle pairs writing to each other


  - apply viscous damping, if viscous damping
  - compute accelerations, if rigid body and particle interaction

    - Note: Involves MPI communication for acceleration on rigid body

- integrator specific post-interaction routine

.. raw:: html

   </details>

4. post_evaluate

.. raw:: html

   <details> <summary>Click to expand</summary>

- particle interaction
- rigid body phase change, if rigid body
- DEM

  - writing behavior

- SPH

  - check open boundary phase change, if open boundary
  - evaluate phase change, if phase change
  - evaluate peridynamic change, if peridynamics

.. raw:: html

   </details>

5. write output, restart files

The main point I take here is that the most important portion of the code to port initially appears to be the particle interaction routines, which makes sense considering how particle based methods work.
The particle pairs themselves track their own interactions and can be processed in parallel, but when those pairs write back data to the individual particles in the pair the portability layer will have to use atomic operations to ensure no conflicts, which means this portion will be slower than processing the interactions themselves.
I would implement in a straightforward fashion at first and then determine if this presents a performance bottleneck and if more extensive modifications are required.

One point to research is how to do parallel updates to the same vector.
This has to be solved somewhere and have a common strategy that is known to be adequate or optimal.


Metadata
================================================================================

Started: 17 Jul 2026

Last edited: 22 Jul 2026
