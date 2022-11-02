import csv

import logging

Logger = logging.getLogger(__name__)

def convert_string_list_to_list(string_list: str):
    return string_list[1:-1].replace(' ', '').replace("'", '').split(',')


def get_users_status(csv_users="users.csv"):
    """
    This functioninit the status of each user

    Example:
    status = {
        "toto": {
            "toto": 0,
            "tata": 0,
        },
        "tata": {
            "toto": 0,
            "tata": 0,
        }
    }
    """
    with open(csv_users, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        users = [row['name'] for row in reader]
        csvfile.close()

    status = {}

    for user in users:
        status[user] = {}
        for i in users:
            status[user][i] = 0

    return status


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

            Logger.debug(f"Amount: {amount}")
            Logger.debug(f"Label: {label}")
            Logger.debug(f"Spender: {spender}")
            Logger.debug(f"People involved: {people_involved}")

            user_concerned_by_purchase = convert_string_list_to_list(people_involved)

            Logger.info(f"User concerned by purchase: {user_concerned_by_purchase}")

            amount_per_user = float(amount) / len(user_concerned_by_purchase)

            for user in user_concerned_by_purchase:
                if user == spender:
                    for user in user_concerned_by_purchase:
                        if user == spender:
                            status[user][user] += amount
                else:
                    status[user][spender] -= amount_per_user
            Logger.info(f"Status: {status}")



        csvfile.close()

    Logger.info(f"Status: {status}")

    Logger.info("Status of the expense report:")