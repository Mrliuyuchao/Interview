from typing import List
class Solution:
    def removeDuplicated(self,nums:list):
        show = 0
        fast = 0
        while fast<len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[show] =nums[fast]
                show += 1
                fast += 1
        return show,nums

if __name__ == '__main__':
    ll = Solution()
    print(ll.removeDuplicated([0,1,0,3,12]))