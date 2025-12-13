from rich.console import Console
from rich.table import Table
from tracker import add_entry, delete_entry, edit_entry, walk_by_id, walks_by_id
from analysis import show_totals, show_stats, show_averages, show_comparison, show_maxes
from visualization import plot_trend
from constants import CATEGORIES
from validation import validate_choice

console = Console()

def show_cmds():
    table = Table(title="Command List", show_lines=True)
    table.add_column("Command", style="bright_cyan", no_wrap=True)
    table.add_column("Category", style="bright_green")
    table.add_column("Description", style="bright_yellow")

    for key, (description, category, _) in commands.items():
        table.add_row(key, category, description)

    console.print(table)
    
def show_category_cmds():
    chosen_category = str(input(f"Enter the category to display the commands for: {CATEGORIES} "))
    chosen_category = validate_choice(chosen_category, CATEGORIES)
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

commands = {
        "add": ("Add an entry", "data", add_entry),
        "delete": ("Delete an entry", "data", delete_entry),
        "edit": ("Edit an entry", "data", edit_entry),
        "show": ("Show a walk by its ID", "data", walk_by_id),
        "list": ("Show a list of all walks and their IDs", "data", walks_by_id),
        "total stats": ("Show your total stats", "stats", show_totals),
        "date stats": ("Show your stats from a specific day", "stats", show_stats),
        "average stats": ("Show your averages across a timeframe", "stats", show_averages),
        "compare stats": ("Show a comparison between stats", "stats", show_comparison),
        "plot stat": ("Plot a trend of a specified stat", "stats", plot_trend),
        "max stats": ("Show your max stats", "stats", show_maxes),
        "cmds": ("Help", "misc", show_cmds),
        "category cmds": ("SHow all commands belonging to a specific category", "misc", show_category_cmds),
        "quit": ("Quit", "misc", None)
    }
    
def main():
    
    while True:
        
        choice = input("> ").strip()
        
        if choice not in commands:
            print("[red]Invalid choice. Please try again.[/red]")
            continue
        
        if choice == "quit":
            print("Bye!")
            break
        
        _, _, func = commands[choice] # Run the function attatched to the user's choice
        func()
        
if __name__ == "__main__":
    main()