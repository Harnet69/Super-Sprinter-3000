import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_data_from_file():
    try:
        with open(DATA_FILE_PATH, newline='') as f:
            user_data = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            stories_list = []
            for item in user_data:
                stories_list.append(item)
            return stories_list
    except FileNotFoundError as e:
        print(e)


def write_data_to_file(user_data, write_one_row='True'):
    try:
        if write_one_row:
            with open(DATA_FILE_PATH, 'a') as f:
                schedule_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                schedule_writer.writerow(user_data)
        else:
            with open(DATA_FILE_PATH, 'w') as f:
                schedule_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                schedule_writer.writerows(user_data)
    except FileNotFoundError as e:
        print(e)


def get_all_user_story():
    get_data_from_file()
