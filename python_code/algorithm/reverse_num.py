# 反转数字

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    str_num = str(x)
    if x >= 0:
        res = int(str_num[::-1])
        if res <= -2 ** 32 or res >= 2 ** 31 - 1:
            res = 0
        return res
    else:
        res = -int(str_num[::-1][0:len(str_num) - 1])
        if res <= -2 ** 32 or res >= 2 ** 31 - 1:
            res = 0
        return res


print(reverse(-1563847412))
print(-2147483651<=-2**32)