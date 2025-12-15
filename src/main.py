from rich.console import Console
from rich.table import Table
from data import export_csv
from tracker import add_entry, delete_entry, edit_entry, walk_by_id, walks_by_id
from analysis import show_totals, show_stats, show_averages, show_comparison, show_maxes
from visualization import plot_trend, weekly_steps, monthly_steps, weekly_distance, monthly_distance
from constants import CATEGORIES
from validation import validate_choice

console = Console()

def show_cmds(): # Function that returns a list of all commands, formatted in a Rich table
    
    table = Table(title="Command List", show_lines=True)
    table.add_column("Command", style="bright_cyan", no_wrap=True)
    table.add_column("Category", style="bright_green")
    table.add_column("Description", style="bright_yellow")

    for key, (description, category, _) in commands.items():
        table.add_row(key, category, description)

    console.print(table)
    
def show_category_cmds(): # Function that prints a list of commands from a chosen category, formatted in a Rich table
    
    chosen_category = str(input(f"Enter the category to display the commands for: {CATEGORIES} "))
    chosen_category = validate_choice(chosen_category, CATEGORIES) # Validating the inputted category against valid categories
    if chosen_category == None:
        print(f"Invalid category. Please retry and choose from {CATEGORIES} ")
        return
    
    table = Table(title=f"{chosen_category.capitalize()} Command List", show_lines=True)
    table.add_column("Command", style="bright_cyan", no_wrap=True)
    table.add_column("Description", style="bright_yellow")
    
    for key, (description, category, _) in commands.items():
        if chosen_category == category:
            table.add_row(key, description)

    console.print(table)

commands = { # List of commands, along with their description, category and attacthed function
        "add": ("Add an entry", "data", add_entry),
        "delete": ("Delete an entry", "data", delete_entry),
        "edit": ("Edit an entry", "data", edit_entry),
        "show": ("Show a walk by its ID", "data", walk_by_id),
        "list": ("Show a list of all your walks and their IDs", "data", walks_by_id),
        "export csv": ("Export your walk data as a csv file", "data", export_csv),
        "total stats": ("Show your total walk stats", "stats", show_totals),
        "average stats": ("Show your average walk stats across a timeframe", "stats", show_averages),
        "max stats": ("Show your max walk stats", "stats", show_maxes),
        "date stats": ("Show the walk stats from a specific day", "stats", show_stats),
        "compare stats": ("Show the comparison between walk stats across two different timeframes", "stats", show_comparison),
        "plot trend": ("Plot a trend of a specified walk stat", "stats", plot_trend),
        "weekly steps": ("Plot a bar chart showing your weekly total steps", "stats", weekly_steps),
        "monthly steps": ("Plot a bar chart showing your monthly total steps", "stats", monthly_steps),
        "weekly distance": ("Plot a bar chart showing your weekly total distance", "stats", weekly_distance),
        "monthly distance": ("Plot a bar chart showing your monthly total distance", "stats", monthly_distance),
        "cmds": ("Show a list of all available commands", "misc", show_cmds),
        "category cmds": ("Show all commands belonging to a specific category", "misc", show_category_cmds),
        "quit": ("Quit :[", "misc", None)
    }
    
def main():
    console.print("[green]Hi! Welcome to walk tracker :] [/green]")
    console.print("Type [bold]cmds[/bold] to see a list of all commands and get started.")
    while True:
        choice = input("> ").strip()
        
        if choice not in commands:
            console.print("[red]Invalid choice. Please try again.[/red]")
            continue
        if choice == "quit":
            print("Bye!")
            break
        
        _, _, func = commands[choice] # Run the function attatched to the user's choice
        func()
        
if __name__ == "__main__":
    main()