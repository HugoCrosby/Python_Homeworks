Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sum_of_range(a,b):
    res = a
    while a < b:
        res += a + 1
        a += 1
    return res

def sum_of_range2(a,b):
    res = 0
    while a < b:
        res += a
        a += 1
    return res + b


sum_of_range(1,10)
55
sum_of_range2(1,10)
55
sum_of_range(2,20)
209
sum_of_range2(2,20)
209
