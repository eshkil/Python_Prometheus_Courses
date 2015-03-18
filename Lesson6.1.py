def count_holes(n):
    dict = {1:0,2:0,3:0,4:1,5:0,6:1,7:0,8:2,9:1,0:1}
    if type(n) in [str,int,long]:
        if type(n) == str:
            try:
                n = long(n)
            except ValueError:
                return 'ERROR'
        if type(n) in [int,long]:
            n = str(n)
        if n[0] == '-':
            n = n[1:]
        count = 0
        for i in n:
            count = count + dict[int(i)]
        return count
    else:
        return 'ERROR'

print(count_holes(0))