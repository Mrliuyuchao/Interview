def hammingWeight(n):
    # 计数
    count = 0
    # 输入的二进制数不为0
    while n != 0:
        # 输入的这个数与这个数减一做与运算
        n = n&(n-1)
        # 计数加等于1
        count += 1
        # 返回计数值就是一的个数
    return count

ll = hammingWeight(110000001)
print(hammingWeight(110000001))