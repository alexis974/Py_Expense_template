import csv
import logging

from PyInquirer import print_json, prompt

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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]


def new_expense(*args, csv_file="expense_report.csv"):
    infos = prompt(expense_questions)

    csv_columns = ['amount','label','spender']
    with open(csv_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writerow(infos)
        csvfile.close()

    Logger.debug(infos)
    Logger.info("Expense Added !")
    return True
