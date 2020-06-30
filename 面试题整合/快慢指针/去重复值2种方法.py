"""
首先创检一个快指针和一个慢指针
循环慢快指针小于列表的长度
如果快指针等于慢指针
快指针 += 1向后走一步
否则 慢指针不等于慢指针
慢指针 += 1向后走一步
快指针的值赋值给慢指针
快指针 += 1向后走一步

"""


# 方法一
from typing import List
# class Solution:
#     def removeDuolicated(self,nums:list):
#         show = 0
#         fast = 1
#         while fast <len(nums):
#             if nums[fast] == nums[show]:
#                 fast += 1
#             else:
#                 show += 1
#                 nums[show] = nums[fast]
#                 fast += 1
#         return show + 1,nums


# 方法二
class Solution:
    def removeDuolicated(self,nums:List):
        n = len(set(nums))
        i = 0
        while i < n -1:
            if nums[i] == nums[i+1]:
                temp = nums[i+1]
                nums[i+1:len(nums) -1 ] = nums[i+2:]
                nums[-1] = temp
                continue
            else:
                i+=1
        return i + 1,nums


if __name__ == '__main__':
    test = Solution()
    print(test.removeDuolicated([1,1,2,4,4,5]))
