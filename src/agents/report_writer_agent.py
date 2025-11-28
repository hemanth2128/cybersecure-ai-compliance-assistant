# src/agents/report_writer_agent.py

from typing import Any, Dict, List
from rich.console import Console
from google import genai
from memory.session_service import SessionMemory
from tools.report_save_tool import save_report_to_file


class ReportWriterAgent:
    """
    Uses Gemini to generate a structured cybersecurity compliance report
    based on organization profile, risk analysis, and tone preference.
    """

    def __init__(self, memory: SessionMemory, console: Console, client: genai.Client):
        self.memory = memory
        self.console = console
        self.client = client

    def run(self) -> None:
        self.console.print("\n[ReportWriterAgent] Generating compliance report with Gemini...")

        profile: Dict[str, Any] = self.memory.get("org_profile")
        risks: List[Dict[str, Any]] = self.memory.get("risks")
        risk_score: Dict[str, Any] = self.memory.get("risk_score", {})

        if not profile or risks is None:
            self.console.print("[ReportWriterAgent] Missing profile or risk data. Cannot generate report.")
            return

        prompt = self._build_prompt(profile, risks, risk_score)

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

    def _build_prompt(
        self,
        profile: Dict[str, Any],
        risks: List[Dict[str, Any]],
        risk_score: Dict[str, Any]
    ) -> str:
        org_name = profile.get("organization_name", "Unknown Organization")
        tone = (profile.get("tone_mode") or "audit").lower()

        tone_instruction = {
            "audit": "Use precise compliance and audit-style language. Be direct about gaps and controls.",
            "advisory": "Use a supportive, consulting tone. Focus on guidance and next steps rather than blame.",
            "executive": "Write in a concise, business-oriented style suitable for executive leadership summaries."
        }.get(tone, "Use a neutral professional tone.")

        score_value = risk_score.get("score", "N/A")
        score_status = risk_score.get("status", "Unknown")

        prompt = f"""
You are an experienced cybersecurity and compliance consultant.

Write a cybersecurity compliance assessment report for the organization below.

STYLE / TONE:
- Tone mode selected by user: {tone}
- Apply this style: {tone_instruction}

OVERALL RISK SCORE:
- Numeric score: {score_value} / 100
- Posture: {score_status}

ORGANIZATION PROFILE:
- Name: {profile.get('organization_name')}
- Industry: {profile.get('industry')}
- Employee count: {profile.get('employee_count')}
- Cloud environment: {profile.get('cloud_environment')}
- Uses MFA: {profile.get('uses_mfa')}
- Encryption at rest: {profile.get('encryption_at_rest')}
- Regular backups: {profile.get('regular_backups')}
- Stores personal data: {profile.get('stores_personal_data')}

RISK ANALYSIS INPUT (list of dicts with control, status, risk, recommendation):
{risks}

Now produce the report in the following markdown structure:

# Cybersecurity Compliance Report for {org_name}

## 0. Overview and Risk Score
- Overall risk score (0-100) and posture label.
- One short paragraph summarizing the situation in plain language.

## 1. Executive Summary
A short, clear explanation of:
- The overall security posture
- The key risks (in business terms)
- The urgency level, if posture is "Critical"

## 2. Organization Profile
Summarize the profile in a few bullet points.

## 3. Risk Assessment
Present a table in markdown with the following columns:

| Control | Status | Risk Level | Recommendation |

Populate the table using the risk analysis input.

## 4. Recommended Improvement Roadmap
Organize improvements into phases:

- Phase 1: High priority (immediate actions)
- Phase 2: Medium priority (short to mid-term)
- Phase 3: Low priority / optimization

For each phase, list a few bullet points.

## 5. Alignment with Common Frameworks
Briefly map key recommendations to frameworks such as:
- ISO 27001
- NIST CSF
- SOC 2 (Security)

## 6. Additional Notes and Next Steps
Provide any final advice, including:
- Suggested order of implementation
- Advice for small teams or limited budgets

The report should:
- Be friendly but professional
- Avoid unnecessary fear-based language
- Help the reader understand what to do next.
"""
        return prompt
