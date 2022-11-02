import csv

import logging

Logger = logging.getLogger(__name__)

def convert_string_list_to_list(string_list: str):
    return string_list[1:-1].replace(' ', '').replace("'", '').split(',')


def get_all_user(csv_users):
    """
    This function should return a list of all users
    """
    with open(csv_users, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        users = [row['name'] for row in reader]
        csvfile.close()

    return users


def get_users_status(csv_users="users.csv"):
    """
    This functioninit the status of each user

    Example:
    status = {
        "toto": {
            "toto": 0, # Will be used for total amount (toto own 0 in total)
            "tata": 0, # Toto owes 0 to tata
        },
        "tata": {
            "toto": 0,
            "tata": 0,
        }
    }
    """
    users = get_all_user(csv_users)
    status = {}

    for user in users:
        status[user] = {}
        for i in users:
            status[user][i] = 0

    return status

def pretty_print_status(status):
    """
    This function should print the status of the expense report
    """
    users = get_all_user("users.csv")

    for user in users:
        for i in users:
            if user != i:
                if status[user][i] < 0:
                    Logger.info(f"{user} owes {status[user][i] * -1} to {i}")



def show_status(csv_expense_report="expense_report.csv", csv_users="users.csv"):
    """
    This function should show the status of the expense report
    """
    status = get_users_status(csv_users)
    Logger.debug(status)

    with open(csv_expense_report, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in list(reader)[1:]:

            amount = float(row[0])
            label = row[1]
            spender = row[2]
            people_involved = row[3]

            user_concerned_by_purchase = convert_string_list_to_list(people_involved)

            Logger.debug(f"User concerned by purchase: {user_concerned_by_purchase}")

            amount_per_user = float(amount) / len(user_concerned_by_purchase)

            for user in user_concerned_by_purchase:
                if user == spender:
                    for i in user_concerned_by_purchase:
                        if i != user:  # Don't add the amount to the spender
                            status[user][i] += amount_per_user
                else:
                    status[user][spender] -= amount_per_user

        csvfile.close()

    Logger.debug(f"Summary: {status}")
    pretty_print_status(status)
