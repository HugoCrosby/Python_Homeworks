Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def inc(a):
    return a + 1

def dec(a):
    return a - 1

def add1(a,b):
    '''the function is recursion ,as every time, during the call, the local area is created until the argument a will be equal to 0, then the argument b will increase by 1 as much as the local area is created '''
    if a == 0:
        return b
    return inc(add1(dec(a),b))

def add2(a,b):
    '''the function is considered to be tail recursion as during the call the recursion is taking place but the action is iterative, so the local area 1 is created and the argument a and b which are included in that local area change and for the next call the last values are not necessary'''
    if a == 0:
        return b
    return add2(dec(a),inc(b):