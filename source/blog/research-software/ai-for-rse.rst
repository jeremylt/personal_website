Agentic AI Usage for RSEs
********************************************************************************

Research Software Engineers (RSEs) combine the expertise of professional software development with domain specific skills for academic research.
Several groups and professional declarations, such as the `Journal of Open Source Software <https://joss.theoj.org>`_ and the `San Francisco Declaration on Research Assessment <https://sfdora.org/read)>`_ have advocated for treating research software as first class artifacts, on par with peer-reviewed papers, especially for the purposes of career assessment and promotions for RSEs.
In order for RSEs to enrich scientific research and our software to be considered first class artifacts, we need to adhere to both software development best practices and professional research ethics.

Large Language Model (LLM) based development practices, including agentic AI (Happy Bhati provides a summary `here <https://arxiv.org/abs/2604.26275>`_), are changing software development workflows for many industry software engineers.
Best practices and areas of concern are solidifying on many industry software development teams; however these practices and concerns do not perfectly align with research software development due to both the differences between industry and academic software development and developers.
Furthemore, the the unique concerns of professional research ethics add additional constraints not present in industry software development.

In this article, we will discuss the ways in which developing LLM based best practices for industry software development do and do not map onto research software development.
We will also discuss the specific concerns that professional research ethics bring to research software development with agentic AI and other LLM based software development tools.

.. admonition:: Author's Note

   In this article, I am specifically focused on how emerging industry software development practices intersect with research software development and professional research standards.
   There is an important and interesting discussion to be had about the ethics of the LLM industry and what options may or may not exist for more ethical LLM based software development tools; however, there is not adequate space to have both discussions in this article.
   Both sets of concerns, practical and ethical, need to be addressed for agentic AI and other LLM based software development tools to be incorporated into research software development practices.

Ultimately, researchers who let AI/LLMs write their code will have bad code.
Software developers who let AI/LLMs do their research will violate research ethics.
As experts in two domains - research and software development - RSEs require skills in both professional software development and research practices to ensure they meet the quality and ethical standards in both domains.


Industry Best Practices
================================================================================

The response to so called agentic AI in industry software development teams has been varied.
In this section, we will identify some common trends and best practices that are emerging and compare those against the known differences between academic and industry software development.

.. admonition:: Author's Note

   It has proven somewhat difficult to find more neutral or pragmatic academic papers discussing agentic AI development practices.
   This may be due to the amount of research that is funded by industry on this topic (MIT's Sloan School discusses this `here <https://mitsloan.mit.edu/ideas-made-to-matter/study-industry-now-dominates-ai-research>`_ and MIT's Initiative on the Digital Economy `here <https://ide.mit.edu/wp-content/uploads/2023/03/0303PolicyForum_Ai_FF-2.pdf>`_) and the profit motives therein.
   This could also be due to a broader trend in scientific research articles towards positive language over the last 25 years (Yuan and Yao discuss this `here <https://pmc.ncbi.nlm.nih.gov/articles/PMC9526210/pdf/11192_2022_Article_4515.pdf>`_).
   Or it could be due to my personal search process only producing positive results.
   Or perhaps this is due to other contributing factors.
   In any case, I have included written accounts from senior software developers in industry in this section to provide a more pragmatic assessment of current best practices and concerns in usage.

Industry Practice
-------------------------------------------------------------------------------

Some industry software development teams have reported benefits to using LLMs or agentic AI in their software development workflows; however, these benefits are deeply tied to the workflows and quality standards of these teams.
These benefits do not easily translate into software development that does not include these mechanisms.

