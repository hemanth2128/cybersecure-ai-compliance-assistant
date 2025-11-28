Workflow Sequence:

1. Intake Agent collects and stores inputs in session memory.
2. Research Agent retrieves external compliance standards via Search Tool.
3. Risk Analysis Agent compares user answers vs. standards and generates a structured risk model.
4. Report Writer Agent formats final cybersecurity compliance report.
5. Evaluation Agent reviews report:
   - If valid → Done
   - If invalid → Loop back to report writer
