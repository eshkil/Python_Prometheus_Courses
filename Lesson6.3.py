def saddle_point(matrix):
    result = []
    for row in matrix:
        new_list = []
        min_no = row.index(min(row))
        min_digit = min(row)
        if row.count(min_digit) == 1:
            for col in range(len(matrix)):
                new_list.append(matrix[col][min_no])
            if max(new_list) == min_digit:
                result.append(new_list.index(max(new_list)))
                result.append(min_no)
    if len(result) == 0 or len(result) > 2:
        return False
    elif len(result) == 2:
        return tuple(result)

#---
if saddle_point([[13]]) == (0, 0):
    print('Ok')
else:
    print('bad')

if saddle_point([[0,0,0],[2,1,2],[1,0,1]]) == (1, 1):
    print('Ok')
else:
    print('bad')

if saddle_point([[5,5,5], [5,5,6], [5,4,5]]) == False:
    print('Ok')
else:
    print('bad')

if saddle_point([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]) == (9,9):
    print('Ok')
else:
    print('bad')

if saddle_point([[1,2,3,0,1,1], [4,3,2,1,1,2], [4,3,2,0,1,1], [0,0,0,0,0,1]]) == False:
    print('Ok')
else:
    print('bad')
