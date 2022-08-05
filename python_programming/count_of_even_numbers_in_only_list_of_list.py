list_c = [[9, 7, 100], [9, 111, 436]]


def even_numbers_count(list):
    count = 0
    for i in list:
        for j in i:
            if j % 2 == 0:
                count += 1
    return count


print(even_numbers_count(list_c))
