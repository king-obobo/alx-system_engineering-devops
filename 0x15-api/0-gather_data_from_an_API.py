#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get(BASE_URL + "users/{}".format(id)).json()
    todos = requests.get(BASE_URL + "todos", params={"userId": id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print(f"Employee {user.get('name')} is done with tasks {len(completed)}/{len(todos)}:")
    [print("\t {}".format(c)) for c in completed]
