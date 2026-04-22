# tests/test_general_assistant.py
import os
import pytest
from agent.general_assistant import GeneralAssistant

def test_assistant_initialization():
    """Testet die Initialisierung (f, A) des Assistenten (m, A)."""
    assistant = GeneralAssistant()
    assert assistant.name == "General AI Assistant"
    assert assistant.client is not None


def test_ask_simple_question():
    """Testet eine einfache Frage (f, A)."""
    # Überspringe (A) den Test (m, A), wenn kein API-Key (m) vorhanden ist
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY nicht gesetzt")
    
    assistant = GeneralAssistant()
    answer = assistant.ask("Was ist 2+2?")
    
    assert answer is not None
    assert len(answer) > 0
    assert isinstance(answer, str)


def test_ask_with_context():
    """Testet eine Frage (f, A) mit Kontext (m, D)."""
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY nicht gesetzt")
    
    assistant = GeneralAssistant()
    context = "Ich bin Business Analyst in der Automobilindustrie."
    question = "Welche Tools sollte ich kennen?"
    
    answer = assistant.ask(question, context)
    
    assert answer is not None
    assert len(answer) > 0
