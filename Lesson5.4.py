def file_search(folder, filename, path=''):
    if len(folder) > 1:
        if path != '':
            path = path + '/' + folder[0]
        else:
            path = folder[0]

        for i in folder[1:]:
            if type(i) == str:
                if i == filename:
                    return path + '/' + filename
            else:
                if len(i) > 1:
                    return file_search(i,filename,path)
    else:
        return False

print(file_search(['C:'], 'crack.exe'))
print('-- End')

print(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'))
print('-- End')

print(
    file_search(
        ['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak']], 'hey.py'], 'asd.txt'))
print('-- End')
print(file_search(['/home', ['user1'],
                   ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py']]],\
                  'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'))
print('-- End')