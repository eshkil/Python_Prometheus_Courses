import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if x <= 0 or y<=0 or z<=0:
    print('not triangle')
    exit(0)

if x>=z:
    if x>=y:
        if y + z <= x: print('not triangle')
        else: print('triangle')
else:
   if y>=z:
        if x + z <= y: print('not triangle')
        else: print('triangle')
   else:
        if x + y <= z: print('not triangle')
        else: print('triangle')