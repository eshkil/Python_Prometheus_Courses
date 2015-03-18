import sys

count = 0

x = str(sys.argv[1])
y = str(sys.argv[2])

z = range(int(x),int(y)+1)

for i in z:
    i = str(i)
    if len(i)<6: j = '0'*(6-len(i)) + i
    else: j = i
    if int(j[0])+int(j[1])+int(j[2]) == int(j[3])+int(j[4])+int(j[5]):
        count = count + 1

print(count)
