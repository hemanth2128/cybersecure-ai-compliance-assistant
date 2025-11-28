# src/agents/risk_agent.py

from typing import Any, Dict, List
from rich.console import Console
from memory.session_service import SessionMemory


class RiskAnalysisAgent:
    """
    Compares organization profile with basic expectations
    and generates a list of risks and an overall risk score.
    """

    def __init__(self, memory: SessionMemory, console: Console):
        self.memory = memory
        self.console = console

    def _normalize_answer(self, value: str) -> str:
        return (value or "").strip().lower()

    def run(self) -> None:
        self.console.print("\n[RiskAnalysisAgent] Starting risk evaluation...")

        profile: Dict[str, Any] = self.memory.get("org_profile")
        if not profile:
            self.console.print("[RiskAnalysisAgent] No organization profile found. Cannot analyze risks.")
            return

        risks: List[Dict[str, Any]] = []

        uses_mfa = self._normalize_answer(profile.get("uses_mfa", "unknown"))
        encryption_at_rest = self._normalize_answer(profile.get("encryption_at_rest", "unknown"))
        regular_backups = self._normalize_answer(profile.get("regular_backups", "unknown"))
        stores_personal_data = self._normalize_answer(profile.get("stores_personal_data", "unknown"))

        # Risk rules
        if uses_mfa != "yes":
            risks.append({
                "control": "Multi-Factor Authentication (MFA)",
                "status": "Missing or unknown",
                "risk": "HIGH",
                "recommendation": "Implement MFA for all privileged and remote access accounts."
            })

        if encryption_at_rest != "yes":
            risks.append({
                "control": "Encryption at rest",
                "status": "Missing or unknown",
                "risk": "HIGH",
                "recommendation": "Enable encryption for all sensitive data at rest."
            })

        if regular_backups != "yes":
            risks.append({
                "control": "Regular backups",
                "status": "Missing or unknown",
                "risk": "MEDIUM",
                "recommendation": "Implement automated, tested backups for critical systems and data."
            })

        if stores_personal_data == "yes" and encryption_at_rest != "yes":
            risks.append({
                "control": "Protection of personal data",
                "status": "Insufficient",
                "risk": "HIGH",
                "recommendation": "Encrypt personal data and apply strict access controls."
            })

        if not risks:
            risks.append({
                "control": "General posture",
                "status": "Good baseline",
                "risk": "LOW",
                "recommendation": "Continue monitoring, testing controls, and improving security maturity."
            })

        # NEW: compute numeric risk score
        score = 100
        for r in risks:
            if r["risk"] == "HIGH":
                score -= 30
            elif r["risk"] == "MEDIUM":
                score -= 15
            else:
                score -= 5

        if score < 0:
            score = 0

        if score >= 85:
            posture = "Strong"
        elif score >= 60:
            posture = "Moderate"
        else:
            posture = "Critical"

        risk_score = {"score": score, "status": posture}

        self.memory.set("risks", risks)
        self.memory.set("risk_score", risk_score)

        self.console.print(f"[RiskAnalysisAgent] Identified {len(risks)} risk items.")
        self.console.print(f"[RiskAnalysisAgent] Overall risk score: {score} / 100 ({posture}).")