The concept of the `Software Development Life Cycle (SLDC) <https://en.wikipedia.org/wiki/Systems_development_life_cycle>`_ is important in industry software development.
The exact steps of the SDLC depend upon the exact model, but it can be broken approximately into 3 phases: planning, development, and review.
In the planning phase, the developers determine what a new feature needs to do and how it should be designed - a 'definition of done' is agreed upon before the development is started.
In the development phase, the code itself is written along with unit tests and documentation as needed.
Finally, in the review phase, the developers review the code and determine if it meets requirements and quality standards.
Industry best practices center around incorporating LLMs into their existing SDLC practices while RSEs tend to only loosely follow a SDLC, if at all.
This planning and review structure helps control LLM output quality, and RSEs need similar structure if we want to see the benefits that some industry development teams have observed.
This pattern can be replicated in a smaller scale during the development phase to prompt, generate, and review code from and LLM.
The smaller pieces are easier for humans to review, helping control quality and ensure developer intent is met.

.. admonition:: Author's Note

   We academics seem to be particularly alergic to these sorts of software development processes.
   Perhaps we feel they are too constrictive or we are simiply unfamiliar with them due to a lack of training.
   In any case, LLMs can only generate output, not decisions, so some sort of framework for planning and then reviewing the generated content is required, as ultimately the humans (the RSEs) are responsible for the work we submit.

Adam Tornhill provides quality focused best practices `here <https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality>`_).
A common theme throughout his article is that agentic AI relies upon healthy, high quality codebases and testing to control risk and produce high quality output code.
Specifically, he notes that AI models have no understanding of maintainability or charge risk inside of a codebase and can easily generate 'unhealthy' code (see discussion `here <https://codescene.io/docs/guides/technical/code-health.html#code-health-identifies-factors-known-to-impact-maintenance-costs-and-delivery-risks>`_) and perform better in codebase with 'healthy' code (see discussion `here <https://arxiv.org/abs/2601.02200>`_).
Largely, this means that a codebase that follows best practices for human code development is a prerequisite for successful development with agentic AI.
A similar finding linking code quality and LLM output quality was also discussed by Borg et al. `here <https://arxiv.org/abs/2601.02200>`_.
Tornhill notes that disciplined engineering practices with planning, review, and testing are required.

.. admonition:: Author's Note

   I have found a limited diversity of sources for this sort of research, with most of it coming from one group, but the research here matches my impressions from discussions with industry software developers.
   Many of the resources I have found in this section all seem to be associated with the CodeHealth tool from CodeScene, a company that provides enterprise software tools for industry software development teams.
   See my comment above about the difficulty in finding quality articles about best practices for using agentic AI and LLM based software development tools due, in part, to the amount of money and the profit motives that generates.

Research Software Engineer Challenges
-------------------------------------------------------------------------------

Unfortunately, RSEs frequently encounter difficulties meeting standard industry best practices for software development (see discussion by Anzt et al. `here <https://arxiv.org/abs/2005.01469>`_ for discussion of specific challenges faced in Germany and by Carver at al. `here <https://arxiv.org/abs/2103.01880>`_ for similar challenges in the United States).
In particular, sufficient training and resources particularly are a common challenge for RSEs.
This is exacerbated by unstable or unclear career trajectories that make it difficult for research teams to identify, train, and retain individuals with the appropriate interests and skills for research software development.
Arvanitou et al. summarized these concerns nicely `here <https://arxiv.org/abs/2010.09pdf914>`_ and showed that adherence to best practices focused on performance, maintainability, and development productivity improve quality.
The challenges around training and resources unfortunately make it difficult to deliver the prerequisite codebase quality required to implement Tornhill's suggestions.
If RSEs frequently do not have adequate training in software development and quality usage of agentic AI or other LLM based software development tools relies upon disciplined engineering practices, that places research software development at particular risk for low quality software being generated by these tools.

