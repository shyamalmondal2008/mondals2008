my_dict = {-36: 1, 12: 2, 6: 4, 24: 2, 33: 2, 4: 1}
maxValue = []
maximum = 0
maxKey = 0
maxKeys = []

for key, value in my_dict.items():
     if value >= maximum:
          maxValue.append(value)


number = max(maxValue)

for key, value in my_dict.items():
    if key > maxKey:
         maxKeys.append(key)

number_1 = max(maxKeys)

print('{} {}'.format(number_1, number))