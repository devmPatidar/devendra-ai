from rich.console import Console
from rich.panel import Panel

console = Console()

def display_response(result):
    console.print(Panel.fit(
        f"[bold cyan]Query:[/bold cyan]\n{result['query']}",
        title="User Query"
    ))

    console.print(Panel.fit(
        f"[green]{result['answer']}[/green]",
        title="CIS Policy Agent Response"
    ))