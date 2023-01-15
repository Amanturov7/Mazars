import json
import random



def readAll():
    with open('Laptops.json') as f:
        templates = json.load(f)

    for section, commands in templates.items():
        print(section)
        print('\n'.join(map(str, commands)) + '\n')
        return templates

def read(id):
    with open('Laptops.json') as f:
        templates = json.load(f)

    print(templates)

    for section, commands in templates.items():
        if (section == id):
            return commands


def create(name, description, price):
    id = random.randint(0, 10000)

    if (description == None):
        description = 'No Description'

    write = [id, name, description, price]
    data = json.load(open("Laptops.json"))
    data[id]=write
    with open("Laptops.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def update(id, name, description, price):
    with open('Laptops.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)

    for section, commands in templates.items():

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
    with open('Laptops.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)
        templates.pop(id,None)
    to_json = templates
    with open('Laptops.json', 'w') as f:
        json.dump(to_json, f, sort_keys=True, indent=2)
