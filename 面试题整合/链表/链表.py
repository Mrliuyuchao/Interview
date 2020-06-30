from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(%s)'%(self.data)

class LinkList:
    def __init__(self):
        self.head = None

    # 增加头部
    def insert_head(self,data):
        new_data = Node(data)
        if self.head:
            new_data.next = data
        self.head = new_data

    # 增加尾部
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    # 中间插入
    def insert(self,i,data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            new_data = Node(data)
            curr =self.head
            pre = self.head
            j = 1
            while j<i:
                pre = curr
                curr = curr.next
                j += 1
            pre.next = new_data
            new_data.next = curr

    # 直接构建多元链表链
    def LinkList(self,obj:List):
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

    # 删除头部
    def delete_head(self):
        if self.head is None:
            raise Exception('空链表')
        else:
            self.head = self.head.next

    #删除尾部
    def pop(self):
        if self.head is None:
            raise Exception('空链表')
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next = None
        return temp

    # 删除尾部2
    def delete_tail(self):
        if self.head is None:
            raise Exception('空链表')
        else:
            curr = self.head
            pre = curr
            while curr.next:
                pre = curr
                curr = curr.next
            temp = pre
            pre.next = None
        return temp

    # 打印
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def __repr__(self):
        curr = self.head
        string = ''
        while curr:
            string += '%s-->'%(curr)
            curr = curr.next
        return string + 'END'

if __name__ == '__main__':
    ll = LinkList()
    ll.insert_head(1)
    ll.append(2)
    ll.insert(2,20)
    # ll.LinkList([1, 2, 3, 4, 5])
    # print(ll)
    # ll.delete_head()
    # ll.delete_tail()
    # print(ll.delete_tail())
    # ll.pop()
    # print(ll.pop())
    ll.print_list()
    print(ll)

