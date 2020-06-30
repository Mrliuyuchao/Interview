# def binarySearch(nums,val):
    # left = 0
    # right = len(nums) - 1
    # while left <= right:
    #     if target not in nums:
                # return -1
    #     if val == nums[left]:
    #         return left
    #     elif val == nums[right]:
    #         return right
    #     else:
    #         mid = (left + right) // 2
    #         if val > nums[mid]:
    #             left = mid
    #         elif val < nums[mid]:
    #             right = mid
    #         else:
    #             return mid

#改良
def binarySearch(nums,target):
    left = -1
    right = len(nums)
    while left < right:
        if target not in nums:
            return -1
        mid = (left + right) // 2
        # mid = left + (right - left) //2 适合其他编程语言
        if target > nums[mid]:
            left = mid
        elif target < nums[mid]:
            right = mid
        else:
            return mid


# @递归版
def binarySearch(nums,target,left,right):
    if right > 0:
        mid =left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binarySearch(nums,target,left,mid-1)
        else:
            return binarySearch(nums,target,mid+1 ,right)
    else:
        return -1


a = list(range(30))
b =10
ll = binarySearch(a,b,-1,31)
print(ll)
