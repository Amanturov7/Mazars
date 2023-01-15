import json
import random

from pydantic.main import BaseModel


def readAll():
    #open file
    with open('Laptops.json') as f:
        templates = json.load(f)

    #iterate over the list using items()
    for section, commands in templates.items():
        print(section)
        print('\n'.join(map(str, commands)) + '\n')

        #return all of list
        return templates

def readItem(id):

    # open file
    with open('Laptops.json') as f:
        templates = json.load(f)

        # iterate over the list using items()
    for section, commands in templates.items():
        #we return the necessary Id
        if (section == id):
            return commands


def create(name, description, price):

    #generator random and uniquie id value
    id = random.randint(0, 10000)
    #optional field Description
    if (description == None):
        description = 'No Description'

    #put the list as value and the key will be itself ID
    write = [id, name, description, price]
    data = json.load(open("Laptops.json"))
    # dict= {id:write}
    data[id]=write

    #write file
    with open("Laptops.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def update(id, name, description, price):

    #open file
    with open('Laptops.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)

    #if we find necessary id of dict
    for section, commands in templates.items():

        #fields: name, description, price are optional fields, and we truth check and change value
        if (section == id):
            if name is not None:
                commands[1] = name
            if description is not None:
                commands[2] = description
            if price is not None:
                commands[3] = price
    to_json = templates
    with open('Laptops.json', 'w') as f:
        json.dump(to_json, f, sort_keys=True, indent=2)


def delete(id):
    #open file
    with open('Laptops.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)

        #delete by key
        templates.pop(id,None)
    to_json = templates
    with open('Laptops.json', 'w') as f:
        json.dump(to_json, f, sort_keys=True, indent=2)
