
# src/agents/research_agent.py

from typing import Dict, List, Any
from rich.console import Console
from google import genai
from memory.session_service import SessionMemory


class ResearchAgent:
    """
    In a real system this would call external tools (e.g. Google Search)
    to fetch control requirements. For the capstone and offline running,
    we simulate this with predefined data and (optionally) Gemini summarization.
    """

    def __init__(self, memory: SessionMemory, console: Console, client: genai.Client):
        self.memory = memory
        self.console = console
        self.client = client

    def run(self) -> None:
        self.console.print("\n[ResearchAgent] Starting security standards research...")

        # If already researched for this session, skip
        existing = self.memory.get("security_standards")
        if existing:
            self.console.print("[ResearchAgent] Standards already in memory. Skipping.")
            return

        # Simulated standards; you can mention this simplification in your write-up.
        standards: List[Dict[str, Any]] = [
            {
                "standard": "ISO 27001",
                "required_controls": [
                    "Access control",
                    "Encryption of data at rest and in transit",
                    "Incident response plan",
                    "Backup and recovery",
                    "Asset management",
                    "Logging and monitoring",
                ],
            },
            {
                "standard": "NIST CSF",
                "required_controls": [
                    "Identify critical assets",
                    "Protect data using encryption",
                    "Detect security events",
                    "Respond to incidents",
                    "Recover from disruptions",
                ],
            },
            {
                "standard": "SOC 2 (Security)",
                "required_controls": [
                    "Logical access control",
                    "Change management",
                    "System operations monitoring",
                    "Data backup and recovery",
                ],
            },
        ]

        self.memory.set("security_standards", standards)
        self.console.print("[ResearchAgent] Security standards summary stored in memory.")
