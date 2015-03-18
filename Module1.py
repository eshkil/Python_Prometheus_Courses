import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_string = ''
result = ''
code = []
new_code = []
i = 0
position = 0

input_string = sys.argv[1]

while i < len(input_string):
    if input_string[i] != ' ': new_string = new_string + input_string[i]
    i += 1

for i in range(0,len(new_string),5): code.append(new_string[i:i+5])

for new_string in code:
    if len(new_string) == 5:
        symbol = ''
        for i in range(5):
            if new_string[i].islower(): symbol = symbol + 'a'
            else: symbol = symbol + 'b'
        result = result + alphabet[key.find(symbol)]
    else: None

print(result)

n = 100
for x in range(n):
    is_cool = x < 10 or (x / 10 == x % 10)
    print(x / 10)
    print(x % 10)
    print x, is_cool