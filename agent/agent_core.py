# agent_core.py
# KI-Logik (f) mit OpenAI API

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class TestReportAgent:
    """
    KI-Agent (m) zur Analyse (f) von Testberichten (Pl.)
    Eingabe (f):  Testbericht (m) als Text
    Ausgabe (f):  Zusammenfassung (f) und Empfehlung (f)
    """

    def __init__(self):
        self.name   = "AI Test Report Agent"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze(self, report_text: str) -> dict:
        """
        Analysiert (A) einen Testbericht (m) – ohne KI
        Zählt (A) PASS und FAIL
        """
        lines  = report_text.strip().split("\n")
        total  = len(lines)
        passed = sum(1 for l in lines if "PASS" in l.upper())
        failed = sum(1 for l in lines if "FAIL" in l.upper())

        return {
            "total_tests": total,
            "passed":      passed,
            "failed":      failed,
            "status":      "OK" if failed == 0 else "ATTENTION NEEDED"
        }

    def analyze_with_ai(self, report_text: str) -> str:
        """
        Analysiert (A) einen Testbericht (m) – MIT KI!
        Gibt eine Empfehlung (f) auf Englisch zurück
        """
        prompt = f"""
You are a QA analyst and Business Analyst assistant.
Analyze the following test report and provide:
1. A short summary of the results
2. Which tests failed and why
3. A clear recommendation for the development team

Test Report:
{report_text}
"""
        response = self.client.chat.completions.create(
            model    = "gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are a helpful QA and BA assistant."},
                {"role": "user",   "content": prompt}
            ],
            max_tokens = 500
        )

        return response.choices[0].message.content
