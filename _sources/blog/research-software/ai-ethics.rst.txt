LLM Ethical Considerations for RSE
********************************************************************************

In `my other post <https://jeremylt.org/blog/research-software/ai-for-rse>`_ I discussed using AI/LLM based software development tools for Research Software Engineers strictly from the lens of considering skills, risks, and research ethics.
I tried to focus on a purely pragmatic perspective that considered if or how it could be possible for RSEs to see the benefits that some industry software development teams have experienced.

However, these are not the only considerations present.
In this post I want to gather various perspectives on the ethical considerations around the LLMs themselves, including training and environmental impact concerns.


Data Center Impacts
================================================================================

Perhaps one of the most publicized impacts of LLMs is the environmental impacts of data centers.
Two of the common factors are water and electricity usage.
While this is a rather limited lens to capture the impacts of LLM usage, I am including this here because it has a tangible, direct impact upon local communities.
Even if these impacts were successfully mitigated, other ethical considerations presented in this article would also be present.

The `Data Centers and the Climate Landscape: An Actionable Resource for US Mayors <https://greatercle.com/clientuploads/Data_Centers_and_the_Climate_Landscape_An_Actionable_Resource_for_US_Mayors.pdf?_t=1782241863>`_ report states that two thirds of the data centers built in the US since 2022 were constructed in water stressed areas and 97 percent of data centers get their operating water from municipal water systems.
Large data centers can consume water approximately equivalent to 10,000 to 50,000 people while smaller centers can consume approximately 2,000 people's water, or less.
According to `Jegham et. al. <https://arxiv.org/abs/2505.09598>`_ a 0.42  watt-hour short query, scaled to 700 million queries per day would represent the freshwater needs of approximately 1.2 million people, as well as representing the electricity usage of 35,000 US homes and carbon emissions that would require a forest the size of Chicago to offset.

The `2025 Update <https://www.osti.gov/biblio/3374245>`_ to the `2024 Data Center Energy Usage Report <https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report>`_ from Lawrence Berkeley National Laboratory reports that data centers could account for between 6.7 and 12.0 percent of total US electricity usage by 2028.
Data centers represented 4.4 percent of US electricity usage in 2023 and 4.7 percent in 2024.
`Various reporting <https://www.reuters.com/sustainability/boards-policy-regulation/americas-largest-power-grid-is-struggling-meet-demand-ai-2025-07-09>`_ has indicated that data center growth is one of the factor leading to increasing strain on the US power grid.
This also coincides with `increasing strain from extreme weather due to climate change <https://www.reuters.com/business/energy/scorching-heat-forecast-threatens-demand-records-us-electric-grid-2026-06-30>`_.
Additionally, `Li et. al. <https://arxiv.org/abs/2409.11416>`_ noted that the characteristics of the load LLM data centers place on the power grid pose unique threats to grid reliability and resilience.
Considering how much critical infrastructure relies upon electricity, this strain from data centers represents a real safety threat to people who live in locations where these centers are being built.
It remains difficult to know the exact impact due to the resource usage data remaining secret, but the environmental impact of LLM infrastructure is significant by all estimates I can find.

This strain is not spread over all data centers equally.
The `Data Centers and the Climate Landscape: An Actionable Resource for US Mayors <https://greatercle.com/clientuploads/Data_Centers_and_the_Climate_Landscape_An_Actionable_Resource_for_US_Mayors.pdf?_t=1782241863>`_ report states that facilities involved with model training and hyperscale facilities represent the largest impact in terms of power and water consumption.
While these concerns are not the limits of impacts of LLMs on people, it seems clear that these data centers do indeed result in less water and power being available for people to use.
Participating in the demand for LLMs would thus be participating in this reduced access to water and power.
While it is true that interacting with internet based technologies does have an impact and require the usage of data centers, LLM usage itself has a particularly high usage, with queries submitted to LLMs requiring `10 to 30 times more energy than traditional internet search engines require <https://www.scientificamerican.com/article/what-do-googles-ai-answers-cost-the-environment>`_.
These and other impacts seem to be especially concentrated on `marginalized and minority communities in the US <https://thenarrativematters.com/data-centers-impact-on-low-income-marginalized-communities-balancing-economic-opportunity-and-community-burden>`_.
Reinforcing existing systematic biases and issues is a theme that will come up in other contexts in this article.


Model Training
================================================================================

There are a few components of model training that feel particularly noteworthy to me.
First, the matter of consent when gathering training data matters greatly to me.
Secondly, the disproportionate resource consumption when training these models, even if they are run locally, is a concern.
Additionally, the training process's disassociation of the data from attribution and licensing considerations is problematic.

