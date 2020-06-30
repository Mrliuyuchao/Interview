from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        show = 0
        fast = 1
        count = 1
        while fast < len(nums):
            if nums[fast] == nums[show]:
                if count>=2:
                    fast += 1
                else:
                    count += 1
                    show += 1
                    nums[show] =nums[fast]
                    fast += 1
            else:
                count = 1
                show += 1
                nums[show] = nums[fast]
                fast += 1
        return nums
if __name__ == '__main__':
    ll = Solution()
    print(ll.removeDuplicates([1,1,1,2,2,3,3]))