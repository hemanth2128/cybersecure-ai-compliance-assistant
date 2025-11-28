
# src/agents/intake_agent.py

from typing import Dict
from rich.console import Console
from google import genai
from memory.session_service import SessionMemory


class IntakeAgent:
    """
    Collects organization profile and basic security posture via CLI.
    In the capstone write-up, you can describe this as the "intake agent".
    """

    def __init__(self, memory: SessionMemory, console: Console, client: genai.Client):
        self.memory = memory
        self.console = console
        self.client = client

    def run(self) -> None:
        self.console.print("\n[IntakeAgent] Starting organization intake...")

        existing_profile = self.memory.get("org_profile")
        if existing_profile:
            self.console.print("[IntakeAgent] Existing profile found in memory. Skipping questions.")
            return

        profile: Dict[str, str] = {}

        profile["organization_name"] = input("Organization name: ").strip()
        profile["industry"] = input("Industry (Finance/Healthcare/Retail/SaaS/etc.): ").strip()
        profile["employee_count"] = input("Number of employees: ").strip()
        profile["cloud_environment"] = input("Cloud environment (AWS/Azure/GCP/On-Prem/Hybrid): ").strip()

        profile["uses_mfa"] = input("Do you use Multi-Factor Authentication (MFA)? (Yes/No/Unknown): ").strip()
        profile["encryption_at_rest"] = input("Is sensitive data encrypted at rest? (Yes/No/Unknown): ").strip()
        profile["regular_backups"] = input("Do you have regular backups? (Yes/No/Unknown): ").strip()
        profile["stores_personal_data"] = input("Do you store customer personal data? (Yes/No/Unknown): ").strip()

        self.memory.set("org_profile", profile)

        self.console.print("\n[IntakeAgent] Organization profile captured and stored in session memory.")
