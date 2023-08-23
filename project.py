import os
import csv
import re

from datetime import date
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
running = True

LINER = "=" * 15

amount_pattern = r'^\$?(\d*(\d\.?|\.\d{1,2}))$'
date_pattern = r"^\d+\-\d+\-\d+$"
description_pattern = rf"^.{{0,50}}$"
category_pattern = r"^[a-zA-Z]+$"

expenses = []

"""Startscreen"""
def main():
    load_from_csv()
    clear()
    while running:
        console.print(
            f"{LINER}\n"
            "[blue]Expense Tracker[/]\n"
            f"{LINER}\n"
            "[1] Add\n"
            "[2] Delete\n"
            "[3] Display\n"
            "[4] Edit\n"
            "[5] Exit"
        )

        action = input("Enter Option: ")
        if action == "1":
            add_expense()
        elif action == "2":
            delete_expense()
        elif action == "3":
            display_expenses()
            console.input("[yellow][italic]Press enter to go back.[/]")
        elif action == "4":
            edit_expense()
        elif action == "5":
            exit_program()
        else:
            print("Invalid key, try again.")


def add_expense():
    clear()
    console.print(
            "[cyan underline]Add An Expense[/]"
        )

    price = float(validate_input("Price: ", amount_pattern))
    date = validate_input("Date (YYYY-MM-DD): ", date_pattern)
    description = validate_input("Description (Limit of 50 Characters): ", description_pattern)
    category = validate_input("Category (One Word): ", category_pattern)

    new_expense = {
        'Price': price,
        'Date': date,
        'Description': description,
        'Category': category
    }
    expenses.append(new_expense)
    clear()
    add_to_csv()
    console.print("\n[light_green bold]Expense Added![/]\n")


def validate_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.search(pattern, user_input):
            return user_input
        print("Invalid input, try again.")


def display_expenses():
    clear()
    table = Table(title="Expense List", box=box.SIMPLE_HEAVY)
    table.add_column("Index", justify="center")
    table.add_column("Price", justify="center")
    table.add_column("Date", justify="center")
    table.add_column("Description", justify="center")
    table.add_column("Category", justify="center")

    for index, expense in enumerate(expenses):
        table.add_row(
            str(index + 1),
            str((f"${expense['Price']:,.2f}")),
            expense["Date"],
            expense["Description"],
            expense["Category"]
        )

    texpense = total_expense()
    table.add_row(
        "#",
        str((f"${texpense:,.2f}")),
        str(date.today()),
        "Total Price",
        "Total"
        )

    console.print(table)


def delete_expense():
    clear()
    display_expenses()
    while True:
        try:
            delete = int(input("Which expense would you like to delete? (Type 0 to exit.) \n")) - 1
            if 0 <= delete < len(expenses):
                del expenses[delete]
                clear()
                console.print("\n[red bold]Expense Deleted![/]\n")
                break
            if delete < 0:
                break
            else:
                console.print("[red]Invalid index, try again.[/]")
        except ValueError:
            console.print("[red]Invalid input, try again.[/]")
        finally:
            if delete == "None":
                break


def edit_expense():
    clear()
    display_expenses()
    while True:
        try:
            edit = int(input("Which expense would you like to edit? (Type 0 to exit.) \n")) - 1
            if 0 <= edit < len(expenses):
                edited_expense = expenses[edit]
                edited_expense["Price"] = float(validate_input("Price: ", amount_pattern))
                edited_expense["Date"] = validate_input("Date (YYYY-MM-DD): ", date_pattern)
                edited_expense["Description"] = validate_input("Description (Limit of 50 Characters): ", description_pattern)
                edited_expense["Category"] = validate_input("Category (One Word): ", category_pattern)
                expenses[edit] = edited_expense

                clear()
                console.print("\n[blue bold]Expense Edited![/]\n")
                break
            if edit < 0:
                break
            else:
                console.print("[red]Invalid index, try again.[/]")
        except ValueError:
            console.print("[red]Invalid input, try again.[/]")


def exit_program():
    global running
    clear()
    console.print("[red bold]Program Closed[/]")
    running = False


def load_from_csv():
    if os.path.isfile("expenses.csv") == True:
        try:
            with open("expenses.csv") as list:
                reader = csv.DictReader(list)
                for line in reader:
                    expenses.append({"Price": float(line['Price']),
                                    "Date": line['Date'],
                                    "Description": line['Description'],
                                    "Category": line['Category']})
        except:
            pass


def add_to_csv():
    try:
        with open("expenses.csv", "w", newline="") as list:
            writer = csv.DictWriter(list, fieldnames=["Price", "Date", "Description", "Category"])
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense)
    except:
        pass


def total_expense():
    texpense = 0
    for expense in expenses:
        texpense += expense["Price"]
    return texpense


def clear():
    os.system("clear")


if __name__ == "__main__":
    main()
