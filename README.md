# 🤖 AI Test Report Agent

An AI-powered agent for automated test report analysis  
with business and QA focus.

---

## 📋 About

This project was developed by **Kasim** – PhD in AI,  
Senior Business Analyst based in Frankfurt.

The agent reads test reports (e.g. from TestComplete),  
analyzes the results and gives a clear status summary.

---

## 🗂️ Project Structure

- **agent/**
  - `main.py` → Entry point of the program
  - `agent_core.py` → Core AI analysis logic
- **reports/**
  - `example_report.txt` → Sample test report (input)
- **output/**
  - `.gitkeep` → Placeholder for result files
- **tests/**
  - `test_agent.py` → Automated unit tests
- `requirements.txt` → Python dependencies
- `README.md` → Project documentation
---

## ⚙️ Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| pytest | Automated testing framework |
| OpenAI API | AI model integration |
| python-dotenv | Secure API key management |
| GitHub Actions | CI/CD automation |

---

## 🚀 How It Works

1. **Input:** `reports/example_report.txt`
2. **Agent:** Reads and analyzes the report
3. **Output:** Total tests / Passed / Failed / Status

---

## 👤 Author

**Kasim** – PhD in Artificial Intelligence  
Senior Business Analyst | Frankfurt, Germany  
GitHub: [RunnerTrack](https://github.com/RunnerTrack)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
