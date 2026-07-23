import click
from rich.console import Console
from rich.table import Table
from core.expenses import addExpense, loadExpense, deleteExpense, summaryExpenses

console = Console()

@click.group()
def cli():
    pass

######
# Command for the addExpense function
######
@cli.command()

# Options for the arguments the command takes, each required because each contains prompt
@click.option('--amount', prompt='Amount', type=float, help='The amount of the expense')
@click.option('--category', prompt='Category', type=str, help='The category of the expense')
@click.option('--description', prompt='Description', type=str, help='The description of the expense')

# Add command is defined with arguments that are linked to the options, arguments autmatically find options based on "--{argument}" notation
def add(amount, category, description):
    addExpense(amount, category, description)
    console.print("Expense has been added to records!")



if __name__ == "__main__":
    cli()
