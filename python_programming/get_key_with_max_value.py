dict_val = {'W': 2, 'X': 5, 'Y': -16, 'Z': 3}


def method_max_val():
    print('111111', dict_val.keys())
    k = list(dict_val.keys())
    print('22222222', k)
    v = list(dict_val.values())
    print('3333333', v.index(max(v)))
    return k[v.index(max(v))]


print(method_max_val())
