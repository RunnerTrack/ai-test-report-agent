# agent/main.py
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from agent.agent_core import TestReportAgent
from agent.general_assistant import GeneralAssistant


def print_menu():
    """Zeigt das Hauptmenü (n, A)."""
    print("\n" + "=" * 60)
    print("🤖 AI Test Report Agent - Hauptmenü")
    print("=" * 60)
    print("1. Testbericht analysieren (vorhandener Beispiel-Report)")
    print("2. Eigenen Testbericht analysieren (Text eingeben)")
    print("3. Allgemeine Frage an KI stellen")
    print("4. Beenden")
    print("=" * 60)


def analyze_example_report():
    """Analysiert den Beispiel-Testbericht (m, A)."""
    print("\n📄 Lade Beispiel-Testbericht...")
    
    report_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'reports', 'example_report.txt')
    
    with open(report_path, "r") as f:
        report_text = f.read()
    
    print("\n--- Testbericht ---")
    print(report_text)
    print("--- Ende ---\n")
    
    agent = TestReportAgent()
    
    # Regelbasierte Analyse
    result = agent.analyze(report_text)
    print("\n📊 Analyse (regelbasiert):")
    print(f"  Total Tests : {result['total_tests']}")
    print(f"  Bestanden   : {result['passed']}")
    print(f"  Fehlgeschlagen: {result['failed']}")
    print(f"  Status      : {result['status']}")
    
    # KI-Analyse
    print("\n🤖 KI-Analyse (OpenAI GPT-4o-mini):")
    print("-" * 60)
    ai_result = agent.analyze_with_ai(report_text)
    print(ai_result)
    print("-" * 60)


def analyze_custom_report():
    """Analysiert einen vom Benutzer (m, D) eingegebenen Testbericht (m, A)."""
    print("\n📝 Gib deinen Testbericht ein (mehrere Zeilen möglich).")
    print("Beende die Eingabe (f, A) mit einer leeren Zeile (f, D):\n")
    
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    
    report_text = "\n".join(lines)
    
    if not report_text.strip():
        print("❌ Kein Text eingegeben. Abbruch (m).")
        return
    
    agent = TestReportAgent()
    
    # Regelbasierte Analyse
    result = agent.analyze(report_text)
    print("\n📊 Analyse (regelbasiert):")
    print(f"  Total Tests : {result['total_tests']}")
    print(f"  Bestanden   : {result['passed']}")
    print(f"  Fehlgeschlagen: {result['failed']}")
    print(f"  Status      : {result['status']}")
    
    # KI-Analyse
    print("\n🤖 KI-Analyse (OpenAI GPT-4o-mini):")
    print("-" * 60)
    ai_result = agent.analyze_with_ai(report_text)
    print(ai_result)
    print("-" * 60)


def ask_general_question():
    """Stellt eine allgemeine Frage (f, A) an die KI (f, D)."""
    print("\n💬 General AI Assistant")
    print("-" * 60)
    
    question = input("Deine Frage: ").strip()
    
    if not question:
        print("❌ Keine Frage eingegeben. Abbruch (m).")
        return
    
    # Optional: Kontext hinzufügen
    add_context = input("\nMöchtest du Kontext (m, A) hinzufügen? (j/n): ").strip().lower()
    context = ""
    
    if add_context == "j":
        print("Gib den Kontext (m, A) ein (leere Zeile zum Beenden):\n")
        context_lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            context_lines.append(line)
        context = "\n".join(context_lines)
    
    assistant = GeneralAssistant()
    
    print("\n🤖 Antwort:")
    print("-" * 60)
    answer = assistant.ask(question, context)
    print(answer)
    print("-" * 60)


def main():
    """Hauptfunktion (f) mit Menü-Schleife (f, D)."""
    print("\n🚀 AI Test Report Agent gestartet...")
    howmany=3
    while True:
        print_menu()
#        choice = input("\nWähle eine Option (1-4): ").strip()
        choice="1"
        howmany-=1
        if (howmany<0):
            choice="4"
        
        if choice == "1":
            analyze_example_report()
        
        elif choice == "2":
            analyze_custom_report()
        
        elif choice == "3":
            ask_general_question()
        
        elif choice == "4":
            print("\n👋 Programm (n) wird beendet. Auf Wiedersehen!")
            break
        
        else:
            print("\n❌ Ungültige Eingabe (f). Bitte wähle 1, 2, 3 oder 4.")
        
#        input("\n[Drücke Enter (m, A) zum Fortfahren...]")
            print("\nDrücke Enter zum Fortfahren nicht möglich!")


if __name__ == "__main__":
    main()
