#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import logging
import sys
from os.path import exists as path_exists
from os.path import isfile as path_isfile

from PyInquirer import prompt

from src.expense import new_expense
from src.user import add_user
from src.show_status import show_status

sys.path.insert(0, './src')

log_format = "[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(filename)s:%(lineno)d"
logging.basicConfig(encoding='utf-8', format=log_format, level=logging.DEBUG)

Logger = logging.getLogger(__name__)

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    elif (option['main_options']) == "Show Status":
        show_status()
        ask_option()
    elif (option['main_options']) == "New User":
        add_user()
        ask_option()
    else:
        Logger.error("Option not found !")


def init_csv(csv_expense_report="expense_report.csv", csv_users="users.csv"):
    """
    This function should create the csv files if they don't exist
    """
    if not (path_exists(csv_expense_report) and path_isfile(csv_expense_report)):
        with open(csv_expense_report, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['amount','label','spender', 'People_involved'], delimiter=';')
            writer.writeheader()
            csvfile.close()

    if not (path_exists(csv_users) and path_isfile(csv_users)):
        with open(csv_users, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name'], delimiter=';')
            writer.writeheader()
            csvfile.close()


def main():
    init_csv()
    ask_option()


if __name__ == "__main__":
    main()