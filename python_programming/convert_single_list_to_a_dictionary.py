res_dct = {}


def Convert(lst):
    for i in range(0, len(lst), 2):
        res_dct.update({lst[i]: lst[i + 1]})
    print(res_dct)


# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
Convert(lst)
