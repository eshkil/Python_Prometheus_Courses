def encode_morze(text):
    coded = ''
    morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--.."
}
    for letter in text.upper():
        if letter != ' ':
            if letter in morse_code.keys():
                if coded != '':
                    coded = coded + '_'*2
                for i in morse_code[letter]:
                    if coded != '':
                        coded = coded + '_' + coder(i)
                    else:
                        coded = coder(i)
            else:
                None
        else:
            coded = coded + coder(' ')
    return coded

def coder(sign):
    if sign == '.':
        return '^'
    elif sign == ' ':
        return '_'*4
    elif sign == '-':
        return '^'*3


#---
fraze = ''
result = encode_morze(fraze)
print(result)

if result == '^_^___^^^_^_______^_^^^_______^_^_^_^___^^^_^^^_^^^___^_^^^_^_^___^_______^_^___^^^_^_______^^^___^_^_^_^___^_______^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^_^_^^^___^^^_^___^^^_^_^_______^^^___^_^_^_^___^___^_^^^_^___^_______^_^^^_^_^___^_^___^_^_^_^^^___^___^^^_^_^_______^_^^^_______^_^_^_^___^^^_^^^_^^^___^^^_^_^_^___^^^_^_^_^___^_^___^^^':
    print('Ok')
else:
    print('Fail')
    print('^^^_^___^^^_^^^_^^^___^^^_______^_^^^_______^^^_^___^_^^^___^_^_^___^^^___^^^_^_^^^_^^^_______^^^_^_^___^_^___^_^^^_^___^^^___^^^_^_^^^_^^^_______^_^^^_^^^___^___^^^_______^_^_^_^___^^^_^^^_^^^___^_^^^_^_^___^_______^_^_^^^_^___^_^___^_^^^_^_^___^_^^^_^_^___^___^^^_^_^_______^_^^^_^^^___^_^___^^^___^_^_^_^_______^^^___^_^_^_^___^_______^___^^^_^___^^^_^_^___^_^_^_______^^^_^^^_^^^___^_^_^^^_^_______^_^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^___^_^_^_______^_^^^___^^^_^___^^^_^_^_______^_^^^___^^^_^_______^^^_^^^_^^^___^^^_^^^_^^^___^^^_^^^_^_^___^^^_^_^^^_^^^_______^_^_^___^^^_^^^___^___^_^^^_^_^___^_^^^_^_^_______^^^_^___^^^_^^^_^^^___^_^^^_^_______^^^_^_^^^_^^^___^___^^^_______^_^^^_______^^^_^_^___^_^^^_^___^^^_^_^^^_^^^_______^^^_^_^_^___^_^^^___^_^^^_^___^_______^_^_^___^_^^^___^^^_^___^^^_^_^___^^^_^_^^^_^^^_______^_^_^_^___^^^_^^^_^^^___^_^^^_^_^___^_______^_^^^_^^^___^_^___^^^___^_^_^_^_______^^^_^___^^^_^^^_^^^___^^^___^_^_^_^___^_^___^^^_^___^^^_^^^_^_______^_^___^^^_^_______^_^___^^^_______^^^___^^^_^^^_^^^_______^_^_^___^_^___^^^_______^^^_^_^___^^^_^^^_^^^___^_^^^_^^^___^^^_^_______^^^_^^^_^^^___^^^_^_______^^^_^^^_^^^___^_^^^_^_______^^^___^^^_^^^_^^^_______^___^_^^^___^^^_______^_^___^^^_______^_^^^_^^^___^_^^^___^_^_^_______^_^^^_______^_^_^_^___^^^_^^^_^^^___^^^_^_^_^___^^^_^_^_^___^_^___^^^___^_^_^_^___^^^_^^^_^^^___^_^^^_^_^___^_______^_^^^___^^^_^___^^^_^_^_______^^^___^_^_^_^___^_^^^___^^^_______^^^_^^^___^___^_^^^___^^^_^___^_^_^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^^^___^_^_^^^_^___^^^_^^^_^^^___^_^^^_^___^^^')
    print(fraze)