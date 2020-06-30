def longestPalindrome(strs):
    # 字符串长度
    length = len(strs)
    # 如果字符串长度小于2
    if length < 2:
        # 返回字符串
        return strs
    # 最大长度为1
    maxlen = 1
    # 字符串首位
    res = strs[0]
    # 循环
    for i in range(length-1):
        # 奇数调用方法
        odd = centerSpread(strs,i,i)
        # 偶数调用方法
        even = centerSpread(strs,i,i+1)
        # 最大字符串等于如果奇数字符串长返回奇数否则返回偶数
        maxstr = odd if len(odd) > len(even) else even
        # 如果 最大字符串长度大于最大长度
        if len(maxstr) > maxlen:
            # 最大长度等于最大字符串长度
            maxlen = len(maxstr)
            # 字符串等于最大字符串
            res = maxstr
    return res

def centerSpread(strs,left,right):
    # 长度
    length = len(strs)
    # i等于左指针
    i = left
    # j等于右指针
    j = right
    # 循环i大于等于零并且j小于长度
    while i >= 0 and j< length:
        # 如果字符串对应的i值等于字符串对应的j值
        if strs[i] == strs[j]:
            # 左指针向左移动一位
            i -= 1
            # 右指针向右移动一位
            j += 1
        # 否则
        else:
            # 跳出循环
            break
    # 返回从左指针加1到右指针中间的值
    return strs[i+1:j]