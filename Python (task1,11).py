Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def f_rec(n):
    if n < 0:
        return n
    return f_rec(n-1) + f_rec(n-2) + f_rec(n-3)

def f_loop(n):
    a = 0
    b = 1
    c = 2
    while n > 0:
        tmp1 = b
        tmp2 = c
        c = a + b + c
        a = tmp1
        b = tmp2
        n -= 1
    return a

f_loop(5)
11
f_loop(10)
230

def f_tail_rec(n):
    