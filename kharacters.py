import json
import csv
from os import path, stat

new_character = {
    "name": "Hulk",
    "intelligence": 9,
    "power": 7,
    "strength": 10,
    "agility": 8
}

character_id = 1

def find_all_characters(filename):

    exist_file = path.exists(filename)
    size_file = stat(filename).st_size

    if not exist_file or size_file < 0:
        return []

    with open(filename) as file:
        chars = csv.DictReader(file)

        return [char for char in chars]
    
def find_character_by_id(filename, character_id):

    csv_chars = find_all_characters(filename)

    for char in csv_chars:
        if int(char["id"]) == character_id:
            return char
        else:
            return None

def generate_id(filename):
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        file_content = list(reader)

        if not len(file_content):
            return 1

        my_id = file_content[-1]['id']
        my_last_id = int(my_id) + 1

        return my_last_id

def create_character(filename, **kwargs):

    if not path.exists(filename):
        with open(filename, 'w') as file:
            fieldnames = ['id', 'name', 'intelligence', 'power', 'strength', 'agility']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

    my_id = generate_id(filename)

    with open(filename, 'a') as file:
        fieldnames = ['id', 'name', 'intelligence', 'power', 'strength', 'agility']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        kwargs['id'] = my_id
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(kwargs) 

        return kwargs

if __name__ == "__main__":
    
    filename = "characters.csv"

    found_character = find_all_characters(filename)
    print(found_character)

    # new_id = generate_id(filename) 
    # print(new_id) 

    found_character = find_character_by_id(filename, character_id)
    print(found_character)

    created_character = create_character(filename, **new_character)
    print(created_character)