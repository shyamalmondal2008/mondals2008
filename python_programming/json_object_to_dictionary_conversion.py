import json

person = '{"name": "Bob", "languages": ["English", "Bengali"]}'   # json
student = {"name": "John", "languages": ["French", "Spanish"]}    # dictionary


def json_func(input_parm):
    global key, value
    person_dict = json.loads(person)
    print(person_dict)
    print(person_dict['languages'])

    for key, value in person_dict.items():
        print(key, value)
    return value


json_func("name")
