# app/utils.py
from rich.console import Console
from rich.prompt import Prompt

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

def print_result(message: str):
    """Print the final recommendation message."""
    console.print(f"\n[bold yellow]{message}[/bold yellow]\n")
