from tracker import add_entry
from analysis import show_totals, show_stats, show_averages, show_comparison
from visualization import plot_trend

def main():
    menu_options = {
        "1": ("Add an entry", add_entry),
        "2": ("Show your total stats", show_totals),
        "3": ("Show your stats from a specific day", show_stats),
        "4": ("Show your averages across a timeframe", show_averages),
        "5": ("Show a comparison between stats", show_comparison),
        "6": ("Plot a trend of a specified stat", plot_trend),
        "7": ("Quit", None)
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