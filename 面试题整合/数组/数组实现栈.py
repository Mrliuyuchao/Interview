class Stack:
    def __init__(self,limit = 10):
        self.stack = []
        self.size = 0

    def __str__(self):
        return str(self.stack)

    # 压栈
    def push(self,item):
        self.stack.append(item)
        self.size += 1

    # 弹栈
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.size -= 1

    # 顶值
    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return self.stack is None

    def size(self):
        return self.size

if __name__ == '__main__':
    stack = Stack(10)
    for i in range(10):
        stack.push(i)
    print(stack)
    for i in range(2):
        stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size)
