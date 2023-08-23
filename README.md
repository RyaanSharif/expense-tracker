# Expense-Tracker
Beginner project where I can track expenses and saves all previous expenses to a csv file.

# Libraries
os
csv
re
datetime
rich.console
rich.table
rich

# Functioning
main(): 
contains the startscreen and all the functions of adding, deleting, editing, displaying the expenses
can also choose to load all previous expenses or not

add_expense(): 
adds an expense by prompting the user for a price, date, description, and category before adding it to the expenses list as a dict

validate_input():
checks every input for add_expense to ensure that it fits in the category

display_expenses():
displays the expenses in a table by enumerating the expenses list and looping through each index 
also displays the total cost of the list at the bottom

delete_expense():
prints the display and finds the index that should be deleted

edit_expense():
prints the display and finds the index that should be edited before editing through the validate_input() function

exit_program():
will exit the program

load_from_csv():
will load all previous expenses from a csv file if it exists

add_to_csv():
will add all expenses to the csv file "expenses.csv"

clear():
clears the screen

# Author
Ryaan Sharif
