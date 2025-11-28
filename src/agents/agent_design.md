🧠 Agent Responsibilities & Behavior Logic
1️⃣ Intake Agent

✔ Collects input from the user:

Company name

Industry

Number of employees

Cloud usage (AWS/Azure/GCP/on-prem)

Security practices (MFA, encryption, SOC monitoring, backups)

✔ Stores responses in session/memory.

2️⃣ Research Agent

✔ Uses Google Search Tool to find:

“ISO27001 controls summary applicable to SMEs”
“SOC2 checklist startup”
“NIST Cybersecurity Framework simplified”

✔ Extracts 3–5 high-level controls.

3️⃣ Risk Analysis Agent

✔ Compares user answers with expected standards.

Example rules:

Missing Practice	Risk
No MFA	High
No encryption at rest	High
No backups	Medium
No network segmentation	Low
4️⃣ Report Writer Agent

✔ Formats results into structured report:

Executive Summary

Risk Priority Table

Gap Analysis

Next Steps

5️⃣ Evaluation Agent

✔ Validates report:

Does it include risks?

Does it mention company name?

Is format readable?
