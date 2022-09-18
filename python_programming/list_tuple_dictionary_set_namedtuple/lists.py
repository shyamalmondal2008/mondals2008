courses = ['math', 'physics', 'computersci', 'history']
courses_2 = ['geometry', 'phychology']
nums = [4, 6, 2, 3, 1, 12]

print(courses[2])
print(courses[2:])

courses.append('drawing')
print('new list is', courses)

courses.insert(0, 'geography')
print('new list with defining indexes', courses)

courses.extend(courses_2)  # courses.append(courses_2)  for appended list directly

print('appended list for individual items', courses)

courses.remove('history')
print('list after removing values', courses)

popped = courses.pop()  # to remove the last values
print('popped values', popped)
print('after removing the last values', courses)

courses.reverse()
print('list after reverse list', courses)

courses.sort()
print('list after sorting', courses)

courses.sort(reverse=True)
print('list after reverse sorting', courses)

sorted_courses = sorted(courses)
print('sorted version of the list', sorted_courses)

print('minimum number of the list', min(nums))
print('maximum number of the list', max(nums))
print('summation of the numbers of the list', sum(nums))
print('Art' in courses)

for item in courses:
    print(item)

for index,course in enumerate(courses,start=1):
    print(index,course)

course_str=' - '.join(courses)
print(course_str)

new_str = course_str.split(' - ')
print(new_str)


