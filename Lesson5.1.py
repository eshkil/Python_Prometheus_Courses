def clean_list(list_to_clean):
    for i in range(len(list_to_clean)):
        for j in range(i+1,len(list_to_clean)):
            if (type(list_to_clean[i]) == type(list_to_clean[j]) and list_to_clean[i] == list_to_clean[j] and list_to_clean[i] != None):
                list_to_clean[j] = None

    for i in range(list_to_clean.count(None)):
        list_to_clean.remove(None)

    return list_to_clean


clean_list([1, 1.0, '1', -1, 1])