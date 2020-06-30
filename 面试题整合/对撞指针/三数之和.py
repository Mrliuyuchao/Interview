from typing import List
def threeSum(nums:List[int]) -> List:
    nums.sort()
    result = []
    # 固定C位
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums) -1
        while left < right :
            node = nums[i] + nums[left] + nums[right]
            if node >0:
                right -= 1
            elif node < 0:
                left +=1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return result

if __name__ == '__main__':
    ll = threeSum([-1,0,1,-1,2,3])
    print(ll)

