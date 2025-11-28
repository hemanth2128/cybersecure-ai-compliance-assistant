# src/main.py

import os
from dotenv import load_dotenv
from rich.console import Console
from google import genai

from memory.session_service import SessionMemory
from agents.intake_agent import IntakeAgent
from agents.research_agent import ResearchAgent
from agents.risk_agent import RiskAnalysisAgent
from agents.report_writer_agent import ReportWriterAgent
from agents.evaluation_agent import EvaluationAgent

load_dotenv()
console = Console()


def get_client() -> genai.Client:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is not set in .env file.")
    return genai.Client(api_key=api_key)


def main() -> None:
    console.print("\nCyberSecure AI Compliance Assistant - Multi-Agent Run")

    client = get_client()
    memory = SessionMemory()

    intake_agent = IntakeAgent(memory=memory, console=console, client=client)
    research_agent = ResearchAgent(memory=memory, console=console, client=client)
    risk_agent = RiskAnalysisAgent(memory=memory, console=console)
    report_writer_agent = ReportWriterAgent(memory=memory, console=console, client=client)
    evaluation_agent = EvaluationAgent(memory=memory, console=console)

    intake_agent.run()
    research_agent.run()
    risk_agent.run()
    report_writer_agent.run()
    evaluation_agent.run()

    console.print("\nRun complete. Check the 'reports' folder for the generated report.\n")


if __name__ == "__main__":
    main()
