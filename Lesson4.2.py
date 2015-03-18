import sys

reverse_line = ''

for i in sys.argv[1:]:
    if reverse_line == '': reverse_line = i + reverse_line
    else: reverse_line = i + ' ' + reverse_line

print(reverse_line)