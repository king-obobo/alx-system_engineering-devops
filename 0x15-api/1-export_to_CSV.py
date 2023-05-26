#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys
import csv

BASE_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(BASE_URL + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(BASE_URL + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
