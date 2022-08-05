sample_dict = {14: 2, 25: 3, 32: 21, 12: 16, 11: 34}
list_keys = []
list_val = []


def max_key_val():
    for keys, values in sample_dict.items():
        list_keys.append(keys)
        list_val.append(values)
    max_key = max(list_keys)
    max_val = max(list_val)
    print('max key and value are {}:{}'.format(max_key, max_val))


max_key_val()