LLM performance scales with training dataset size and many modern LLMs are trained on hundreds of billions or trillions of tokens, according to a `survey by Zhao et. al. <https://arxiv.org/abs/2303.18223>`_.
This is a massive amount of data, collected from web pages, books, academic publications, Wikipedia, open source software repositories, and additional sources.
Many of these sources did not consent to their data being used to train LLMs, leading to lawsuits such as `The New York Times suing OpenAI and Microsoft <https://harvardlawreview.org/blog/2024/04/nyt-v-openai-the-timess-about-face>`_, `a 1.5 billion dollar settlement between authors and Anthropic <https://www.anthropiccopyrightsettlement.com/faq>`_, `Elseiver and other companies suing Meta <https://www.nature.com/articles/d41586-026-01481-0>`_, among other examples.
The collection of this data without permission and in some cases against the wishes of the authors and creators violates basic ethics around consent.
US courts appear to agree with LLM companies, at least in part and in some cases, that `lawfully acquired training data may be fair use <https://www.reuters.com/legal/legalindustry/copyright-law-2025-courts-begin-draw-lines-around-ai-training-piracy-market-harm--pracin-2026-03-16>`_, though many cases are still ongoing and different countries have different legal frameworks.
In any case, while LLM training data collection practices may be legal, that still does not address the ethical concern of using the data without the permission and sometimes against the expressed wishes of the originators.
Research guidelines, such as the `The European Code of Conduct for Research Integrity <https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/guidance/european-code-of-conduct-for-research-integrity_horizon_en.pdf>`_ set the expectation that research subjects and materials should be treated with respect and consistent with ethical guidelines.
For researchers using LLMs during their research, this distinction between legal and ethical data collection is important.

There have been efforts to ensure ethical collection of training data, such as the `Common Corpus project <https://proceedings.iclr.cc/paper_files/paper/2026/file/2b5c5689fae6fa9a4883e73e511d52c8-Paper-Conference.pdf>`_.
This dataset consists of approximately 2 billion tokens, which is in line with the size of data sets for several of the recent larger models.
The data set is filtered by permissive licenses, and personally identifiable information was removed.
Furthermore, the Common Corpus team attempted to filter out data that was deemed toxic by a specifically trained multilingual small model for this purpose.
These efforts address the ethics of data collection, or at least attempts to, but does not address the questions of resources consumed training the model or attribution concerns.

The second point I will not spend long on here except to note that even with ethically sourced training data, the cost of training these LLMs noted in the previous section still remains.
Using these models directly encourages the training costs of new models as various corporations attempt to secure additional users in their efforts to become profitable.

As I noted in `my other post <https://jeremylt.org/blog/research-software/ai-for-rse>`_, the third point is a particular concern for academics, including Research Software Engineers.
From a purely pragmatic point of view, it is not possible to identify which of the billions of tokens in the training data were the most significant in generating a specific output from the model.
That's not how the training works, at a fundamental level.
Disclosure of usage of LLM based tools does indirectly cite the training data for the specific model, if the details of the tools are supplied, but this lacks the specificity expected for citations.

LLMs can be prompted to generate sources for their content; however, this process is not the same as traditional methods of identify the source of information and attributing that information the the source.
A `study by Linardon et al. <https://pmc.ncbi.nlm.nih.gov/articles/PMC12658395>`_ found that GPT-4 fabricated or generated otherwise erroneous citations when prompted to generate 6 literature reviews for medical studies; and that prompt design can mitigate but not eliminate this behavior.
Zhao et al. estimated that at least `146,932 hallucinated citations <https://arxiv.org/abs/2605.07723>`_ were in papers submitted to arXiv in 2025 alone.
The true sources of the information that correspond to the LLM generated output are not reliably recoverable from the models themselves.

This means that the training data is divorced from its original context, which complicates or makes impossible the task of attribution and licensing compatibility verification.
This is especially problematic when the training data was not ethically sourced, as the original authors may have added licensing stipulations that are incompatible with the intended usage of LLM output.
Data is collected without permission, the model is trained in a resource intensive fashion, and then the end user of the model cannot easily attribute the source data that was most relevant to the generated output or even ensure that their usage aligns with any stipulations on the original data, such as licensing agreements.


Bias and Inequity
================================================================================

LLMs can reinforce existing systemic bias and inequity.
In this section, I discuss various research about this pattern.

With respect to generated output, LLMs have a measurable impact upon the generated output when compared to human written content, as discussed by Abdulhai et. al. `here <https://arxiv.org/abs/2603.18161>`_.
Of particular note is the tendency, discussed by Agarwal et. al. `here <https://arxiv.org/abs/2409.11360>`_, for LLMs to homogenize output towards Western cultural norms, erasing cultural expression.
Furthermore, this tendency means that non-Western users have to put in additional effort to achieve perceived productivity gains reported by Western users.
Multiple studies have explored how LLMs flatten out perspectives that are not dominant in the training data, which tends to be dominated by Western and often US American web content.

Meincke et. al. `discuss <https://www.nature.com/articles/s41562-025-02173-x.pdf>`_ how ChatGPT reduces idea diversity during brainstorming.
Producing outputs conforming to a smaller set of norms and producing a reduced diversity of ideas go hand in hand.
Anecdotally, one of the benefits of diversity that was discussed in the US military in 2005-2016, when I was in the US Air Force, was the idea that a diversity of perspectives would lead to better and more varied problem solving.

Related to the previous section, LLMs have a tendency to reinforce or exacerbate gender imbalances in citations by underreporting the works of women in generated citations (see discussion by He `here <https://arxiv.org/abs/2508.02740>`_), meaning that references to important contributions may be omitted or misattributed.
Taken together, these studies demonstrate a tendency of LLMs to erase perspectives and cultures that are not strongly represented in their training data, and those perspectives and cultures often correspond to groups that have been traditionally underrepresented in bodies of work prior to the widespread usage of LLMs, which makes sense considering the training process for LLMs.


Metadata
================================================================================

Started: 10 Aug 2026

Last edited: 03 Sep 2026
