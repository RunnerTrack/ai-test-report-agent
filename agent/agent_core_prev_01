# agent_core.py
# KI-Logik (f) für die Analyse (f) von Testberichten (Pl.)

class TestReportAgent:
    """
    KI-Agent (m) zur Analyse (f) von Testberichten (Pl.)
    Eingabe (f):  Testbericht (m) als Text
    Ausgabe (f):  Zusammenfassung (f) und Empfehlung (f)
    """

    def __init__(self):
        self.name = "AI Test Report Agent"

    def analyze(self, report_text: str) -> dict:
        """
        Analysiert (A) einen Testbericht (m)
        und gibt eine Zusammenfassung (f) zurück.
        """
        lines = report_text.strip().split("\n")
        
        total   = len(lines)
        passed  = sum(1 for l in lines if "PASS" in l.upper())
        failed  = sum(1 for l in lines if "FAIL" in l.upper())

        return {
            "total_tests":  total,
            "passed":       passed,
            "failed":       failed,
            "status":       "OK" if failed == 0 else "ATTENTION NEEDED"
        }
