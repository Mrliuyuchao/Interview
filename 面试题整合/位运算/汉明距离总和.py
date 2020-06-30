# def hammingWeight(nums):
#     count = 0
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             a = nums[i]^nums[j]
#             while a!=0:
#                 a = a & (a-1)
#                 count += 1
#     return count
# print(hammingWeight([4,14,2]))


def hammingWeight(nums):
    # 记录总和
    res = 0
    # 循环,从零到32因为一个帧数代表8位
    for i in range(32):
        # 记录零的个数
        count_0 = 0
        # 记录一的个数
        count_1 = 0
        # 循环,从零到列表的长度
        for j in range(len(nums)):
            # 如果nums[j]向右移动位和1做与运算不为零
            if (nums[j] >> i) & 1:
                # 记录1的个数加等于1
                count_1 += 1
            else:
                # 记录零的个数加等于
                count_0 += 1
        # 总和等于总和加记录零的个数乘以记录一的个数
        res = res + count_0 * count_1
    return res
print(hammingWeight([4,14,2]))

