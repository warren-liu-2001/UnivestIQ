import math
import matplotlib as pyplot
from access import Access
import requests

def main():
    access = Access()
    while True:
        resp = requests.get('https://todolist.example.com/tasks/')
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        for todo_item in resp.json():
            print('{} {}'.format(todo_item['id'], todo_item['summary']))


if __name__ == "__main__":
    main()

