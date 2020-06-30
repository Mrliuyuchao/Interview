# 方法一
# 利用对撞指针实现
# 设左指针(left)从列表的第零位开始,右指针(right)从列表的最后一位开始,
# 如果左指针+右指针的和大于输入的值,则右指针向前移动(left+right)>target  right -= 1
# 如果左指针+右指针的和小于输入的值,则左指针向后移动(left+right)<rarget  left += 1
# 如果左指针+右指针的和等于输入的值,则返回这个值(left+right) == raeget

from typing import List
# 第一种方法
# def twoSum(nums:list,target:int):
#      左指针
#     left = 0
#      右指针
#     right = len(nums) -1
#       当左指针小于右指针
#     while left < right:
#           记录左指针和右指针的和值
#         curr = nums[left] + nums[right]
#           如果左指针和右指针的和等于输入的值
#         if curr == target:
#               返回左指针和右指针的值
#             return [left,right]
#         否则左指针和右指针的和不等于输入的值
#         else:
#               如果左指针和右指针的和小于输入的值
#             if curr < target:
#                   左指针 += 1想后移动
#                 left += 1
#               否则 左指针和右指针的和大于输入的值
#             else:
#                   右指针 -= 1 想前移动
#                 right -= 1
#

# ll = twoSum([-5,-4,-3,-2,-1],-8)
# print(ll)


# 方法二
# 运用字典的key和values值
# 首先新建一个新字典,遍历真个列表,新建临时变量接收输入的数减去列表中的每个数
# 判断这个数是不是在新建的新字典中,如果在,返回临时变量的values,不在,把列表中的值传入字典的key值,下标是values值
# 第二种方法
# class Solution:
#     def twoSum(self,nums:list,target:int):
#         new_sums = {}
#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if temp in new_sums:
#                 return [new_sums[temp],i]
#             else:
#                 new_sums[nums[i]] = i

# 方法三
# 暴力破解
# 利用双层循环,把列表循环,i值是下标,再循环一遍列表,从i+1未开始
# 如果nums[i] + nums[2] == 输入的值
# 返回i,j的值
# 第一个值和后面所有的值加一下判断相不相等
# 第三种方法
class Solution:
    def twoSum(self,nums:list,target:int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == '__main__':
    num = Solution()

    print(num.twoSum([3,2,4],6))