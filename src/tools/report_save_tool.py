
# src/tools/report_save_tool.py

import os
from datetime import datetime


def save_report_to_file(report_text: str, directory: str = "reports") -> str:
    """
    Saves the generated report to a markdown file.
    Returns the file path.
    """

    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"cybersecure_report_{timestamp}.md"
    file_path = os.path.join(directory, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    return file_path
