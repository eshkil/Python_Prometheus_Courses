import sys

result = 0
element_1 = 0
element_2 = 1

n = int(sys.argv[1])

if n<0:
    print('Error')
    exit(0)
if n ==0:
    print(0)
    exit(0)

if n == 1:
    print(1)
    exit(0)

for counter in range(n-1):
    result = element_1 + element_2
    element_1 = element_2
    element_2 = result

print(result)