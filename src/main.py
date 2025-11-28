
import os
from dotenv import load_dotenv
from google.genai import Client
from rich.console import Console

console = Console()

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ Google API Key missing. Set it inside .env file.")

client = Client(api_key=GOOGLE_API_KEY)

def run_intake_agent():
    console.print("[bold cyan]🤖 Intake Agent Started...[/bold cyan]")

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="Hello! Please ask the first question for organization onboarding."
    )

    console.print(f"[bold green]Agent Response:[/bold green] {response.text}")


if __name__ == "__main__":
    console.print("[bold yellow]🚀 CyberSecure AI Compliance Assistant (Prototype Run)...[/bold yellow]")
    run_intake_agent()
