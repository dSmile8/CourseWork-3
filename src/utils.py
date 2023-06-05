import json

from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data, filter_empty_from=False):
    data = [x for x in data if "state" in x and x["state"] == "EXCUTED"]
    if filter_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data