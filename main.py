import csv
import logging

from examples import custom_style_2
from PyInquirer import prompt

from expense import expense_questions, new_expense
from user import add_user, user_questions

log_format = "[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(filename)s:%(lineno)d"
logging.basicConfig(encoding='utf-8', format=log_format, level=logging.DEBUG)

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
    elif (option['main_options']) == "New User":
        add_user()
        ask_option()

def main():
    ask_option()

main()