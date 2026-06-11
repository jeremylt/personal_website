Agentic AI Usage for RSE
********************************************************************************

Research Software Engineers (RSE) combine the expertise of professional software development with domain specific skills for academic research.
Several groups and professional declarations, such as the [Journal of Open Source Software](https://joss.theoj.org) and the [San Francisco Declaration on Research Assessment](https://sfdora.org/read), have advocated for treating research software as a first class artifact, on par with peer-reviewed papers, especially for the purposes of career assessment and promotions for RSE.
In order for RSE to enrich scientific research, we need to adhere to both software development best practices and professional research ethics.

Large Language Model (LLM) based development practices, including agentic AI (Happy Bhati provides a summary [here](https://arxiv.org/abs/2604.26275)), are changing software development workflows for many industry software engineers.
Best practices and areas of concern are solidifying on many industry software development teams; however these practices and concerns do not perfectly map to research software development due to both the differences between industry and academic software development and the the unique concerns of professional research ethics in the specific context of software development.

In this article, we will discuss the ways in which developing LLM based best practices for industry software development do and do not map onto research software development.
Also, we will discuss the specific concerns that professional research ethics bring to research software development with agentic AI and other LLM based software development tools.

Author's Note: In this article, I am specifically focused on how emerging industry software development practices intersect with professional research standards.
There is an important and interesting discussion to be had about the ethics of the LLM industry and what options may exist for more ethical LLM based software development tools; however, there is not adequate space to have both discussions in this article.
Both sets of concerns, practical and ethical, need to be addressed for agentic AI and other LLM based software development tools to be incorporated into ethical research practices.


Industry Best Practices
================================================================================

The response to so called agentic AI in industry software development teams has been varied.
In this section, we will identify some common trends and best practices that are emerging and compare those against the known differences between academic and industry software development.

Author's Note: It has proven somewhat difficult to find more neutral or pragmatic academic papers discussing agentic AI development practices.
This may be due to the amount of research that is funded by industry on this topic (MIT's Sloan School discusses this [here](https://mitsloan.mit.edu/ideas-made-to-matter/study-industry-now-dominates-ai-research) and MIT's Initiative on the Digital Economy [here](https://ide.mit.edu/wp-content/uploads/2023/03/0303PolicyForum_Ai_FF-2.pdf)) and the profit motives therein.
This could also be due towards a broader trend in scientific research articles towards positive language over the last 25 years (Yuan and Yao discuss this [here](https://pmc.ncbi.nlm.nih.gov/articles/PMC9526210/pdf/11192_2022_Article_4515.pdf)).
Or it could be due to my personal search process only producing positive results, or perhaps due to other contributing factors.
In any case, I have included written accounts from senior software developers in industry in this section to provide a more pragmatic assessment of current best practices and concerns in usage.

Adam Tornhill provides quality focused best practices [here](https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality).
A common theme throughout his article is that agentic AI relies upon healthy, high quality code and testing to control risk.
Specifically, he notes that AI models have no understanding of maintainability or charge risk inside of a codebase and can easily generate 'unhealthy' code (see discussion [here](https://codescene.io/docs/guides/technical/code-health.html#code-health-identifies-factors-known-to-impact-maintenance-costs-and-delivery-risks)) and perform better in codebase with 'healthy' code (see discussion [here](https://arxiv.org/abs/2601.02200)).
Largely, this means that a codebase that follows best practices for human code development is a prerequisite for successful development with agentic AI.
Tornhill notes that disciplined engineering practices with planning, review, and testing are required.

However, RSEs frequently encounter difficulties meeting standard industry best practices for software development (see discussion by Anzt et al. [here](https://arxiv.org/abs/2005.01469) for discussion of specific challenges faced in Germany and by Carver at al. [here](https://arxiv.org/abs/2103.01880) for similar challenges in the United States).
In particular, training and resources particularly are a common challenge for RSEs.
This is exacerbated by unstable or unclear career trajectories that make it difficult for research teams to identify, train, and retain individuals with the appropriate interests and skills for research software development.
Arvanitou et al. summarized these concerns nicely [here](arxiv.org/abs/2010.09pdf914) and showed that adherence to best practices focused on performance, maintainability, and development productivity improve quality.
The challenges around training and resources unfortunately make it difficult to deliver the prerequisite quality required to implement Tornhill's suggestions.

Of particular interest, given the difficulties with research software engineering training, is the risk of deskilling (discussed by Gerlich [here](https://www.mdpi.com/2075-4698/15/1/6)) or degraded skill formation (discussed by Shen and Tamkin [here](https://arxiv.org/abs/2601.20245)).
If RSEs frequently do not have adequate training in software development and quality usage of agentic AI or other LLM based software development tools relies upon disciplined engineering practices, that places research software development at particular risk for low quality software being generated by these tools.

Additionally, Stetskov notes the increased code review time required with heavy use of LLM based coding tools [here](https://techtrenches.dev/p/the-human-cost-of-10x-how-ai-is-physically) and the fact that agentic AI tools do not always follow instructions (as discussed [here](https://techtrenches.dev/p/your-claudemd-is-a-wish-list-not)).
Critically, Stetskov notes the importance of senior developer skill in catching errors in generated code, which is problematic when considering the issues around training and the risk of deskilling for RSEs.
Additionally, time is consistently a constrained resource for research teams, but high quality code review is a time consuming activity.

Open source software development overlaps with both industry and research software communities.
Several scientific open source software packages have released contribution guidelines for AI and LLM generated content ([NumPy](https://numpy.org/devdocs/dev/ai_policy.html), [matplotlib](https://matplotlib.org/devdocs/devel/contribute.html#generative-ai), [Pandas](https://pandas.pydata.org/docs/dev/development/contributing.html#automated-contributions-policy), and [SciPy](https://scipy.github.io/devdocs/dev/conduct/ai_policy.html) just to name a few from [this list](https://github.com/melissawm/open-source-ai-contribution-policies) by Melissa Weber Mendonça).
A common theme in many of these policies is the need for developers to understand and accept responsibility for the code they submit.
Understanding requires, again, time and training, which are points of concern for RSEs.
(While not immediately sanguine to the discussion of the intersection between industry software development best practices and research software engineering, [van der Walt's post on the Scientific Python Blog](https://blog.scientific-python.org/scientific-python/community-considerations-around-ai/) highlights many concerns and thoughts relevant to development of research software.)

This combination of factors emphasizes the need to focus on training and further highlights a vulnerability for research software - high skill is required to appropriately use agentic AI and other LLM based software development tools.
Given the consistent concerns over training and resources for RSEs, achieving the productivity benefits that some industry software development teams have reported while maintaining software quality may prove difficult for RSEs to achieve while using agentic AI and other LLM based software development tools.


Research Software Ethics
================================================================================

The challenges faced by the research software development community make it difficult to implement industry software development best practices for agentic AI and other LLM based software development.
However, software development best practices are not the only guidelines for professional research software development.
As academic researchers, RSEs must also follow research integrity standards.

The European Code of Conduct for Research Integrity (available [here](https://zenodo.org/records/12729678)) calls out a few key points of note for this discussion.
Firstly, researchers have an obligation to be transparent in their reporting of methods, including the use of AI tools.
Secondly, researchers and institutions should treat software as 'legitimate and citable' research products (similar to the [San Francisco Declaration on Research Assessment](https://sfdora.org/read)).
Thirdly, researchers must not plagiarize the work of others.
RSE must keep these practices in mind while using agentic AI and other LLM based software development tools.

The first point, an obligation to disclose methods, is consistent with many of the policies for AI and LLM generated content from [the list of open source policies](https://github.com/melissawm/open-source-ai-contribution-policies) by Melissa Weber Mendonça.
Not only is disclosure consistent with research ethics, but also LLM based coding tools tend to make different types of errors than human software developers (Cotronen et al. [here](https://arxiv.org/abs/2508.21634), CodeRabbit [here](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report), and Chong [here](https://c3.unu.edu/blog/strange-errors-and-familiar-flaws-how-ai-and-human-mistakes-compare) discuss different perspectives on this issue).
As a result, disclosure allows the developers to better review the generated code and catch the types of errors more commonly found in LLM generated code.

The second and third points are trickier.
If we want research software to be considered a first class artifact like research papers, then novel algorithms or implementations from other researchers must be cited when used.
Importing external libraries naturally acts as a citation mechanism; however, not all algorithms can be imported in this way, for various reasons.
In such cases, the original researcher should be cited via another mechanism, such as in the project documentation.
Unfortunately, LLMs can generate novel or copyrighted code without attribution, making it difficult to properly attribute the source of the generated content when using LLM based software development tools.

Prof Tim Davis prompted GitHub's Copilot to generate large portions of his own copyrighted code from CSparse without any attribution or the LGPL license [here](https://x.com/DocSparse/status/1581461734665367554).
LLMs can be prompted to generate sources for their content; however, this process is not the same as how humans generate citations.
The target content is prompted and results with citations are generated (potentially with errors) instead of the typical academic process of ingesting the material and then citing the material as you design and create new research content.
Additionally, a [study by Linardon et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12658395) found that GPT-4 fabricated or generated otherwise erroneous citations when prompted to generate 6 literature reviews for medical studies; and that prompt design can mitigate but not eliminate this behavior.
Zhao et al. estimated that at least [146,932 hallucinated citations](https://arxiv.org/abs/2605.07723) were in papers submitted to arXiv in 2025 alone.
Disclosure of usage of LLM based tools does indirectly cite the training data for the specific model, especially if the details of the tools are supplied, but this lacks the specificity expected for citations in research products.
RSEs should carefully consider the scope of prompts to generate code to reduce this risk and carefully check all generated citations.

Ultimately, the RSE is responsible for meeting the ethical requirement to cite the relevant sources when generating research products.
Contributing code without proper attribution is plagiarism if usage of the LLM based tools are not disclosed, and even if the usage is disclosed it still is a violation of academic integrity to include no or inaccurate citations.
ArXiv [announced](https://arstechnica.com/science/2026/05/preprint-server-arxiv-will-ban-submitters-of-ai-generated-hallucinations) that papers submitted to the platform containing LLM usage that violates academic integrity standards, such as plagiarism or fabricated citations, will result in a one year ban from using the platform and requiring the researcher to have their future publications undergo peer review before uploading them to arXiv.
RSEs should similarly hold ourselves to high academic research integrity standards regardless of how we are generating the contents of our research products, including our software.


Conclusions
================================================================================

Many software development teams in industry have reported benefits to using agentic AI and other LLM based software development tools.
However, best practices are indicating that using these tools while maintaining high quality code requires a high degree of skill and training, which is a particular weakness of the research software engineering career field.
Furthermore, research ethics require appropriate citations for research artifacts, but LLMs omit, fabricate, or make errors with citations.
RSEs need to be cognizant of these risks if they decide to incorporate agentic AI and other LLM based software development tools into their research work, including generating academic software.


Community Comments
================================================================================

This section contains reactions from community members on the topic of agentic AI and LLM based software development tools for research software development.
