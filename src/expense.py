import csv
import logging

from PyInquirer import prompt, Separator
from examples import custom_style_2

Logger = logging.getLogger(__name__)

expense_questions_part_one = [
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
    }
]

expense_questions_part_two = [
    {
        "type":"checkbox",
        "name":"People involved",
        "message":"New Expense - People involved: ",
        "choices": []
    }
]


def get_questions_part_two(users: list, spender: str):
    expense_questions_part_two[0]['choices'] = [] # Reset choices
    for user in users:
        dict_of_user = {'name': user, 'checked': user == spender}
        expense_questions_part_two[0]['choices'].append(dict_of_user)
    return expense_questions_part_two


def get_possible_spender(csv_users):
    with open(csv_users, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        users = [row['name'] for row in reader]
        csvfile.close()
    return users


def new_expense(csv_expense_report="expense_report.csv", csv_users="users.csv"):

    users = get_possible_spender(csv_users)

    if len(users) == 0:
        Logger.error("No user found ! Can't add expense. You must first add at least one user")
        return

    expense_questions_part_one[2]['choices'] = users # Possible Spender
    infos_part_one = prompt(expense_questions_part_one)

    expense_questions_part_two = get_questions_part_two(users, infos_part_one['spender'])
    infos_part_two = prompt(expense_questions_part_two, style=custom_style_2)
    infos_part_one['People_involved'] = infos_part_two['People involved'] # Add People involved to infos_part_one

    if len(infos_part_one['People_involved']) == 0:
        Logger.error("No people involved ! Can't add expense.")
        return

    csv_columns = ['amount','label','spender', 'People_involved']
    with open(csv_expense_report, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writerow(infos_part_one)
        csvfile.close()

    Logger.info(f"{infos_part_one['spender']} spend {infos_part_one['amount']} money point for {infos_part_one['People_involved']}!")
    return True
