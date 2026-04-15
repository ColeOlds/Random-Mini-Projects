import calendar
import datetime
import json
import os

EVENTS_FILE = 'events.json'

def load_events():
    if not os.path.exists(EVENTS_FILE) or os.path.getsize(EVENTS_FILE) == 0:
        return {} # Return an empty dictionary if file doesn't exist or is empty
    with open(EVENTS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from events.json. File might be corrupted.")
            return {}

def save_events(events_data):
    with open(EVENTS_FILE, 'w') as f:
        json.dump(events_data, f, indent=2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Calendar Functions ---

def display_month(year, month, events):
    clear_screen()
    cal = calendar.Calendar()
    
    print(f"\n--- {datetime.date(year, month, 1).strftime('%B %Y')} ---")
    print("Mo Tu We Th Fr Sa Su") # Header for days of the week

    for week in cal.monthdayscalendar(year, month):
        week_str = ""
        for day in week:
            if day == 0: # Day is 0 if it's a padding day from prev/next month
                week_str += "   "
            else:
                date_str = f"{year}-{month:02d}-{day:02d}"
                # Check if there are events for this date
                if events.get(date_str):
                    week_str += f"{day:2d}*" # Mark with an asterisk
                else:
                    week_str += f"{day:2d} "
                week_str += " " # Add space between days
        print(week_str.strip())
    print("----------------------------\n")

def add_event(events):
    clear_screen()
    print("\n--- Add New Event ---")
    while True:
        date_input = input("Enter date (YYYY-MM-DD), or 'q' to cancel: ").strip()
        if date_input.lower() == 'q':
            print("Event creation cancelled.")
            return

        try:
            # Validate date format and if it's a real date
            datetime.datetime.strptime(date_input, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    description = input("Enter event description: ").strip()
    if not description:
        print("Event description cannot be empty. Event not added.")
        return

    # Initialize the date's list of events if it doesn't exist
    if date_input not in events:
        events[date_input] = []
    
    events[date_input].append(description)
    save_events(events)
    print(f"\nEvent added for {date_input}: '{description}'")
    input("Press Enter to continue...")

def view_events(events):
    clear_screen()
    print("\n--- View Events ---")
    view_type = input("View events for a specific date (D) or all events (A)? (D/A): ").strip().lower()

    if view_type == 'd':
        while True:
            date_input = input("Enter date (YYYY-MM-DD) to view events, or 'q' to cancel: ").strip()
            if date_input.lower() == 'q':
                return
            try:
                datetime.datetime.strptime(date_input, '%Y-%m-%d')
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        print(f"\nEvents for {date_input}:")
        if date_input in events and events[date_input]:
            for i, event_desc in enumerate(events[date_input]):
                print(f"- {event_desc}")
        else:
            print("No events for this date.")
    
    elif view_type == 'a':
        print("\n--- All Stored Events ---")
        if not events:
            print("No events stored yet.")
        else:
            # Sort dates for better readability
            sorted_dates = sorted(events.keys())
            for date_str in sorted_dates:
                if events[date_str]: # Only print if there are events for the date
                    print(f"\n{date_str}:")
                    for i, event_desc in enumerate(events[date_str]):
                        print(f"  - {event_desc}")
        print("---------------------------")
    else:
        print("Invalid choice. Returning to main menu.")

    input("\nPress Enter to continue...")

def main():
    events = load_events()
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    while True:
        display_month(current_year, current_month, events)
        print("--- Calendar Menu ---")
        print(f"Current View: {datetime.date(current_year, current_month, 1).strftime('%B %Y')}")
        print("1. Previous Month")
        print("2. Next Month")
        print("3. Go to Specific Month/Year")
        print("4. Add Event")
        print("5. View Events")
        print("6. Exit")
        print("---------------------")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            current_month -= 1
            if current_month < 1:
                current_month = 12
                current_year -= 1
        elif choice == '2':
            current_month += 1
            if current_month > 12:
                current_month = 1
                current_year += 1
        elif choice == '3':
            while True:
                try:
                    new_year = int(input("Enter year (e.g., 2025): ").strip())
                    new_month = int(input("Enter month (1-12): ").strip())
                    if 1 <= new_month <= 12 and new_year > 0: # Basic validation
                        current_year = new_year
                        current_month = new_month
                        break
                    else:
                        print("Invalid month or year.")
                except ValueError:
                    print("Invalid input. Please enter numbers.")
            
        elif choice == '4':
            add_event(events)
        elif choice == '5':
            view_events(events)
        elif choice == '6':
            print("Exiting Calendar. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
