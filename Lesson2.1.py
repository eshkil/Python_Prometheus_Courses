import sys
x = int(sys.argv[1])
y =int(sys.argv[2])
z = int(sys.argv[3])
txt = 'Everybody sing a song:'
kuplet = ' la-la'
if z == 1: znak = '!'
else: znak = '.'
song = txt + kuplet*y + znak
exit(song)