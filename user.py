import csv

from PyInquirer import prompt

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

    return