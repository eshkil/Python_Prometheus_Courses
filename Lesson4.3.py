import sys

result = 0

znaki = str(sys.argv[1])

if znaki != '' and znaki[0] != ')':
    for i in znaki:
        if i == '(': result = result + 1
        else: result = result - 1
else:
    if znaki[0] == ')': result = -1
    else: result = 0

if result == 0: print('YES')
else: print('NO')