#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import json
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(BASE_URL + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(BASE_URL + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
