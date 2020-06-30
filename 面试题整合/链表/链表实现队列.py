from typing import Any,Optional
class Node:
    def __init__(self,data:Any,next:Optional['Node']=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "Node(%s)"%(self.data)

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def put(self,item:Any):
        node:Node = Node(item)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size +=1

    def pop(self):
        if self.is_empty():
            raise IndexError('Empty queue')
        else:
            node :Node = self.front
            self.front = node.next
        self.size -=1
        return node.data


    def get(self,index):
        if index < 0 or index > self.size:
            raise Exception('索引越界')
        else:
            curr = self.front
            for i in range(0,index-1):
                curr = curr.next
        return curr.next

    def __repr__(self):
        curr = self.front
        string = ''
        while curr:
            string += '%s <--' %(curr)
            curr = curr.next
        return string + 'end'

if __name__ == '__main__':
    queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    print(queue)
    queue.get(2)
    print(queue.get(2))
