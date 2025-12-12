from tracker import add_entry, delete_entry, edit_entry, walk_by_id, walks_by_id
from analysis import show_totals, show_stats, show_averages, show_comparison, show_maxes
from visualization import plot_trend

def main():
    menu_options = {
        "1": ("Add an entry", add_entry),
        "2": ("Delete an entry", delete_entry),
        "3": ("Edit an entry", edit_entry),
        "4": ("Show a walk by its ID", walk_by_id),
        "5": ("Show a list of all walks and their IDs", walks_by_id),
        "6": ("Show your total stats", show_totals),
        "7": ("Show your stats from a specific day", show_stats),
        "8": ("Show your averages across a timeframe", show_averages),
        "9": ("Show a comparison between stats", show_comparison),
        "10": ("Plot a trend of a specified stat", plot_trend),
        "11": ("Show your max stats", show_maxes),
        "12": ("Quit", None)
    }
    
    while True:
        print("\nChoose an option:")
        for key, (description, _) in menu_options.items():
            print(f"[{key}] {description}")
        
        choice = input("Enter your choice: ").strip()
        
        if choice not in menu_options:
            print("Invalid choice. Please try again.")
            continue
        
        if choice == "7":
            print("Bye!")
            break
        
        _, func = menu_options[choice] # Run the function attatched to the user's choice
        func()

if __name__ == "__main__":
    main()