import os
from openai import OpenAI

class TestReportAgent:

    def __init__(self):
        self.name = "AI Test Report Agent"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
