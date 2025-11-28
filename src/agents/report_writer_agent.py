
# src/agents/report_writer_agent.py

from typing import Any, Dict, List
from rich.console import Console
from google import genai
from memory.session_service import SessionMemory
from tools.report_save_tool import save_report_to_file


class ReportWriterAgent:
    """
    Uses Gemini to generate a structured cybersecurity compliance report
    based on organization profile and risk analysis.
    """

    def __init__(self, memory: SessionMemory, console: Console, client: genai.Client):
        self.memory = memory
        self.console = console
        self.client = client

    def run(self) -> None:
        self.console.print("\n[ReportWriterAgent] Generating compliance report with Gemini...")

        profile: Dict[str, Any] = self.memory.get("org_profile")
        risks: List[Dict[str, Any]] = self.memory.get("risks")

        if not profile or risks is None:
            self.console.print("[ReportWriterAgent] Missing profile or risk data. Cannot generate report.")
            return

        prompt = self._build_prompt(profile, risks)

        try:
            response = self.client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=prompt
            )

            report_text = response.text
            self.memory.set("report", report_text)

            file_path = save_report_to_file(report_text)
            self.console.print(f"[ReportWriterAgent] Report generated and saved to: {file_path}")

        except Exception as e:
            self.console.print("[ReportWriterAgent] Error while generating report:")
            self.console.print(str(e))

    def _build_prompt(self, profile: Dict[str, Any], risks: List[Dict[str, Any]]) -> str:
        org_name = profile.get("organization_name", "Unknown Organization")

        prompt = f"""
You are a cybersecurity and compliance expert.

Generate a clear, structured cybersecurity compliance assessment report
for the following organization. Use professional, concise language that
a security engineer and business leader can both understand.

ORGANIZATION PROFILE:
- Name: {profile.get('organization_name')}
- Industry: {profile.get('industry')}
- Employee count: {profile.get('employee_count')}
- Cloud environment: {profile.get('cloud_environment')}
- Uses MFA: {profile.get('uses_mfa')}
- Encryption at rest: {profile.get('encryption_at_rest')}
- Regular backups: {profile.get('regular_backups')}
- Stores personal data: {profile.get('stores_personal_data')}

RISK ANALYSIS INPUT (list of dicts):
{risks}

Now produce the report in the following markdown structure:

# Cybersecurity Compliance Report for {org_name}

## 1. Executive Summary
(Brief overview of the security posture and key findings.)

## 2. Organization Profile
(Re-state profile in a concise way.)

## 3. Risk Assessment
Present a table in markdown:

| Control | Status | Risk Level | Recommendation |

## 4. Recommended Improvement Roadmap
Organize improvements into phases:
- Phase 1: High priority items
- Phase 2: Medium priority items
- Phase 3: Low priority / optimization

## 5. Additional Notes and Compliance Guidance
(Include any mapping or references to common frameworks such as ISO 27001, NIST CSF, or SOC 2 where relevant.)

Make sure the report is self-contained and easy to read.
"""
        return prompt
