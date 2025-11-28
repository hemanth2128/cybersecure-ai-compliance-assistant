# cybersecure-ai-compliance-assistant

🛡️ CyberSecure AI Compliance Assistant
      
      Intelligent Multi-Agent System for Automated Cybersecurity Risk & Compliance Reporting

🚀 Overview
     
      The CyberSecure AI Compliance Assistant is an AI-powered multi-agent system designed to automate cybersecurity posture assessment and generate compliance-aligned reports.
Using structured inputs, rule-based risk scoring, and an LLM-powered report generator (Gemini 2.5 Flash), this tool produces an actionable compliance report aligned with frameworks such as:

ISO 27001

NIST Cybersecurity Framework

SOC 2 Security Trust Principles

This project was built as part of the Google AI 5-Day Agent Intensive Program (Capstone Project) under the Enterprise Agent track.

🎯 Problem Statement

Cybersecurity compliance assessments are:

Time-consuming

Require specialized knowledge

Often inconsistent between consultants

Small and mid-sized organizations struggle to perform compliant security posture evaluations without experts — increasing the risk of:

⚠️ Audit failure
⚠️ Regulatory penalties
⚠️ Customer trust damage

This project aims to solve that.

💡 Solution

This solution automates the assessment workflow using a multi-agent architecture, providing:

Intake and structured data gathering

Context-aware memory and session state

Rule-based security control evaluation

AI-generated compliance reporting

Tone-customizable output (Audit / Advisory / Executive)

Numeric cybersecurity posture score

📌 Output is saved automatically in /reports/.

🧠 Agent Architecture
Agent	Function
Intake Agent	Collects organizational and security data interactively
Research Agent	Fetches industry standards (static version placeholder)
Risk Analysis Agent	Applies logic-based scoring and creates risk table
Report Writer Agent	Uses Gemini to produce formatted compliance report
Evaluation Agent	Verifies report structure and ensures completeness
📍 System Flow Diagram
flowchart TD
    A(User Input) --> B[Intake Agent]
    B --> C[(Session Memory)]
    C --> D[Research Agent]
    D --> E[Risk Analysis Agent]
    E --> F[Report Writer Agent → Gemini]
    F --> G[Evaluation Agent]
    G --> H[Final Report (.md/PDF)]


📄 Final architecture image (PNG) is stored under:

/diagrams/architecture.png

🔍 Key Features
Feature	Status
Multi-agent workflow	✔
Memory state management	✔
Rule-based risk scoring (0–100)	✔
Dynamic tone output (Audit / Advisory / Executive)	✔
Document generator (Markdown)	✔
Report validation agent	✔
Persistent file saving system	✔
🛠️ Technology Stack
Component	Technology
Language	Python 3.11+
AI Model	Gemini 2.5 Flash
Framework	Google AI Agent Development Kit
Memory State	JSON session memory
Output Format	Markdown report (.md)
📂 Repository Structure
cybersecure-ai-compliance-assistant/
│
├── agents/                       # All agent classes
├── memory/                       # Session memory system
├── tools/                        # File save helpers
├── reports/                      # Generated compliance reports
├── diagrams/                     # Architecture images
├── src/main.py                  # Pipeline runner
├── requirements.txt             # Dependencies
└── README.md                    # Documentation

▶️ How to Run Locally
1️⃣ Install dependencies:
pip install -r requirements.txt

2️⃣ Create .env file:
GOOGLE_API_KEY=your_api_key_here

3️⃣ Run the assistant:
python src/main.py

🧪 Example Output

A sample generated report is available under:

/reports/sample_output.md

📈 Future Enhancements

🔄 Auto-retry loop with enhanced evaluation

🧠 Persistent long-term memory database

🕹️ Web UI using Streamlit or React

📤 Deployment via Cloud Run for API integration

📊 Export to PDF & SOC2-style audit format

🏆 Submission Track

📌 Enterprise AI Agents – Google AI Capstone 2025
Project uses:

Multi-agent design

Context engineering

Tool execution

State/memory management

Evaluation & refinement loop

👤 Author

Name: Hemanth Kumar S
Role: Cybersecurity Engineering Student
Track: AI + Cybersecurity Automation
Submission Category: Enterprise Agents
