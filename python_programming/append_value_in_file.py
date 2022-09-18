employees = open("append_file.txt","r+")

employees.write("\n Lee - HR")

'''employee = open("append_file.txt","r")'''
'''print(employee.readlines())'''

print(employees.readlines())