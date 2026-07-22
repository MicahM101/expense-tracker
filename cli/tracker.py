import click
from rich.console import Console
from rich.table import Table
from core.expenses import addExpense, loadExpense, deleteExpense, summaryExpenses

console = Console()

@click.group()
def cli():
    pass

if __name__ == "__main__":
    cli()

@click.command()
@click.option('--amount', prompt='Amount', type=float, help='The amount of the expense')

