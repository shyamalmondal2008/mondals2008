import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.json', 'r') as j_f:
    data= json.load( j_f)
    print(data)

with open('person.txt', 'w') as j_w:
    json.dump(person_dict, j_w)