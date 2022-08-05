lst = [1, 3, 5, 4, 6, 8, 2, 7, 9, 12, 10, 4]
sub_list = []
# print([lst[i:i + 3] for i in range(0, len(lst), 3)])
num_of_ele_in_each_list = int(len(lst) / 4)
for i in range(0, len(lst), num_of_ele_in_each_list):
    print('iteration.....', i)
    print('each sublist is', lst[i:i + num_of_ele_in_each_list])
    sub_list.append(sum(lst[i:i + num_of_ele_in_each_list]))

print(sub_list)
if sub_list.index(max(sub_list)) == 0:
    print("WINTER")
elif sub_list.index(max(sub_list)) == 1:
    print("SPRING")
elif sub_list.index(max(sub_list)) == 2:
    print("SUMMER")
else:
    print("AUTUMN")
