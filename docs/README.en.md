## 🚀 IRIS

## 📋 Overview

IRIS is an intelligent assistant that automates issue management in GitHub repositories. Utilizing machine learning and natural language processing, it automatically classifies issues, prioritizes them, and proposes solutions.

## ✨ Key Features

- Automatic issue labeling
- Issue analysis using multiple AI models
- Automated processes via GitHub Actions
- Customizable label management
- Detailed comment generation
- Change suggestions
- Automatic release notes generation

## 🆕 Latest Updates

- **v0.5.0:** Added new features such as automatic release notes generation, automatic README updates, and header image generation.

## 🛠️ Installation Instructions

1. **Clone the repository:**
   - Clone the GitHub repository.
   ```bash
   git clone https://github.com/Sunwood-ai-labs/IRIS.git
   ```
2. **Copy workflow files:**
   - Copy all YAML files located in the `.github/workflows/` directory of the repository to the `.github/workflows/` directory of your GitHub repository.
3. **Set up GitHub secrets:**
   - In your GitHub repository, navigate to the "Settings" tab, select "Secrets and variables" -> "Actions", and add the following secrets:
     - `GITHUB_TOKEN`: Your GitHub personal access token
     - `GEMINI_API_KEY`: Your Google AI Studio API key
     - `YOUR_PERSONAL_ACCESS_TOKEN`: Your GitHub personal access token (must have write permissions to the repository)
     - `YOUR_PERSONAL_ACCESS_TOKEN_IRIS`: A dedicated personal access token for the IRIS system
4. **Install dependencies:**
   - Install the dependencies listed in the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

## 📄 License

This project is released under the [MIT license](LICENSE).

## ❓ Help and Support

If you have any questions or need support, please create a new issue on the [GitHub Issues](https://github.com/Sunwood-ai-labs/IRIS/issues) page.

## 🤝 Contributions

Contributions to the project are highly welcome!

- Create issues to report improvements or problems
- Suggest new features
- Submit pull requests to improve the code

For first-time contributors, please refer to the [First Contributions](https://github.com/firstcontributions/first-contributions) guide.