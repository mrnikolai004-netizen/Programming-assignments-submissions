import datetime
import os
from unicodedata import category

# Define the global filename constant
FILENAME = "personal_expenses.txt"

def build_record(description, amount, category):
    """Takes expense details and returns a single comma-separated string."""
    #1. Get todays's date convert to a string
    Date_str = str(datetime.date.today())
    #2. Slice the description to a maximum of 30 characters
    sliced_description = description[:30]
    #3. Format the amount to exactly 2 decimal places
    formatted_amount = f"{amount:.2f}"
    #4. Use ",".join() to combine the four fields
    record_fields = [Date_str, sliced_description, formatted_amount, category]
    record_line = ",".join(record_fields)
    return record_line

def load_records(filename):
    """Reads saved expenses from a file and returns them as a list of lists."""
    records = []
    
    # Use try/except to catch a FileNotFoundError safely
    try:
        with open(filename, "r") as file:
            for line in file:
                # Strip whitespace and skip empty lines
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                
                # Split each line on commas to produce a list of fields
                fields = cleaned_line.split(",")
                records.append(fields)
    except FileNotFoundError:
        # If the file does not exist, return an empty list instead of crashing
            return []
        
    return records

def display_records(records):
    """Prints all expense records in a clean, readable aligned format."""
    print("\n===== Expense Records =====")
    
    # If the recods lists is empty, print a friendly message
    if not records:
        print("No expenses on record yet.")
        return
    
    # Define f-string format specifiers for fixed column widths
    # Date (12 chars), Description (32 Chars), Amount (12 chars), Category (15 chars)
    header_fmt = "{:<12} {:<32} {:<12} {:<15}"
    row_fmt = "{:<12} {:<32} {:<12} {:<15}"
    
    # Print a header row with column labels
    print(header_fmt.format("Date", "Description", "Amount", "Category"))
    
    # Print a separator line beneath the header
    print("-" * 75)
    
    # Loop through and print each record's fields
    for record in records:
        # Ensure the record has all 4 expected fields before printing
        if len(record) == 4:
            date, desc, amt, cat = record
            print(row_fmt.format(date, desc, amt, cat))
                                 
# ========================================================== 
# Main Program 
# ==========================================================
if __name__ == "__main__":
    #1. Load existing records
    current_records = load_records(FILENAME)
    
    #2. Display current records
    display_records(current_records)
    
    #3. Ask the user how many new expenses they want to add
    try:
        num_expenses = int(input("\nHow many expenses do you want to add? "))
    except ValueError:
        print("Invalid input. Please enter a whole number next time.")
        num_expenses = 0
    
    #4. Loop to collect entries
    for i in range(num_expenses):
        print(f"\n--- Expenses {i + 1} ---")
        description = input("Description: ")
        
        # Simple error handling for user amount input
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid price format. Defaulting to 0.00")
            amount = 0.0
        
        category = input("Category: ")
        
        #5. Call build_record and write to file in append mode
        formatted_line = build_record(description, amount, category)
        
        with open(FILENAME, "a") as file:
            file.write(formatted_line + "\n")
            
        #6. Load and display all records again to show updated list
        updated_records = load_records(FILENAME)
        print("\n===== Updated Expense Records =====")
        display_records(updated_records)
       
        