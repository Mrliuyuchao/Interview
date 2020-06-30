def hammingWeight(x,y):
    # 临时变量等于把输入的;两个数做异或运算 相同为0不同为一
    a = x^y
    # 计数
    count = 0
    # 循环临时变量不等于零
    while a!=0:
        # 临时变量等于临时变量与临时变量减一做与运算  去除最后一个1
        a = a&(a-1)
        # 计数加等于1
        count+=1
        # 返回计数的值就是不同的个数
    return count

print(hammingWeight(4,14))