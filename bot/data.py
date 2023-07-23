import json
import time

print("READY!")

def save_data(item):
    with open("db_copy.json", "w") as outfile:
        json.dump(item, outfile)

def check_json_file(path):
    try:
        with open(path, 'r') as file:
            previous_data = json.load(file)
    except FileNotFoundError:
        previous_data = []
    
    while True:
        with open(path, 'r') as file:
            current_data = json.load(file)
        
        if current_data != previous_data:
            print("JSON data has changed:")
            for item in current_data:
                if item not in previous_data:
                    save_data(item)
                    print(item)
            previous_data = current_data
        
        time.sleep(1)

db_path = "../database.json"
check_json_file(db_path)