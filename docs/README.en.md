## IRIS: Intelligent Repository Issue Solver

<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/IRIS.png" width="100%">
<br>
<h1 align="center">IRIS</h1>
<h2 align="center">
  ～ Intelligent Repository Issue Solver ～
<br>

<a href="https://github.com/Sunwood-ai-labs/IRIS" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=IRIS&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/IRIS">
<a href="https://github.com/Sunwood-ai-labs/IRIS"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/IRIS/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/IRIS"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/IRIS"></a>
<a href="https://github.com/Sunwood-ai-labs/IRIS"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/IRIS"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/IRIS?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/IRIS?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/IRIS/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>This repository's release notes, README, and commit messages are generated using [claude.ai](https://claude.ai/) and [ChatGPT4](https://chatgpt.com/) in conjunction with [AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), and [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II).

## 🌟 Getting Started

I.R.I.S (Intelligent Repository Issue Solver) is an intelligent assistant designed to dramatically improve GitHub repository issue management. It leverages machine learning and natural language processing to automate issue classification, prioritization, and solution suggestions.

This README provides a detailed explanation and step-by-step guide to help you get started, even if you're a beginner.

## 🚀 Features

- **Automatic Issue Labeling:** As new issues are created, AI analyzes their content and automatically assigns appropriate labels.
- **Issue Analysis with Multiple AI Models:** Utilizes advanced natural language processing models like Google Gemini AI to deeply understand issue content.
- **Automated Processes via GitHub Actions:** Operates 24/7 without human intervention.
- **Customizable Label Management:** Easily define and manage project-specific labels through CSV files.
- **Detailed Comment Generation:** Generates detailed comments that provide deeper insights into issues.
- **Change Suggestions:** Generates specific change proposals based on issues, supporting pull request creation.
- **Automatic Release Note Generation:** Generates release notes automatically using AI when pull requests are merged.
- **README Auto-Update:** Reflects release note content in the README upon new releases.
- **Automatic Release Note Creation with Tagging:** Creates release notes corresponding to tags when they are applied.
- **English README Creation:** Generates an English version of the README whenever the original is updated.

## 📁 Repository Structure

```bash
IRIS/
├─ .github/
│  ├─ scripts/
│  │  ├─ deep_comment.py
│  │  ├─ suggest_changes.py
│  │  ├─ label_adder.py
│  │  └─ generate_github_release_notes.py
│  ├─ workflows/
│  │  ├─ issue-deep-comment.yml
│  │  ├─ issue-review.yml
│  │  └─ generate-release-notes.yml
│  ├─ services/
│  │  └─ github_service.py
│  └─ config.py
├─ docs/
│  └─ .sourcesage_releasenotes.yml
└─ README.md
```

## 🛠️ Installation and Configuration (Beginner-Friendly Step-by-Step Guide)

