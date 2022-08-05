A = [1, 3, 5, 4, 6, 8, 2, 7, 9, 12, 10, 4]


def list_divided_equal_parts(A):
    n = len(A)
    each_part_len = int(n / 4)
    new_list = []
    for i in A:
        new_list.append(i)
        if len(new_list) == each_part_len:
            print(new_list[0:each_part_len])
        elif each_part_len < len(new_list) == each_part_len*2:
            print(new_list[each_part_len:each_part_len*2])
        elif each_part_len*2 < len(new_list) == each_part_len*3:
            print(new_list[each_part_len*2:each_part_len*3])
        elif each_part_len*3 < len(new_list) == each_part_len*4:
            print(new_list[each_part_len * 3:each_part_len * 4])
    k=0
    while k < len(A):
        print('Other way of solving by skipping element', A[k])
        k += each_part_len
        break


list_divided_equal_parts(A)
