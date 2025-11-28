import os
from dotenv import load_dotenv
from rich.console import Console
from google import genai  # requires `google-genai` package


# Load environment variables from .env
load_dotenv()

console = Console()


def get_client() -> genai.Client:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY is not set. Please add it to your .env file."
        )

    client = genai.Client(api_key=api_key)
    return client


def run_intake_agent():
    console.print("=== Intake Agent Started ===")

    client = get_client()

    # Simple test prompt just to verify everything works
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="You are the intake agent for a cybersecurity compliance assistant. "
                 "Greet the user in one short sentence."
    )

    # Print the model response
    console.print("Agent Response:")
    console.print(response.text)


if __name__ == "__main__":
    console.print("CyberSecure AI Compliance Assistant (Prototype Run)...")
    run_intake_agent()
