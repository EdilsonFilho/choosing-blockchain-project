# 🧭 Blockchain Advisor
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white) 
![MIT License](https://img.shields.io/badge/License-MIT-green)
![CLI](https://img.shields.io/badge/CLI-Terminal-orange)

An interactive command-line tool that helps developers and enterprises choose the most suitable blockchain platform for their projects — based on a guided yes/no questionnaire.

## 🚀 Features
- Quick Mode (5 questions) — for fast recommendations.
- Advanced Mode (30 questions) — for deep technical analysis.
- Interactive terminal experience.
- Modular and extensible architecture — easy to add new blockchains or questions.
- Recommendations include name, description, and official website.

## 🧩 Project Structure
```
choosing-blockchain-project/
├─ app/
│  ├─ main.py              # Entry point
│  ├─ utils.py             # Helper functions for prompts and printing
│  ├─ recommender.py       # Recommendation logic and centralized blockchain data
│  ├─ questions_quick.py   # Quick Mode logic
│  └─ questions_advanced.py # Advanced Mode logic
├─ tests/
│  ├─ test_quick_mode.py
│  ├─ test_advanced_mode.py
│  └─ test_quick_mode_interactive.py
├─ requirements.txt
└─ README.md
```

## 🧠 How to Run

# Clone the repository
```sh
git clone https://github.com/EdilsonFilho/choosing-blockchain-project.git
```
```sh
cd choosing-blockchain-project
```

# Create virtual environment
```sh
python -m venv .venv
```
```sh
source .venv/bin/activate  # (on Windows use: .venv\Scripts\activate)
```

# Install dependencies
```sh
pip install -r requirements.txt
```

# Run the app
```sh
python -m app.main
```
## Modes

- Quick Mode: Follow 5 simple yes/no questions to get a fast blockchain recommendation.
- Advanced Mode: Answer 30 detailed questions for a deeper technical recommendation.

# 🧪 Running Tests
Automated tests are included to ensure robustness for all possible combinations of answers:
```sh
pytest -v
``` 
Test Coverage
- Quick Mode: Tests all 32 combinations of 5 yes/no questions.
- Advanced Mode: Tests multiple random and extreme combinations of 30 questions.
- Interactive Tests: Simulate user input to verify that the terminal interface never breaks.

> ✅ All tests verify that recommend_blockchain always returns a valid recommendation key and that the interactive terminal works correctly.

# 🔧 Contributing
- Add new blockchains or update descriptions in `app/recommender.py`.
- Add new questions or adjust scoring in `questions_quick.py / questions_advanced.py`.
- Ensure tests pass after changes.

### Author

jose.silva_filho@insa-rouen.fr
