from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=11, y=22)
dict_color={'x':100,'y':200}

print('x=',p.x ,'y=',p.y)
print(dict_color['y'])

