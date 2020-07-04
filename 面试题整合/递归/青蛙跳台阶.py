# 青蛙跳台阶,跳一个台阶有一种方法 一次跳一个,跳两个台阶有两种方法, 一次跳一个跳两次或一次跳两个
def frog(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    return frog(n-1) + frog(n-2)
result = frog(4)