Of particular interest, given the difficulties with research software engineering training, is the risk of deskilling (discussed by Gerlich `here <https://www.mdpi.com/2075-4698/15/1/6>`_ and by Rinta-Kahila et al. `here <https://www.researchgate.net/publication/373783469_The_Vicious_Circles_of_Skill_Erosion_A_Case_Study_of_Cognitive_Automation>`_) or degraded skill formation (discussed by Shen and Tamkin `here <https://arxiv.org/abs/2601.20245>`_).
One particular risk of skill erosion or degraded skill formation is that if the automatic tools become prohibitively expensive, then this leaves organizations unable to complete critical tasks if they have become reliant upon the tools (LLM/AI based software development tools in this case).
Additionally, skill erosion or degraded skill formation also makes it more difficult to detect incorrect output from agentic AI and other LLM based software development tools.
Again, RSEs frequently do not have adequate training in software development and quality usage of agentic AI or other LLM based software development tools relies upon disciplined engineering practices.
Therefore, skill degradation or degraded skill formation poses a significant risk for the quality of academic software.

Additionally, Stetskov notes the increased code review time required with heavy use of LLM based coding tools `here <https://techtrenches.dev/p/the-human-cost-of-10x-how-ai-is-physically>`_ and the fact that agentic AI tools do not always produce outputs that meet all constraints in the provided instructions (as discussed `here <https://techtrenches.dev/p/your-claudemd-is-a-wish-list-not>`_).
Considering the fact that LLMs do not process instructions like deterministic software or understand instructions like humans and instead generate statistically likely outputs given the inputs, it is not surprising that instructions are not always respected in the generated output.
Critically, Stetskov notes the importance of senior developer skill in catching errors in generated code, which is problematic when considering the issues around training and skill acquisition for RSEs.
Additionally, time is consistently a constrained resource for research teams, but high quality code review is a time consuming activity.
As a result of these constraints, it can be difficult for RSEs to implement industry best practices intended to ensure high quality code when using LLM based software development tools.

LLM Aided Code Review
-------------------------------------------------------------------------------

Another way industry software development teams have been using LLM based tools is in the review process.
Almeida et al. discuss LLM based code review `here <https://www.sciencedirect.com/science/article/pii/S2352711024000487>`_ and conclude that this is a promising application of LLMs in software development.
While the deskilling risk is still present, as code review is a task that requires high skill, using LLMs in addition to humans for code review may present a way to improve overall code quality in academic codebases rather than amplifying any existing flaws in the codebase.
Note however that LLM code review appears to consume many tokens, according to Salim et al. `here <https://arxiv.org/abs/2601.14470>`_, so this may be an expensive process if cost per token continues to rise, especially since research budgets are frequently very constrained.
Token usage is a complex and emerging area of research in these tasks; another perspective on the topic is given by Bai et al. `here <https://arxiv.org/abs/2604.22750>`_.

.. admonition:: Author's Note

   Local or so called 'Small Language Models' (SLM) may provide a way to address this concern, as well as concerns about data privacy and dependence upon large corporations.
   Note, however, that these models have smaller context windows and are therefore less capable than LLMs, as a general rule.

Open Source Policies
-------------------------------------------------------------------------------

Open source software development overlaps with both industry and research software communities.
Several scientific open source software packages have released contribution guidelines for AI and LLM generated content (`NumPy <https://numpy.org/devdocs/dev/ai_policy.html>`_, `matplotlib <https://matplotlib.org/devdocs/devel/contribute.html#generative-ai>`_, `Pandas <https://pandas.pydata.org/docs/dev/development/contributing.html#automated-contributions-policy>`_, and `SciPy <https://scipy.github.io/devdocs/dev/conduct/ai_policy.html>`_ just to name a few from `this list <https://github.com/melissawm/open-source-ai-contribution-policies>`_ by Melissa Weber Mendonça).
A common theme in many of these policies is the need for developers to understand and accept responsibility for the code they submit.
Understanding in code and especially in complex codebases requires, again, time and training, which are points of concern for RSEs.
(While not immediately sanguine to the discussion of the intersection between industry software development best practices and research software engineering, `van der Walt's post on the Scientific Python Blog <https://blog.scientific-python.org/scientific-python/community-considerations-around-ai>`_ highlights many concerns and thoughts relevant to development of research software.)

Summary
-------------------------------------------------------------------------------

