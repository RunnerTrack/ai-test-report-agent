# ai-test-report-agent
# Hauptdatei (f) des KI-Agenten

def main():
    print("AI Test Report Agent gestartet...")

    with open("reports/example_report.txt", "r") as f:
        report_text = f.read()
    
    # Agent erstellen und analysieren
    agent = TestReportAgent()
    result = agent.analyze(report_text)
    
    # Ergebnis (n) ausgeben
    print(f"Total Tests:  {result['total_tests']}")
    print(f"Passed:       {result['passed']}")
    print(f"Failed:       {result['failed']}")
    print(f"Status:       {result['status']}")
    
if __name__ == "__main__":
    main()
