Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def pow_with_Znumbs(m,n):
    count = 0
    res = 1
    while count < abs(n):
        res *= m
        count += 1
    if n < 0:
        if m == 0:
            return print("are you fucking high?")
        return 1/res
    elif n ==  0:
        return 1
    return res

pow_with_Znumbs(2,5)
32
pow_with_Znumbs(2,-4)
0.0625
pow_with_Znumbs(0,-2)
are you fucking high?
pow_with_Znumbs(18,0)
1
