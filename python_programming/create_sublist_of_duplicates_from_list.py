A = [1, 3, 5, 4, 6, 8, 2, 7, 9, 12, 10, 4]


def make_sublists(main_list):
    l = []
    for s in main_list:
        if main_list.count(s) > 1:
           l.append(s)
    return l


print(make_sublists(A))
