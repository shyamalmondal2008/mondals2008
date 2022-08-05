# T = [2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18]
T = [2, -3, 3, 1, 10, -8, 2, 5]
l = len(T)
res = int(l / 4)

total = 0
temp_val_list = []
season_list = ['WINTER', 'SPRING', 'SUMMER', 'AUTUMN']

def solution(T):
    temp_val_list.append(sum(T[0:res]))
    temp_val_list.append(sum(T[res:res * 2]))
    temp_val_list.append(sum(T[res * 2:res * 3]))
    temp_val_list.append(sum(T[res * 3:res * 4]))
    print(season_list[temp_val_list.index(max(temp_val_list))])
    print(season_list[temp_val_list.index(max(temp_val_list))])


solution(T)
