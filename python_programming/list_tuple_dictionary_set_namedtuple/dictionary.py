student = {'name':'john', 'address':'helsinki','sub':['Math','Physics']}

print(student['sub'])
print(student['name'])

# get always returns something instead of error

print(student.get('address'))
print(student.get('phone'))

# If don't found returns not found
print(student.get('phone', 'not found'))

student['phone'] = '4444-2222'
student['name'] = 'bob'   # dictionary will be updated

print(student)

student.update({'name':'janne','age':'35'})
print(student)

del student['age']  # or age = student.pop('age')
print(student)

keys = student.keys()
print(keys)
values = student.values()
print(values)
items = student.items()
print(items)

for key,value in student.items():
    print(key,value)
