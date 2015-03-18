def counter(a,b):
    result = 0

    new_a = sort(a)
    new_b = sort(b)

    for i in new_a:
        if new_b.count(i) > 0: result +=1
    return result

def sort(input):
    list_new = []
    list_in = list(str(input))
    for i in list_in:
        if list_in.count(i) >= 1 and list_new.count(i) != 1: list_new.append(i)
    return list_new

print(counter(123, 45))