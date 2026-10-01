Software Development Lifecycle Techniques in LLM Workflows
********************************************************************************

I attended the `Workshop on AI-supported Research Software Engineering <https://de-rse.org/workshop-AI-supported-RSE-Sept26>`_ hosted by de-RSE which preceded the annual de-RSE Collaboration Workshop.
In particular, I attended the Quality Assurance in the Age of AI session hosted by Harald Mack and Tuyen Le, and the From Code Generation to Control: Engineering Reliable Software with AI session hosted by Edwin Carreño and Maxim Scheremetjew from the various parallel session options.
Purely estimating by the 'eyeball norm' and the fact that these sessions were held in the largest space, I think concerns around quality and reliability are high priorities for many Research Software Engineers (RSEs).

A common idea from these two sessions and discussions throughout the week is that Software Development Lifecycle (SDLC) techniques can be used to help ensure the output code quality is higher, particularly when compared to simply 'vibecoding'.
I will outline what exactly SDLC is before discussing how these techniques were discussed in the workshop.

.. admonition:: Author's Note

   My discussion here and my takeaways from this workshop align well with `my other post <https://jeremylt.org/blog/research-software/ai-for-rse>`_ that I wrote at the start of the summer.
   Hopefully this means that my initial research into this topic was accurate and well aligned with what RSEs are experiencing.
   Hopefully this does not mean that I heard what I expected because of preconceived notions.


Software Development Lifecycle
================================================================================

The `Wikipedia article <https://wikipedia.org/wiki/Systems_development_life_cycle>`_ is a reasonable place to start to get oriented.
Wikipedia describes SLDC as 'the typical phases and progression between phases during the development of a computer-based system'.
More colloquially put, SDLC describes the separate phases of development when making a software product.
SDLC does not describe *how* these phases are accomplished but rather the general workflow.

The typical phases of SDLC are as follows

1. Conceptualization - conceptual design, options, and priorities are considered.
This phase is about deciding what should be built.

2. Requirements Analysis - specific needs that the software needs to meet are considered.
The requirements from this phase should become testable criteria for determining if the final software is truly finished.

3. Design - here the focus is on determining exactly 
This phase is about deciding how the software should be built.

4. Construction - finally we get to writing the code.
All of the required components should be built here, including tests and documentation.

5. Acceptance - software is reviewed and tested to verify it meets the requirements.
Software can be sent back to an earlier phase, such as construction or design, to address issues.

6. Deployment - software is accepted and released to the users.
The users will let us know if something did not truly meet the requirements.

7. Maintenance - this phase is about identifying and addressing issues.
Fixes to these issues may go through their own version of the first 6 phases.

8. Decommission - the software has reached the end of its useful life and we need to remove or replace it.

SDLC comes from decades of studying professional software development and is particularly important in managing large or complex codebases.
Lots of researchers prompt LLMs to generate code for them, and SDLC provides a framework to manage the large amounts of code and complexity from LLM output.
At a high level, teams using SDLC determine first what the software needs to do, then construct that software by whatever means, and finally look back at the software to judge if it meets the original requirements.

Steps 1-5 seem to receive the most focus when discussing the usage of LLMs in software development.
Personally I think that phase 7, maintenance, needs to be considered as well.
How easily can the end software product be maintained?
Does that answer change if we lose access to the current LLM based tools that were used?
There is a maintenance burden in scientific software because other researchers need to be able to use our tools to reproduce or extend our results.
However, that was not a primary focus of the sessions I attended.

SDLC and LLMs
================================================================================

With the basic idea of SDLC in place, we can contextualize the key takeaways from the sessions.


Quality Assurance in the Age of AI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This session focused on verification and validation.
The presenters nicely summarized that validation is determining if the right software is being built while verification determines if the software is being build right.
Put another way, verification determines if the software constructed correctly matches the requirements while validation determines if the software was designed to meet the correct requirements.

Both fit within the domain of quality control and quality assurance, where we identify and repair defects during the process of creating and maintaining the software.
As noted above, I see this as a key scientific responsibility for the generation of academic software, as we need to ensure that our software justifies our scientific claims and other researchers can reproduce and extend our work.

The presenters brought up two techniques to use during the construction phase, Test Driven Design (TDD) and Behavior Driven Design (BDD).
TDD is more widely known in academic circles in my experience - first tests are written to match the requirements, and then code is written to satisfy the tests.
Since these tests are derived from the requirements, they should ensure the correct outputs from the software instead of focusing on implementation specifics.

With BDD, first target behaviors for the users interacting with the software are written down.
These target behaviors are then used to generate the tests.
If the software passes these tests, then it should be meeting the specific ways in which the users plan to interact with the software, if those behaviors were accurately created and passed to the developer.

In both cases, the key takeaway is not only to clearly and precisely write the requirements before any code is authored but also to ensure that those requirements are formalized in such a way that it is clear if those requirements are met, specifically in this case by writing tests.


From Code Generation to Control: Engineering Reliable Software with AI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This session emphasized that ultimately the human is the decision maker in the process and is responsible for the outcome.
A lot of the same takeaways from the first session echoed here even though the two sessions were on separate days, with different presenters, and using two different LLM based workflows.

This presentation discussed a set of `skills <https://github.com/ecarrenolozano/ai-sdlc-skills>`_ to help developers using an agentic harness with the steps of SDLC.
These skills lead the developer through the stages described above (albeit with slightly different wording, but the same intent), and they also include a focus on TDD and BDD to ensure that the final software meets the requirements and intended usage.


Summary
================================================================================

Ultimately, this workshop emphasized to me that there is a lot of work to be done before code is created to ensure that the outcomes are clear before we start.
With the speed at which LLMs can generate code and the frequency that the code will compile and run even when it may not meet expectations of the human controlling the LLM, doing this work of formalizing the desired outcomes before construction/coding begins is even more important now.
I have seen plenty of us academics feel much more comfortable iteratively creating our requirements and code at the same time while we figure out what we want as we go along.
When using LLMs to generate large amounts of code, it becomes easy for a less intentional process to result in software that deviates from expectations in subtle but easy to overlook ways.

One point that I did not call out above but was also a frequent idea throughout the workshop was repeating SDLC concepts inside of an outer SDLC process.
For example, a researcher could be working on a larger feature and during the construction phase breaking the task down into subtasks, each with their own requirements, design, tests, implementation, and acceptance.

Ultimately, the discussions in this workshop align with my idea of 'defensive programming'.
In 'defensive programming', you assume the code is always wrong and try to detect and repair as many of these breakages as possible.
Even once you have found and repaired some bugs, there are always more because the code is always wrong.
If you are using an LLM, then it is itself a piece of code and is thus subject to the core principle of defensive programming - the code is always wrong.
For researchers choosing to incorporate LLMs into their workflows, this SDLC approach allows two critical decision points where a human has to exercise judgment - determining the requirements or acceptance criteria and determining if the code correctly meets those requirements or criteria.
This lets us concretely state what correct vs wrong outcomes would be and let us discover as many of the ways in which the code is wrong as we can, as early as we can.

Really, we should be doing this formalization of requirements and judging our results against those requirements even without LLM usage to ensure that we are building the right code and building the code right.
SDLC techniques help ensure that all of us researchers who generate code end up with code that correctly does what we expect.


Metadata
================================================================================

Started: 30 Sep 2026

Last edited: 01 Oct 2026
