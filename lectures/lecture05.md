# Lecture 5

## Housekeeping
- Week in World of AI
    * Open AI Strawberry (o1) as STaR confirmations
    * [Claude Dev (extension to VS Code)](https://github.com/saoudrizwan/claude-dev)
    * [Updated Coding Benchmarks: Open AI, Anthropic, Google](https://www.youtube.com/watch?v=cESc7v1G1uA) & [Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)
    * [New Microsoft Models](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcs8uhnA2CPUQP9EpzFBvjCNOmTg62aYu8PKxQVL8Z3Gf4Rv5LaOdHGBXEIupZXdYu9-eIhgW5mBC5j4ZUYp14zxBBX61VObQpC1x7_cyG_5PBbSZuYThwRolLJBWWwZlAB_MD8-7iTDS4OpXCEvgOI3zdV?key=EeRJUTRsFriuBsQRcjhLjw)
    * Meta Conference This week + open source developments
- Homework and Quizzes Assesment; Docking 10% minimum for missed deadlines; Due dates will now on late Wednesday (after class) & Docked Thursday
- Walk through Github Pull Request
- A word on System and Language Ecosystem Package Management (`npm`, `brew`, `choco install`, `pip`, `uv`, etc.)
- Re-orienting class: TypeScript + Python language ecosystems
- Get Groq key: [https://console.groq.com/keys](https://console.groq.com/keys)

## Where Everyone Should Be:
- Discord Notifications with Webhook (DM me if you need the hook)
- Upstream forked and Setup on Personal Github accounts; Know Git/hub:
    * `ssh-keygen` & `ssh-add {-l}`
    * `git pull`
    * `git push`
    * `git checkout {-b} <branch>`
    * `git set upstream <branch>`
    * `ssh -vT git@github.com # check ssh key setup`
- Pull Requests on Github, forks, and origin/upstreams.
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
- Mindset: Operating at Higher Levels of Abstraction

- Assignment 1 Pull Request on Github account with changes in assignment directory
    * ` npx shadcn@latest add "https://v0.dev/chat/...`

## Artificial Neural Networks:
- MoE & Encoding Re-Review
<div align="center">
  <img src="./MoE.png" width="600" height="365" />
</div>
<div align="center">
  <img src="./Encoder_router_MoE.png" width="600" height="365" />
</div>

## Homework
- Currently free / See above to get Groq key; [Open AI Compatibility](https://groq.com/groqcloud/)
- Fifth Week Assignment (#3)
    * `git pull upstream master; git push # on your forked master branch`
    * Make jeffrey-l-turner a collaborator on your fork & wait for acceptance; Place jeffrey-l-turner as reviewer on pull request
    * Copy and modify [`assignments/sample.aider.conf.yml`](https://github.com/paul-gauthier/aider/blob/main/aider/website/assets/sample.aider.conf.yml) to existing `assignments/`directory; Place Groq API key and model in this file so that Aider works properly
    * use Aider and/or LLM with your assignment to enhance code with UI; Make sure all code is committed from V0 in `assignments/` directory
    * Now using [`uv`](https://github.com/astral-sh/uv) to install aider and other Python tooling ([Windows:Chocalatey](https://chocolatey.org/install); Mac: [brew](https://brew.sh/) ; Linux: use `curl`)
- Make sure to enhance .md file with your screenshot and any notes
- Sign up for OpenRouter; Install aider with uv (`uv venv; uv pip install aider-chat`); Install [`llm`](https://github.com/simonw/llm) (e.g. `uv pip install llm` or `brew install llm`)
- Again, make sure jeffrey-l-turner is set to reviewer and changes have been committed into PR

## References:
- [Evidence of Strawberry (o1) being STaR]()
- [Using "close to the metal" AI coding synthesis (Aider + Cursor + Bun)](https://youtu.be/QlUt06XLbJE?si=NnwOeyl4BVPo8JRW)
- [Contextual RAG](https://youtu.be/42Da0O9zkhc?si=CyhxuoI44UwpNFoA)
- [Open AI Hates Transparency](https://youtu.be/gC9VW23fk9g?si=nXIe97yhVWD6uc7z)
- [The Intelligence Age](https://youtu.be/evDI1a6E8JY?si=pvjuI5rJmnRfJUBj)
- [ClaudDev](https://youtu.be/Xp8M9kmnV34?si=oW3iHIoibwZ9Hq-S)
- [Nuclear Power and new Microsoft AI Models](https://www.youtube.com/watch?v=T301T6H9l34)

## Resources:
- Channels I Follow for this Class: [Wes Roth](https://www.youtube.com/@WesRoth), [Matthew Berman](https://www.youtube.com/@matthew_berman), [David Shapiro](https://www.youtube.com/@DaveShap/videos), [Indy Dev Dan](https://www.youtube.com/@indydevdan), [Greg Isenberg](https://www.youtube.com/@GregIsenberg), [3 Blue 1 Brown](https://www.youtube.com/@3blue1brown), [AI Explained](https://www.youtube.com/@3blue1brown)
- Tools: [Aider](https://aider.chat/), [LLM](https://github.com/simonw/llm), & [uv](https://github.com/astral-sh/uv)
