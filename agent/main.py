# main.py
# Hauptdatei (f) des KI-Agenten

import os
import sys

# Projektordner (m) zu Python-Pfad (m) hinzufügen
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from agent.agent_core import TestReportAgent

def main():
    print("=" * 50)
    print("AI Test Report Agent gestartet...")
    print("=" * 50)

    # Testbericht (m) einlesen
    report_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'reports', 'example_report.txt')

    with open(report_path, "r") as f:
        report_text = f.read()

    print("\nTestbericht gelesen:")
    print(report_text)

    # Schritt 1 – ohne KI analysieren
    agent  = TestReportAgent()
    result = agent.analyze(report_text)

    print("\nAnalyse (ohne KI):")
    print(f"  Total Tests : {result['total_tests']}")
    print(f"  Passed      : {result['passed']}")
    print(f"  Failed      : {result['failed']}")
    print(f"  Status      : {result['status']}")

    # Schritt 2 – MIT KI analysieren
    print("\nKI-Analyse (OpenAI):")
    ai_result = agent.analyze_with_ai(report_text)
    print(ai_result)

    print("\nKI-Analyse (OpenAI)-2:")
    question2="(Ich möchte, dass du ab jetzt, mein auf Deutsch geschriebene Sätze grammatisch prüfst und korrigierst bei Bedarf) Gibt heutzutage da eine Anstalldung im Darmstadt? Wie oft werden diese Anstalltungen stattfinden? Wie weit ist es zu meiner Arbeit?"
    ai_result = agent.analyze_with_ai(question2)
    print(question2)

    question3="Kannst du mir ein paar große Geschäfte nah zu meinem Wohnung in Eschborn verraten?"
    ai_result = agent.analyze_with_ai(question3)
    print(ai_result)

    question4="Kannst du mir nochmal sagen, wie weit ist diese Strecke von meinem Wohnung?"
    ai_result = agent.analyze_with_ai(question4)
    print(ai_result)


if __name__ == "__main__":
    main()
