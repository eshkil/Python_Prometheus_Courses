def convert_n_to_m(x, n, m):
    if type(x) in [str,int] and 1 <= n and m <= 36:
        if type(x) == str:
            try:
                x = int(x)
            except Exception:
                return False
        if x >= 0:
#            while i >= 1
            print('ddd')
    else:
        return False

#---
print(convert_n_to_m('123', 1, 4))