# ai-test-report-agent
# Hauptdatei (f) des KI-Agenten (m)

from agent.agent_core import TestReportAgent  # ← HINZUFÜGEN!

def main():
    print("AI Test Report Agent gestartet...")

    with open("reports/examplereport.txt", "r") as f:  # ← Name korrigieren!
        report_text = f.read()
    
    agent = TestReportAgent()
    ai_result = agent.analyze_with_ai(report_text)  # ← KI statt analyze!
    print("KI-Analyse:\n", ai_result)  # ← GPT-Output!

if __name__ == "__main__":
    main()
