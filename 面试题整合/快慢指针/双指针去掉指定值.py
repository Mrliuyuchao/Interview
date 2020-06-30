from typing import List
class Solution:
    def removeDuplicated(self,nums:list,val:int):
        show = 0
        fast = 0
        while fast <len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[show] = nums[fast]
                show += 1
                fast += 1
        return show,nums

if __name__ == '__main__':
    ll = Solution()
    print(ll.removeDuplicated([0,1,0,3,12],0))