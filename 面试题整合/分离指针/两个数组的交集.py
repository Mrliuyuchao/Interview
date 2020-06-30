def intersection(nums1,nums2):
    nums1.sort()
    nums2.sort()
    i,j = 0,0
    nums_set = set()

    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            nums_set.add(nums1[i])
            j += 1
            i += 1
    return  list(nums_set)

nums1 = [4,9,5]
nums2 = [9,8,4,4,9]
ll = intersection(nums1,nums2)
print(ll)

