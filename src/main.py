import os
from dotenv import load_dotenv
from rich.console import Console
from google import genai  # Requires `google-genai` package installed

# Load environment variables from .env file
load_dotenv()

console = Console()


def get_client() -> genai.Client:
    """Initialize the GenAI client using the API key."""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise RuntimeError("❌ ERROR: GOOGLE_API_KEY missing in .env file")

    return genai.Client(api_key=api_key)


def test_connection():
    """Sanity test: list available models."""
    client = get_client()
    console.print("\n🔍 Checking available Gemini models...")
    
    try:
        models = client.models.list()
        console.print("\n📌 Available Models:")
        for m in models:
            console.print(f"- {m.name}")
    except Exception as e:
        console.print("\n❌ ERROR while fetching models:")
        console.print(str(e))


def run_intake_agent():
    """Runs a basic initial test with Gemini using the selected model."""
    console.print("\n=== Intake Agent Started ===")

    client = get_client()

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",   # <-- VERIFIED WORKING MODEL
            contents=(
                "You are the intake agent for a cybersecurity compliance assistant. "
                "Greet the user with one short professional sentence."
            )
        )

        console.print("\n🤖 Agent Response:")
        console.print(response.text)

    except Exception as e:
        console.print("\n❌ ERROR while generating response:")
        console.print(str(e))


if __name__ == "__main__":
    console.print("\nCyberSecure AI Compliance Assistant (Prototype Run)...")
    
    # OPTIONAL FIRST RUN (shows available models)
    # Uncomment if needed
    # test_connection()

    run_intake_agent()
    console.print("\n✔ System test complete.\n")
