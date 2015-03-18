import sys, math

x = float(sys.argv[1])
m = float(sys.argv[2])
y = float(sys.argv[3])

f1 = 1/(y*math.sqrt(2*math.pi))
f2 = -(math.pow((x-m),2)/(2*math.pow(y,2)))
f =  f1*math.exp(f2)

print(f)

result = -5

result = result + 1

print(result)
print(type(result))

if '(' == '(': result = result + 1

print(result)