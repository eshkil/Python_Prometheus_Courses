def  find_most_frequent(text):
    result = []
    new_text = ''
    dict = {}
    text = text.lower()
    for i in text:
        if i in ["'",',','.',':',';','!','?','-']:
           new_text = new_text + ' '
        else:
            new_text = new_text + i
    list = new_text.split(' ')
    for i in list:
        if i != '':
            dict[i] = list.count(i)
    for i in dict.keys():
        if dict.get(i) == max(dict.values()):
            result.append(i)
    return result

print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))