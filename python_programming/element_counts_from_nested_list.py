list_c = [1, 2, [8, "abc", [9, "hello", 100]], 4, [6, [9, "good day", 436]]]


def get_element_count_nested_list(list_c):
    count = 0
    for element in list_c:
        if type(element) == list:
            count += get_element_count_nested_list(element)
        else:
            count += 1
    return count


if __name__ == "__main__":
    print(get_element_count_nested_list(list_c))
