# app/main.py
import sys
from rich.console import Console
from app.questions_quick import run_quick_mode
from app.questions_advanced import run_advanced_mode
from app.utils import print_header

console = Console()

def main():
    print_header("Welcome to the Blockchain Advisor")
    console.print("This tool helps you decide which blockchain best fits your project.\n")

    while True:
        console.print("Choose a mode:")
        console.print("1 - Quick Mode (5 questions)")
        console.print("2 - Advanced Mode (30 questions)")
        console.print("Q - Quit\n")

        choice = input("> ").strip().lower()

        if choice == "1":
            run_quick_mode()
        elif choice == "2":
            run_advanced_mode()
        elif choice in ["q", "quit", "exit"]:
            console.print("\n[green]Goodbye![/green]")
            sys.exit(0)
        else:
            console.print("[red]Invalid choice. Please try again.[/red]\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Exiting... Goodbye![/red]")
        sys.exit(0)
