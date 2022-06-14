T = [2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18]
l = len(T)
res = int(l / 4)

total = 0
new_list = []


def solution(T):
    for i in range(len(T)):
        if i <= res:
            T[0:res]

    for i in range(len(T)):
        if res < i <= res * 2:
            T[res:res * 2]

    for i in range(len(T)):
        if res * 2 < i <= res * 3:
            T[res * 2:res * 3]

    for i in range(len(T)):
        if res * 3 < i <= res * 4:
            T[res * 3:res * 4]



print('new list is', T[0:res])
print('sum new list is', sum(T[0:res]))
print('2  new list is', T[res:res * 2])
print('2  sum new list is', sum(T[res:res * 2]))
print('3  new list is', T[res * 2:res * 3])
print('3  sum new list is', sum(T[res * 2:res * 3]))
print('4  new list is', T[res * 3:res * 4])
print('4  sum new list is', sum(T[res * 3:res * 4]))

print(solution(T))
