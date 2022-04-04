Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def cube_root(m):
    res = 1
    while not enough_exactly(res,m):
        res = improve(res,m)
    return res

def enough_exactly(a,b):
    return abs(pow_two(a,3)-b) <= 0.0001

def improve(a,b):
    return ((b/pow_two(a,2)) + (2*a))/3

def pow_two(n,m):
    res = 1
    count = 0
    while count < m:
        res *= n
        count += 1
    return res

cube_root(8)
2.000004911675504
