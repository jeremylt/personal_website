Local LLMs for Development
********************************************************************************

I am experimenting with local instances of Large Language Models (LLMs) for software development.
While this experimentation continues, I will update this post with further information.


Reasoning
================================================================================

Local LLMs, at least in theory, may offer advantages over using APIs to access LLMs operated by large corporations in commercial data centers.

- Local hardware can use less water and power than large data centers

- Data stays on the developer's device, addressing privacy concerns

- With open source models, developers are not dependent upon large corporations who may have conflicting values with the developer

Note however that concerns around skill formation, de-skilling, and plagiarism persist with local LLMs.


Implementation
================================================================================

I have selected `VS Code <https://code.visualstudio.com>`_ as my IDE, as it has support for various extensions that support different levels of LLM integration into software development.

.. admonition:: Author's Note

   Note that VS Code is `owned by Microsoft <https://en.wikipedia.org/wiki/Visual_Studio_Code>`_, there is both a proprietary and open source version of the code.
   The open source version of the code is `under the MIT license <https://github.com/microsoft/vscode>`_.


Specifically, I am using the `Continue <https://www.continue.dev>`_ extension.

.. admonition:: Author's Note

   Note that while Continue is an open source project, the company Continue has been `purchased by Cursor <https://en.wikipedia.org/wiki/Cursor_(company)>`_.
   Cursor is itself being `purchased by SpaceX as part of its xAI <https://en.wikipedia.org/wiki/SpaceXAI>`_ subsidiary.
   While the extension will remain open source (at this time), it is worth monitoring this development for developers who wish to avoid directly relying upon large US software corporations.
   The Cursor extension is `under the Apache 2.0 license <https://github.com/continuedev/continue>`_.

I am using `Ollama <https://ollama.com>`_ to operate the open LLM models.

.. admonition:: Author's Note

   Ollama is an open source software `under the MIT license <https://github.com/ollama/ollama>`_.

Finally, I am currently using the `Qwen3 <https://en.wikipedia.org/wiki/Qwen>`_ model.

.. admonition:: Author's Note

   Qwen3 is an open source model `under the Apache 2.0 license <https://github.com/QwenLM/Qwen3>`_.

The relevant portion of the Continue configuration file is given below:

.. code-block:: yaml

   - name: Qwen3 8B
     provider: ollama
     model: qwen3:8b
     apiBase: http://localhost:11434
     contextLength: 9742
     capabilities:
       - tool_use
     defaultCompletionOptions:
       contextLength: 9742
       maxTokens: 2048
     roles:
       - chat
       - autocomplete
       - edit
       - apply
       - summarize

Observations
================================================================================

Experimentation to select the correct model and context length is important.
I am working with a development machine that has a GPU with only 6GB of VRAM.
This limits the models and context length that I can select.

Specifically, I am currently experimenting with using Qwen3 8B via Ollama with a `contextLength` of `10**13.25≈9742` tokens and a `maxTokens` of `2048`.
While these settings limit the capability of the model to ingest large codebases, it keeps the performance relatively responsive while allowing me to generate smaller snippets of code.
I do not see this limitation as particularly problematic, as this is consistent with my general recommendation to RSEs to only generate small, focused amounts of code at once and maintain control over the overall design and review while creating research software.


Metadata
================================================================================

Started: 10 Jul 2026

Last edited: 10 Jul 2026
