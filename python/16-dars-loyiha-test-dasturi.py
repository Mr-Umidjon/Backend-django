import json
# from pprint import pprint as print
from tabulate import tabulate

with open('16-tests.json', 'r') as f1:
    testjs = json.load(f1)

with open('16-users.json', 'r') as f2:
    usersjs = json.load(f2)

keys = ['a', "b", "c", "d"]


def printTable(users):
    data = [user.values() for user in users]
    print(tabulate(data, headers=['Name', 'Played', "Best score"], tablefmt='orgtbl'))


printTable(usersjs)
