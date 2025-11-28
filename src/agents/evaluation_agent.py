
# src/agents/evaluation_agent.py

from typing import Any, Dict, List
from rich.console import Console
from memory.session_service import SessionMemory


class EvaluationAgent:
    """
    Performs a simple structural validation of the generated report.
    """

    REQUIRED_SECTIONS = [
        "## 1. Executive Summary",
        "## 2. Organization Profile",
        "## 3. Risk Assessment",
        "## 4. Recommended Improvement Roadmap",
        "## 5. Additional Notes and Compliance Guidance",
    ]

    def __init__(self, memory: SessionMemory, console: Console):
        self.memory = memory
        self.console = console

    def run(self) -> None:
        self.console.print("\n[EvaluationAgent] Evaluating generated report...")

        report: str = self.memory.get("report", "")
        if not report:
            self.console.print("[EvaluationAgent] No report found in memory.")
            return

        missing_sections: List[str] = []

        for section in self.REQUIRED_SECTIONS:
            if section not in report:
                missing_sections.append(section)

        if missing_sections:
            self.console.print("[EvaluationAgent] Report is missing the following sections:")
            for s in missing_sections:
                self.console.print(f" - {s}")
            self.console.print("[EvaluationAgent] You can re-run the ReportWriterAgent with adjusted prompts if needed.")
        else:
            self.console.print("[EvaluationAgent] Report structure looks complete.")
