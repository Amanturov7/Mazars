# import json
#
#
# def write(id,name,description,price):
#
#
# def update(id,name,description,price):
#     with open('text.json') as json_file:
#         data = json.load(json_file)
#         for p in data['Computers']:
#             if p['id']== id:
#                 p['name']=name
#                 p['description'] = description
#                 p['price'] = price
#                 with open('text.json', 'w') as outfile:
#                     json.dump(data, outfile)
#
# def read():
#
#     with open('text.json', 'r', encoding='utf-8') as f:
#
#         text = json.load(f)
#         return text
#
# def delete(id):
#     with open('text.json') as json_file:
#         data = json.load(json_file)
#         for p in data['Computers']:
#             if p['id']== id:
#                 p.pop('id'),
#                 p.pop('name'),
#                 p.pop('description'),
#                 p.pop('price')
#                 with open('text.json', 'w') as outfile:
#                     json.dump(data, outfile)