This combination of factors emphasizes the need to focus on training and further highlights a vulnerability for research software - high skill is required to appropriately use agentic AI and other LLM based software development tools while ensuring high quality code.
Given the consistent concerns over training and resources for RSEs, achieving the productivity benefits that some industry software development teams have reported while maintaining software quality may prove difficult for RSEs to achieve while using agentic AI and other LLM based software development tools.
Code review is one area that may be less risky for RSEs to incorporate LLM based software development tools.


Research Software Ethics
================================================================================

The challenges faced by the research software development community make it difficult to implement industry software development best practices for agentic AI and other LLM based software development.
However, software development best practices are not the only guidelines for professional research software development.
As academic researchers, RSEs must also follow research integrity standards.

The European Code of Conduct for Research Integrity (available `here <https://zenodo.org/records/12729678>`_) calls out a few key points of note for this discussion.
Firstly, researchers have an obligation to be transparent in their reporting of methods, including the use of AI tools.
Secondly, researchers and institutions should treat software as 'legitimate and citable' research products (similar to the `San Francisco Declaration on Research Assessment <https://sfdora.org/read>`_).
Thirdly, researchers must not plagiarize the work of others.
RSEs must keep these practices in mind while using agentic AI and other LLM based software development tools.

Disclosure
-------------------------------------------------------------------------------

The first point, an obligation to disclose methods, is consistent with many of the policies for AI and LLM generated content from `the list of open source policies <https://github.com/melissawm/open-source-ai-contribution-policies>`_ by Melissa Weber Mendonça.
Not only is disclosure consistent with research ethics, but also LLM based coding tools tend to make different types of errors than human software developers (Cotronen et al. `here <https://arxiv.org/abs/2508.21634>`_, CodeRabbit `here <https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report>`_, and Chong `here <https://c3.unu.edu/blog/strange-errors-and-familiar-flaws-how-ai-and-human-mistakes-compare>`_ discuss different perspectives on this issue).
As a result, disclosure is not only a professional ethical requirement but also allows the developers to better review the generated code and catch the types of errors more commonly found in LLM generated code.

Citations
-------------------------------------------------------------------------------

The second and third points are trickier.
If we want research software to be considered first class artifacts like research papers, then novel algorithms or implementations from other researchers must be cited when used.
Importing external libraries naturally acts as a citation mechanism; however, not all algorithms can be imported in this way, for various reasons.
In such cases, the original researcher should be cited via another mechanism, such as in the project documentation.
Unfortunately, LLMs can generate novel or copyrighted code without attribution, making it difficult to properly attribute the source of the generated content when using LLM based software development tools.
For example, Professor Tim Davis prompted GitHub's Copilot to generate large portions of his own copyrighted code from CSparse without any attribution or the LGPL license `here <https://x.com/DocSparse/status/1581461734665367554>`_.

LLMs can be prompted to generate sources for their content; however, this process is not the same as how humans generate citations.
The target content is prompted and results with citations are generated (potentially with errors) instead of the typical academic process of ingesting the material and then citing the material as you design and create new research content.
Researchers should therefore proceed carefully when using LLMs to generate citations to ensure proper research ethics and processes are respected.

Additionally, a `study by Linardon et al. <https://pmc.ncbi.nlm.nih.gov/articles/PMC12658395>`_ found that GPT-4 fabricated or generated otherwise erroneous citations when prompted to generate 6 literature reviews for medical studies; and that prompt design can mitigate but not eliminate this behavior.
Zhao et al. estimated that at least `146,932 hallucinated citations <https://arxiv.org/abs/2605.07723>`_ were in papers submitted to arXiv in 2025 alone.
Furthermore, LLMs have a tendency to reinforce or exacerbate gender imbalances in citations by underreporting the works of women in generated citations (see discussion by He `here <https://arxiv.org/abs/2508.02740>`_), meaning that references to important contributions may be omitted or misattributed.
Disclosure of usage of LLM based tools does indirectly cite the training data for the specific model, especially if the details of the tools are supplied, but this lacks the specificity expected for citations in research products.

