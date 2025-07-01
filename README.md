AI Coding Agent

A Python-based AI coding agent powered by Google's Gemini AI, designed to analyze, debug, and enhance codebases. This project showcases an intelligent assistant that interacts with your code, offering actionable suggestions and insights through function calls.

✨ Features

Code Analysis: Scans and evaluates Python files in your project.
Bug Detection: Identifies potential bugs and issues in your code.
Code Suggestions: Recommends improvements and refactoring opportunities.
Interactive Chat: Discuss your code with the AI agent in real-time.
File System Integration: Reads and processes multiple project files.
Gemini AI Integration: Leverages Google's Gemini model for intelligent analysis.

📋 Prerequisites
Python 3.8 or higher
Google AI API key (Gemini)
Git (for version control)
uv (recommended for dependency management)

🛠️ Installation

Clone the repository:

git clone https://github.com/toddswift/ai-agent.git
cd ai-agent

Install dependencies: Using uv (recommended, leveraging pyproject.toml and uv.lock):
uv sync

Alternatively, use pip:
pip install -r requirements.txt

Set up your Google AI API key:
Obtain an API key from Google AI Studio.
Set it as an environment variable:
export GOOGLE_AI_API_KEY="your-api-key-here"
Or create a .env file in the project root (ensure .env is in .gitignore):
GOOGLE_AI_API_KEY=your-api-key-here

🚀 Usage

Run the agent:
uv run python main.py
Or, if not using uv:
python main.py

The agent will:
Scan the project directory for Python files.
Analyze code structure and provide an initial assessment.
Enter interactive mode for further queries.

Example Interaction:

🤖 AI Coding Agent Started
📁 Found 3 Python files
🔍 Analysis complete: 1 bug detected, 2 optimizations suggested

💬 Ask away! Try:
- "Find bugs in utils.py"
- "Optimize my main.py"
- "Add error handling to fetch_data()"

📂 Project Structure

ai-agent/
├── main.py              # Main agent script
├── README.md            # Project documentation
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock             # Locked dependency versions
├── requirements.txt     # Fallback dependency list
└── src/                # Your Python code files

🔍 How It Works

The agent leverages Google's Gemini AI with function-calling capabilities to:

Read Files: Scans Python files using read_file() and list_files().
Analyze Code: Performs deep analysis with analyze_code().
Suggest Improvements: Offers refactoring and optimization via suggest_improvements().
Interact Safely: Operates in read-only mode by default.

🛡️ Safety Considerations

⚠️ Security Notes:
Educational Project: Not production-ready; use for learning purposes.
Read-Only Mode: Prevents unintended file modifications.
API Key Security: Never commit your Google AI API key or .env file. Ensure .env is in .gitignore.
Code Review: Always review AI suggestions before applying them.
Version Control: Commit changes before running the agent to allow easy rollbacks.

🌟 Extending the Project

Enhance the agent by:
Adding functions for code formatting, testing, or documentation.
Supporting other AI models (e.g., via OpenAI or Hugging Face).
Extending to other languages (e.g., JavaScript, Go).
Integrating with IDEs or CI/CD pipelines.
Adding static analysis or security scanning.

🐛 Troubleshooting

API Key Errors:

Verify the key is set (echo $GOOGLE_AI_API_KEY or check .env).
Ensure the key has Gemini API access and isn’t expired.

Dependency Issues:

Run uv sync or pip install -r requirements.txt again.
Check Python version (python --version).

File Access Problems:

Ensure Python files are readable (ls -l).
Run the agent from the project root.

Rate Limits:
Check Google AI Studio for API usage limits.
Wait or request a higher quota if needed.

🤝 Contributing

We welcome contributions! Follow these steps:
Fork the repository.
Create a feature branch:
git checkout -b feature/your-feature
Commit your changes:
git commit -m "Add your feature"

Push to the branch:

git push origin feature/your-feature

Open a Pull Request on GitHub.

Please include tests and update documentation as needed.

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
Built as part of the Boot.dev curriculum.
Powered by Google's Gemini AI.
Inspired by AI coding assistants like Cursor and Claude.

⚠️ Disclaimer
This is an educational project for demonstrating AI-assisted coding. Use responsibly and review AI suggestions before applying them in production.

Happy Coding! 🚀

For questions or issues, open a GitHub issue or contact the maintainer.