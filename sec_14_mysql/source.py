import mysql.connector
from difflib import get_close_matches
import json

data = json.load(open("../files/data.json"))

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()


def define(word):
    # query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{word}'")
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[0])
    elif len(get_close_matches(word, data.keys())) > 0:
        # yn = input("Did you mean %s instead (y/n): " % get_close_matches(w, data.keys())[0])
        yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y if yes, or N if no: ")
        if yn == "y":
            print(data[get_close_matches(word, data.keys())[0]])
        elif yn == "n":
            print("The word doesn't exist. Please double check it.")
        else:
            print("We didn't understand your entry.")
    else:
        print("No word found!")

word = input("Enter the word: ")
word = word.lower()
output = define(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

