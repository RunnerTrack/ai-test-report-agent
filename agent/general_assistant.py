# agent/general_assistant.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class GeneralAssistant:
    def __init__(self):
        self.name = "General AI Assistant"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def ask(self, question: str, context: str = "") -> str:
        """
        Stellt eine allgemeine Frage an die KI.
        
        Args:
            question: Die Benutzerfrage (f, A)
            context: Optionaler Kontext (m, A) für bessere Antworten (Pl.)
        
        Returns:
            Die KI-Antwort (f)
        """
        system_prompt = """Du bist ein hilfreicher Assistent für 
Business Analysten und QA-Engineers. Antworte präzise und 
praxisnah auf Deutsch oder Englisch, je nach Frage."""
        
        user_prompt = question
        if context:
            user_prompt = f"Kontext: {context}\n\nFrage: {question}"
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=800,
            temperature=0.7
        )
        
        return response.choices[0].message.content
