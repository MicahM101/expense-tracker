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

#######
# Command for the loadExpense function
#######

@cli.command()
# Line of code creating a table command
def list():
    # Code initializing the Expense Table
    table = Table(title="List of Expenses")

    # Code to add columns 
    table.add_column("ID")
    table.add_column("Date")
    table.add_column("Amount")
    table.add_column("Category")
    table.add_column("Description")

    # Populating the expense list
    expenseList = loadExpense()

    # Code removing the first line of the CSV from its list
    expenseList = expenseList[1:]

    # Check for if the list is empty
    if not expenseList:
        console.print("No expense found!")
        return

    # Loop adding the rows of the CSV into the command line rich table; Each row is split into its elements to 
    # match the table's columns
    for row in expenseList:
        table.add_row(row[0], row[1], row[2], row[3], row[4])

    console.print(table)


#######
# Command for the delete expenses function
#######

@cli.command()

# Options for the arguments needed for the function
@click.option('--id', prompt='id', type=int, help='The ID of the expense you would like to delete')

def delete(id):
    # Return message for if the file is found and deleted and if it isn't
    if deleteExpense(id):
        console.print("The expense was deleted from file")
    else:
        console.print("This expense ID was not found on file, hence, it was not deleted.")


######
# Command for the summary expenses function
######

@cli.command()
# Function for the delete function
def summary():

    # Creating a table for summary expenses
    etable = Table(title=("Expense Summary"))

    # Code to add columns to the table
    etable.add_column("Category")
    etable.add_column("Spend")

    # Creating a loop to add rows to the table from the dictionary
    summary_dict = summaryExpenses()

    # Empty check
    if not summary_dict:
        print("No expenses found for summary")
        return

    for key in summary_dict:
        etable.add_row(key, str(summary_dict[key]))

    console.print(etable)


if __name__ == "__main__":
    cli()
