import csv
import logging

from PyInquirer import prompt

Logger = logging.getLogger(__name__)

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": []
    },

]


def new_expense(*args, csv_expense_report="expense_report.csv", csv_users="users.csv"):

    with open(csv_users, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        users = [row['name'] for row in reader]
        csvfile.close()

    if len(users) == 0:
        Logger.error("No user found ! Can't add expense. You must first add at least one user")
        return

    Logger.debug(f"List of users: {users}")

    expense_questions[2]['choices'] = users

    infos = prompt(expense_questions)

    csv_columns = ['amount','label','spender']
    with open(csv_expense_report, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writerow(infos)
        csvfile.close()

    Logger.debug(infos)
    Logger.info("Expense Added !")
    return True
