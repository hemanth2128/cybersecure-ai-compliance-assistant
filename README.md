# cybersecure-ai-compliance-assistant

An **Enterprise AI multi-agent system** that helps organizations quickly assess their **cybersecurity posture** and generate a lightweight **compliance report** using Gemini models and a simple rule-based risk engine.

Built as part of the **Google 5-Day AI Agents Intensive – Capstone Project (2025)**.

---

## 1. Problem Statement

Organizations need to follow security and compliance frameworks such as **ISO 27001**, **NIST CSF**, and **SOC 2**.  
However:

- Assessing security posture is often **manual and time-consuming**
- Documentation is **boring, repetitive, and highly text-heavy**
- Small teams or startups may **not** have a dedicated compliance expert

There is a clear need for a **guided assistant** that can collect information, evaluate basic risks, and generate a clear report.

---

## 2. Solution Overview

**CyberSecure AI Compliance Assistant** is a **multi-agent system** that:

1. Collects organization and security posture details from the user  
2. Uses a research agent to load simplified security standards  
3. Evaluates gaps and risks using a risk analysis agent  
4. Uses Gemini to generate a structured **markdown compliance report**  
5. Evaluates the structure of the report to ensure key sections are present  

The output is:

- A markdown report saved in the `reports/` folder
- Ready to be used as a starting point for security reviews or documentation

---

## 3. Architecture Overview

High-level architecture:

```mermaid
flowchart TD
    U[User] --> I[Intake Agent]
    I --> M[(Session Memory)]
    M --> R[Research Agent]
    R --> K[Risk Analysis Agent]
    K --> W[Report Writer Agent (Gemini)]
    W --> E[Evaluation Agent]
    E --> F[Final Markdown Report]

4. Agent Roles and Responsibilities
4.1 Intake Agent

File: src/agents/intake_agent.py

Collects:

Organization name

Industry

Employee count

Cloud environment

MFA usage

Encryption at rest

Regular backups

Whether personal data is stored

Stores all this in SessionMemory under org_profile.

4.2 Research Agent

File: src/agents/research_agent.py

Simulates fetching security standards (ISO 27001, NIST CSF, SOC 2)

Writes a summary of key control areas to memory under security_standards

In a more advanced version, this could call external tools (Google Search, OpenAPI).

4.3 Risk Analysis Agent

File: src/agents/risk_agent.py

Compares the organization profile against simple rules:

Missing MFA → HIGH risk

Missing encryption at rest → HIGH risk

No regular backups → MEDIUM risk

Storing customer personal data without encryption → HIGH risk

Stores the result as a list of dictionaries in memory under risks.

4.4 Report Writer Agent

File: src/agents/report_writer_agent.py

Uses Gemini (models/gemini-2.5-flash) to generate a structured markdown report with sections:

# Cybersecurity Compliance Report for <Org>

## 1. Executive Summary

## 2. Organization Profile

## 3. Risk Assessment

## 4. Recommended Improvement Roadmap

## 5. Additional Notes and Compliance Guidance

Saves the report to reports/cybersecure_report_<timestamp>.md via save_report_to_file().

4.5 Evaluation Agent

File: src/agents/evaluation_agent.py

Checks if the report contains all required sections:

Executive Summary

Organization Profile

Risk Assessment

Recommended Improvement Roadmap

Additional Notes and Compliance Guidance

Prints whether the report is structurally complete.

5. Memory and State Management

File: src/memory/session_service.py

SessionMemory is a simple in-memory key-value store for:

org_profile

security_standards

risks

report

In a real production environment, this could be replaced with:

A database

A long-term memory service

A cloud-hosted session store

6. Tools
6.1 Report Save Tool

File: src/tools/report_save_tool.py

Function: save_report_to_file(report_text: str, directory: str = "reports")

Saves the report as a markdown file and returns the file path.

7. Tech Stack

Language: Python

AI Model: models/gemini-2.5-flash via google-genai SDK

CLI library: rich (for nicer console output)

Config: .env with GOOGLE_API_KEY

8. How to Run Locally
8.1 Install dependencies
pip install -r requirements.txt


Ensure requirements.txt contains:

google-genai
python-dotenv
rich

8.2 Set up .env

Create .env in the project root:

GOOGLE_API_KEY=YOUR_REAL_API_KEY_HERE
PROJECT_ID=placeholder
LOCATION=us-central1


Add .env to .gitignore:

.env

8.3 Run the multi-agent workflow
python src/main.py


You will be prompted to enter organization and security information.
At the end, a report will be created in the reports/ folder.

9. Example Output

Folder: reports/

Example file: cybersecure_report_20251128_123456.md

Open this file to see:

Executive summary

Organization profile

A markdown risk table

A prioritized improvement roadmap

You can attach this as:

A screenshot in your Kaggle submission

A snippet in your write-up

10. Mapping to Capstone Requirements

This project demonstrates:

Multi-agent system:

IntakeAgent, ResearchAgent, RiskAnalysisAgent, ReportWriterAgent, EvaluationAgent

Tools:

Custom report save tool (report_save_tool.py)

Sessions & Memory:

SessionMemory stores org profile, risks, and report

Context engineering:

Prompt carefully structured for Gemini report generation

Observability:

Each agent logs its steps to the console

Agent evaluation:

EvaluationAgent checks report structure

Use of Gemini:

ReportWriterAgent uses models/gemini-2.5-flash to generate the content

11. Future Enhancements

Add real web search tools to fetch live security standards

Persist memory using a database or cloud-hosted store

Add a simple web UI (FastAPI / React)

Export report as PDF

Map specific controls directly to ISO 27001 / NIST CSF sections

12. Author

Name: Hemanth Kumar S

Role: B.E. Computer Science and Engineering (Cyber Security) Student

Project: Google 5-Day AI Agents Intensive – Capstone Project (Enterprise Agents Track)