import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.txt', 'r') as j_f:
    # with open('person.txt', 'w') as j_f:
    # json.dump(person_dict, j_f)
    data= json.load( j_f)
    print(data)