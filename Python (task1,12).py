Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def pascal(column,member):
    ''' bolor "column"-ere irar zugaher en,
    orinak 1-in "column"-e dzax kam aj koxmi 1-ere,
    isk 2-rd "column"-e dran zugaher "1,2,3..." "column"-e '''
    if member == 1:
        return 1
    elif column == 1:
        return 1
    elif member == 2:
        return column
    elif column == 2:
        return member
    return pascal(column-1,member) + pascal(column,member-1)

def real_pascal(m,n):
    return 1 if m in (1,2) or n in (1,m) else real_pascal(m-1,n) + real_pascal(m-1,n-1)

pascal(5,6)
126
real_pascal(5,6)
8
pascal(7,11)
8008
real_pascal(7,11)
32
pascal(7,4)
84
real_pascal(7,4)
20
real_pascal(8,4)
35
