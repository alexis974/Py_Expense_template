import csv
import logging

from PyInquirer import prompt

Logger = logging.getLogger(__name__)

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }

]

def add_user():
    # This function should create a new user, asking for its name
    # and store it in a csv file
    infos = prompt(user_questions)

    csv_columns = ['name']
    with open('users.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writerow(infos)
        csvfile.close()

    Logger.debug(infos)
    Logger.info("Expense Added !")

    return