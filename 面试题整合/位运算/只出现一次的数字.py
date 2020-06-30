def hammingWeight(nums):
    # 记录出现一次的数
    res = 0
    # 遍历数组
    for i in nums:
        # 计数等于 已或运算相同为0不同为1 最后剩下一只出现一次的数字
        res = res ^ i
    return res
print(hammingWeight([4,1,2,1,2]))