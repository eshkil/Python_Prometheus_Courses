import sys

i = j = 0
newstring = reverse_string = ''

string = sys.argv[1].lower()

for i in string:
    if i != ' ':
        newstring = newstring + i
        reverse_string = i + reverse_string

if newstring == reverse_string: print 'YES'
else: print('NO')