RSEs should carefully consider the scope of prompts to generate code to reduce the risk of generating code containing novel algorithms with inadequate attribution and carefully check all generated citations.
Note however, that curating prompts carefully can only mitigate, not eliminate, concerns around citations.

Summary
-------------------------------------------------------------------------------

Ultimately, the RSE is responsible for meeting the ethical requirement to cite the relevant sources when generating research products.
Contributing code without proper attribution is plagiarism if usage of the LLM based tools are not disclosed, and even if the usage is disclosed it still is a violation of academic integrity to have missing or inaccurate citations.
ArXiv `announced <https://arstechnica.com/science/2026/05/preprint-server-arxiv-will-ban-submitters-of-ai-generated-hallucinations>`_ that papers submitted to the platform containing LLM usage that violates academic integrity standards, such as plagiarism or fabricated citations, will result in a one year ban from using the platform and requiring the researcher to have their future publications undergo peer review before uploading them to arXiv.
RSEs should similarly hold ourselves to high academic research integrity standards regardless of how we are generating the contents of our research products, including our software.


Conclusions
================================================================================

Many software development teams in industry have reported benefits to using agentic AI and other LLM based software development tools.
However, best practices are indicating that using these tools while maintaining high quality code requires a high degree of skill and training, which is a particular weakness of the research software engineering career field.
Furthermore, research ethics require appropriate citations for research artifacts, but LLMs omit, fabricate, or make errors with citations.
According to `Nature <https://www.nature.com/articles/d41586-026-01690-7>`_, in a poll posted on Nature's website, social media, and e-mail newsletter researchers reported being broadly negative towards AI, believing that the risks of these tools outweigh the potential benefits, while also feeling like we would be left behind if we do not use these tools.
In that vein, `Zhang and Lee <https://arxiv.org/abs/2606.03560>`_ describe how social pressures and fears of being left behind or eliminated results in problematic AI usage for undergraduate students, which for researches indicates a potential new pressure to violate research ethics, even if accidentally through careless usage of LLMs.
Our undergraduate and graduate students are feeling stress and anxiety from AI displacement of jobs, according to `Farooqi et al. <https://arxiv.org/abs/2601.10468>`_, and we are not immune to these effects either.
RSEs need to ensure that we are continuing to add value and ensure quality in research software as LLM based options proliferate.

.. admonition:: Author's Note

   I find it personally interesting that the results in the Zhang and Lee paper mirror previous results about problematic social media usage or smart phone addiction.

RSEs need to be cognizant of the risks if they decide to incorporate agentic AI and other LLM based software development tools into their research work, including generating academic software.

.. admonition:: Author's Note

   I see research software development as the process by which RSEs further research by way of software.
   That places the software as secondary to the understanding communicated in the codebase, as with research papers; the logical structure of the code should matter more than the code itself.
   Agentic AI and other LLM based software development tools can generate lines of code faster than we can generate understanding, which offers the enticing trap of creating the appearance of productivity with a large volume of code without generating the actual understanding that is the true goal of the research process.
   This reminds me of Forscher's letter to Science in 1963 (available `here <https://www.rpgroup.caltech.edu/virus_bootcamp/assets/pdfs/339.1.full.pdf>`_).
   I think it would help all of us when deciding if and how to incorporate LLM based tools into our research processes to consider our ultimate goals instead of just the intermediate products which are intended to help us meet those goals.

.. admonition:: Author's Note

   The `Leiden Declaration of Artifical Intelligence and Mathematics <https://leidendeclaration.ai>`_ may also be of note to readers, as it echos many of the themes I captured in this post.


Metadata
================================================================================

Started: 11 Jun 2026

Last edited: 05 Jul 2026


Community Comments
================================================================================

This section contains reactions from community members on the topic of agentic AI and LLM based software development tools for research software development.