1. **Clone the Repository:**
   - If you don't have a GitHub account, first [sign up for GitHub](https://github.com/join).
   - Visit the [IRIS repository](https://github.com/Sunwood-ai-labs/IRIS) and click the green "Code" button.
   - Choose "Download ZIP" to download the file and unzip it.

2. **Copy Workflow Files:**
   - Locate all YAML files within the `.github/workflows/` directory of the unzipped folder.
   - Copy these files to the `.github/workflows/` directory of your GitHub repository.
     (Create the `.github/workflows/` directory if it doesn't exist.)

3. **Set up GitHub Secrets:**
   - Go to your GitHub repository page and click the "Settings" tab.
   - From the left-hand menu, select "Secrets and variables" → "Actions."
   - Click the "New repository secret" button and add the following secrets:
     - `GITHUB_TOKEN`: Your GitHub personal access token.
     - `GEMINI_API_KEY`: Your Google AI Studio API key.
     - `YOUR_PERSONAL_ACCESS_TOKEN`: Your GitHub personal access token (requires write access to the repository).
     - `YOUR_PERSONAL_ACCESS_TOKEN_IRIS`: A special personal access token for the IRIS system.
   - If you're unsure how to obtain these keys, refer to the documentation of each service or contact the developers.

4. **Install Dependencies:**
   - Install the dependencies listed in the `requirements.txt` file.
   ```
   pip install -r requirements.txt
   ```

## 🔧 Usage

Once you've configured IRIS, here's how it works:

1. When a new issue is created in your repository, IRIS automatically activates.
2. AI analyzes the content of the issue.
3. Appropriate labels are suggested and automatically applied to the issue.
4. A detailed comment is added to the issue.
5. If necessary, change suggestions are generated.
6. When pull requests are merged, release notes are generated automatically.
7. Upon new releases, the release note content is automatically reflected in the README.

No special operations are required. Simply create new issues, and IRIS will handle the rest automatically.

## 📝 Release Updates

- **[v0.5.4](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.4):** Updated English README, updated version information in SourceSage configuration files, removed unnecessary README descriptions, improved README auto-update functionality, and made several code changes.
- [v0.5.3](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.3): Added new features and improvements, including automatic README updates, release note creation with tagging, and English README creation.
- [v0.5.1](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.1): Improved documentation and structure for an enhanced user experience.
- [v0.5.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.0): Added new features such as automatic release note generation, README auto-update, and header image generation.
- [v0.4.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.4.0): Added automatic release note generation functionality (experimental feature), improvements to the GitHub service.
- [v0.3.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.3.0): Added detailed comment generation and change suggestion features.
- [v0.2.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.2.0): Google Generative AI integration, improved label management system, and enhanced usability.
- [v0.1.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.1.0): Implemented automatic issue labeling functionality.

## 🔄 Workflow

The following diagram illustrates the workflow of IRIS:

```mermaid
%%{init:{'theme':'base','themeVariables':{'primaryColor':'#024959','primaryTextColor':'#F2C335','primaryBorderColor':'#F2AE30','lineColor':'#A1A2A6','secondaryColor':'#593E25','tertiaryColor':'#F2C335','noteTextColor':'#024959','noteBkgColor':'#F2C335','textColor':'#024959','fontSize':'18px'}}}%%

sequenceDiagram
    participant User as 👤 User
    participant GitHub as 🐙 GitHub
    participant IRIS as 🤖 I.R.I.S
    participant AI as 🧠 AI Models
    participant Labels as 📋 Labels

    alt Issue Creation Phase
        User->>GitHub: Creates an issue
        GitHub->>IRIS: Triggers GitHub Action
    end

    alt Issue Analysis Phase
        IRIS->>GitHub: Retrieves issue content
        GitHub-->>IRIS: Issue details
        IRIS->>AI: Requests content analysis
        AI-->>IRIS: Analysis results
    end

    alt Labeling Phase
        IRIS->>Labels: Matches suggested labels
        Labels-->>IRIS: Valid labels
        IRIS->>GitHub: Applies verified labels
    end

    alt Comment Generation Phase
        IRIS->>AI: Requests detailed comment generation
        AI-->>IRIS: Generated detailed comment
        IRIS->>GitHub: Adds detailed comment
    end

    alt Change Suggestion Phase
        IRIS->>AI: Requests change suggestion generation
        AI-->>IRIS: Generated change suggestion
        IRIS->>GitHub: Adds change suggestion
    end

    alt Release Note Generation Phase
        GitHub->>IRIS: Pull request merge notification
        IRIS->>AI: Requests release note generation
        AI-->>IRIS: Generated release notes
        IRIS->>GitHub: Creates release notes
    end

    alt README Update Phase
        GitHub->>IRIS: Release event notification
        IRIS->>AI: Requests README update
        AI-->>IRIS: Updated README content
        IRIS->>GitHub: Updates README
    end

    GitHub-->>User: Sends update notification
```

## 🧪 Development Commands (For Advanced Users)

These commands are intended for those involved in developing IRIS:

Generate commit messages using AIRA:
```bash
aira --mode sourcesage commit  --config=.aira\config.dev.commit.yml --ss-model-name="gemini/gemini-1.5-pro-latest" --llm-output="llm_output.md"
```

Generate release notes using SourceSage:
```bash
sourcesage --ss-mode=DocuMind --yaml-file=docs\.sourcesage_releasenotes.yml
```

## 🤝 Contributions

Contributions to the project are welcome! Here's how you can contribute:

1. Create issues to report improvements or problems.
2. Suggest new features.
3. Submit pull requests to improve the code.

If you're new to contributing, check out the [First Contributions](https://github.com/firstcontributions/first-contributions) guide for help.

## 📄 License

This project is licensed under the [MIT License](LICENSE). Please review the license terms for usage, reproduction, modification, and distribution.

## 🙏 Acknowledgements

- Google - for providing Gemini AI.
- GitHub - for providing actions and a development platform.
- All contributors and users.

## ❓ Help and Support

If you have any questions or need support, please reach out using the following methods:

1. Create a new issue on the [GitHub Issues](https://github.com/Sunwood-ai-labs/IRIS/issues) page.
2. Use the contact form on the [official website](https://hamaruki.com/).
3. Send a direct message on [Twitter](https://x.com/hAru_mAki_ch).

Don't hesitate to contact us, even if you're a beginner. We welcome your feedback!