LLM Ethical Considerations for RSE
********************************************************************************

In `my post <https://jeremylt.org/blog/research-software/ai-for-rse>`_ I discussed using AI/LLM based software development tools for Research Software Engineers strictly from the lens of considering skills, risks, and research ethics.
I tried to focus on a purely pragmatic perspective that considered if or how it could be possible for RSEs to see the benefits that some industry software development teams have experienced.

However, these are not the only considerations present.
In this post I want to gather various perspectives on the ethical considerations around the LLMs themselves, including training and environmental impact concerns.


Data Center Impacts
================================================================================

Perhaps one of the most publicized impacts of LLMs is the environmental impacts of data centers.
Two of the common factors are water and electricity usage.
While this is a rather limited lens to capture the impacts of LLM usage, I am including this here because it has a tangible direct impact upon local communities.
Even if these impacts were successfully mitigated, other ethical considerations presented in this article would also be present.

The `Data Centers and the Climate Landscape: An Actionable Resource for US Mayors <https://greatercle.com/clientuploads/Data_Centers_and_the_Climate_Landscape_An_Actionable_Resource_for_US_Mayors.pdf?_t=1782241863>`_ report states that two thirds of the data centers built in the US since 2022 were constructed in water stressed areas and 97 percent of data centers get their operating water from municipal water systems.
Large data centers can consume water approximately equivalent to 10,000 to 50,000 people while smaller centers can consume approximately 2,000 people's water, or less.

The `2025 Update <https://www.osti.gov/biblio/3374245>`_ to the `2024 Data Center Energy Usage Report <https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report>`_ from Lawrence Berkeley National Laboratory reports that data centers could account for between 6.7 and 12.0 percent of total US electricity usage by 2028.
Data centers represented 4.4 percent of US electricity usage in 2023 and 4.7 percent in 2024.
`Various reporting <https://www.reuters.com/sustainability/boards-policy-regulation/americas-largest-power-grid-is-struggling-meet-demand-ai-2025-07-09>`_ has indicated that data center growth is one of the factor leading to increasing strain on the US power grid.
This also coincides with `increasing strain from extreme weather due to climate change <https://www.reuters.com/business/energy/scorching-heat-forecast-threatens-demand-records-us-electric-grid-2026-06-30>`_.
Considering how much critical infrastructure relies upon electricity, this strain from data centers represents a real safety threat to people who live in locations where these centers are being built.

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


Metadata
================================================================================

Started: 10 Aug 2026

Last edited: 10 Aug 2026
