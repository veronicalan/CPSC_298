# Lecture 7

## Housekeeping
- Week in World of AI
    * [Open AI Dev Announcements](https://youtu.be/i53gpiiDEbU?si=1yQeSBplEXWYDrcV)
    * [Agentic Framework Evolution](https://youtu.be/4akq4SKZxyk?si=2MsZRK7H6z1h3CHa)
    * [Metta Announcements](https://youtu.be/Hh152IbXPus?si=YotVHDzJjDpx_Ygj)
    * [Sam Altman is Evil from Elon](https://youtu.be/JP7QN_KM7nY?si=okPwrSygb814cFXz)
    * [Lex Fridman: Cursor Team Interview](https://youtu.be/oFfVt3S51T4?si=_vCXIMnHn-vc65NP)
    * [Open AI Fundraising]()https://youtu.be/4S-vwzfnEeU?si=CVzBx_q5tyEqEV4J
    * [Realtime API with Voice Coding](https://youtu.be/vN0t-kcPOXo?si=b2DYyf7affrs6bi-)
    * [Bolt.new](https://youtu.be/JnikJf0m5J4?si=Nz_0TjokcIxQptmk)
- Homework and Quizzes Assesment; Half class has not completed mid-term; Still missing 1/3 of homework.
- Canvas Updated once I review your PR (make sure I'm contributor/reviewer)
- Please check updated CSV with your handles
- Poll on Groq Key and Open AI API key usage; Will be assigning keys immediately; Budget set to $5 per person through end of month
- Will start shortening time on quizzes & final
- Committed `sample.aider.conf.yml` to `examples /` in Repo; `git pull upstream master && git push`

## Where Everyone Should Be Revisited:
- Discord Notifications with Webhook (DM me if you need the hook; Look in Discord help channel for Webhooks)
- Upstream forked and Setup on Personal Github accounts; Know Git/hub:
    * `ssh-keygen` & `ssh-add {-l}`
    * `git set upstream <branch>`
    * `git pull upstream master`
    * `git merge`
    * `git push {origin}`
    * `git checkout {-b} <branch>`
    * `ssh -vT git@github.com # check ssh key setup`
    * understand `.gitignore` and `.*` hidden files in project
    * understand `git log` and how to reset out sync repos with the `upstream`
    * if on Mac: `ssh-add --apple-use-keychain  ... && ssh-add --apple-load-keychain` otherwise:
    * `ssh-add -K ~/.ssh/.ssh`
- Pull Requests on Github, forks, and origin/upstreams synchronized.
- Basics of AI coding with V0 and setting up code on local repo
- Knowledge of TypeScript ecosystem with `npx`, `npm`, and NodeJS (ask AI if uncertain)
- AI Tooling: V0, Replit, Chat.dev, Copilot, Cursor, & Concepts:
    * Large Language Models (LLMs)
    * Feed forward networks (& ANNs)
    * Context Windows
    * Retrieval Augmented Generation (RAG)
    * Chain & Tree of Thought (CoT/ToT)
    * Self Taught Reasoning (STaR)
    * Tokenization and Transformer Architectures as well as Next Token Prediction
    * Mixture of Experts (MoE)
    * Agentic Approaches
    * Benchmarking, Weigths/Biases (Parameters) & Open Source Relevance (open weights, data, and models)
- API Keys setup & sample `.aider.conf.yml` in proper subdirectory
- Have me (jeffrey-l-turner) as reviewer/collaborator on Pull Requests (note Canvas will be graded once assignment complete)
- Make Sure you're information is accurate on CSV posted in Discord
- Signup for [Pythathagora](https://www.pythagora.ai) - no luck getting access so far; Recommendation: use Cursor with Pythagora
- Understand basics of complexity theory and non-deterministic algos

## A visual for Coding Assistance systems revisited
- Models & Coding Assistance
- Context Windows, Size & Next Token Prediction
- Increase Computing and Storage to Scale
- Star Trek Computer Analogy (circa 2265)

## Prompts as Programs
- Download Cursor (or VS Code)
- Ensure LLM has been setup [see: LLM installation](./lecture05.md)
- XML Structures
- Will LLM + provided OpenAI keys for homework
- Will look at structure of your prompts; Bonus for figuring out how to use JSON schema
- Assignment: [LLM](https://github.com/simonw/llm): Install and setup XML as prompts to create a automated `git` commit:
    * Replace LLM command with `git-llm` bash/zsh alias (or script)
    * Place alias or script and XML files in `assignments/git-llm/` subdirectory
    * Create new branch and put PR with me as reviwer
    * Should not take more than an hour
    * helpful `llm | LLM` commands: `llm --help`, `llm templates`, `llm templates path`, `llm --save summarize` / e.g. `llm --system 'Create an automated git commit command' --model gpt-4 --save summarize`

## References:
- [Prompts as Programs](https://youtu.be/IQI5BZlVI3Y?si=FuNUtqfFVVV_BZ6y)

## Resources:
- Channels I Follow for this Class: [Wes Roth](https://www.youtube.com/@WesRoth), [Matthew Berman](https://www.youtube.com/@matthew_berman), [David Shapiro](https://www.youtube.com/@DaveShap/videos), [Indy Dev Dan](https://www.youtube.com/@indydevdan), [Greg Isenberg](https://www.youtube.com/@GregIsenberg), [3 Blue 1 Brown](https://www.youtube.com/@3blue1brown), [AI Explained](https://www.youtube.com/@3blue1brown)
- Tools: [Aider](https://aider.chat/), [LLM](https://github.com/simonw/llm), & [uv](https://github.com/astral-sh/uv) [Data Centric](https://youtube.com/@data-centric?si=SjrEhrokPgsDoeYF)
- [Groq key](https://console.groq.com/keys)
- [Open AI Key Management](https://platform.openai.com/)
