def super_fibonacci(n, m):
    if n > 35: return 0
    if n < m: return 1

    list = []
    for i in range(n):
        if i < m: list.append(1)
        else: list = plus(list,m)
    list.reverse()
    return list[0]

def plus(list,count):
    new_digit_in_list = 0
    list.reverse()
    for i in range(count):
        new_digit_in_list = new_digit_in_list + list[i]
    list.reverse()
    list.append(new_digit_in_list)
    return list

print(super_fibonacci(17,2))