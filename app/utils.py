# app/utils.py
from rich.console import Console
from rich.prompt import Prompt
from app.recommender import recommendations  # ✅ import no topo

console = Console()

def ask_yes_no(question: str) -> bool:
    """
    Ask a yes/no question and return True for yes, False for no.
    """
    while True:
        answer = Prompt.ask(f"[bold cyan]{question}[/bold cyan] (yes/no)").strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            console.print("[red]Please answer with 'yes' or 'no'.[/red]")

def print_header(title: str):
    """Print a stylized section header."""
    console.print(f"\n[bold green]--- {title.upper()} ---[/bold green]\n")

def print_result(recommendation_key: str):
    """
    Print recommendation using the centralized 'recommendations' dict.
    """
    rec = recommendations.get(recommendation_key)
    if rec:
        console.print(f"\n[bold yellow]{rec['name']}[/bold yellow]")
        console.print(f"[cyan]{rec['description']}[/cyan]")
        console.print(f"[blue underline]{rec['website']}[/blue underline]\n")
    else:
        console.print(f"[red]Recommendation not found for key: {recommendation_key}[/red]")
