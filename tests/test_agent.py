# test_agent.py
# Unit Tests (Pl.) für den KI-Agenten

from agent.agent_core import TestReportAgent

def test_passed():
    agent = TestReportAgent()
    result = agent.analyze("TC001 - Login Test PASS")
    assert result["passed"] == 1

def test_failed():
    agent = TestReportAgent()
    result = agent.analyze("TC001 - Login Test FAIL")
    assert result["failed"] == 1

def test_status_ok():
    agent = TestReportAgent()
    result = agent.analyze("TC001 - Login Test PASS")
    assert result["status"] == "OK"

def test_status_attention():
    agent = TestReportAgent()
    result = agent.analyze("TC001 - Login Test FAIL")
    assert result["status"] == "ATTENTION NEEDED"
