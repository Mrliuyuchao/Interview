# **tree**
#### **创建一个节点类**
    新建一个节点类
        定义一个init方法,传入一个数
            创建一个data等于出入的数
            创建一个左孩子等于None
            创建一个右孩子等于None
        
        定义一个repr方法
            返回设计好的输出类型
            
    class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node(%s)"%(self.data)



#### **二叉树的增加与查询**
    定义一个树类
        定义一个init方法
            创建一个根节点等于None
    class Tree:
    def __init__(self):
        self.root = None
    
    ## 增加
        定义一个增加的方法,传入要增加的数
            创建一个变量1接收要插入的数
            如果 根节点为空的时候
                根节点就等于变量1 
            否则:
                创建有个变量2接收根节点用数组的形式
                循环,死循环(不知道运行多少次的情况下)
                    定义一个临时变量3等于变量2弹出的第一个值下标为零(此时数组为None)
                    如果 临时变量3的左孩子是空的话:
                        临时变量3的左孩子等于变量1
                        跳出循环
                    否则如果 临时变量3的右孩子为空的话
                        临时变量3的右孩子等于变量1
                    否则:
                        把临时变量3的左孩子增加到变量2的列表中
                        把临时变量3的右孩子增加到变量2的列表中
    
        def add(self,item):
            node = Node(item)
            if self.root is None:
                self.root = node
            else:
                temp = [self.root]
                while True:
                    pop_node = temp.pop(0)
                    if pop_node.left is None:
                        pop_node.left = node
                        return
                    elif pop_node.right is None:
                        pop_node.right = node
                        return
                    else:
                        temp.append(pop_node.left)
                        temp.append(pop_node.right)                    
        
                    
    ## 查找父节点
         ## 1.只能查找到第一个父节点
         定义一个查找父节点的方法,传入要查找的数
            如果 根节点的数值等于要传入的数:   
                返回None
            创建一个临时变量temp等于根节点用数组接收
            循环 当临时变量temp 不为空的时候
                创建一个临时变量pop 等于 临时变量temp弹出第一个值
                如果 临时变量pop的左孩子的值等于要查找的值
                    返回 临时变量pop
                如果 临时变量pop的右孩子的值等于要查找的值
                    返回 临时变量pop
                如果 临时变量pop的左孩子不为空时:
                    把临时变量pop的左孩子添加到临时变量temp
                如果 临时变量pop的右孩子不为空时:
                    把临时变量pop的右孩子添加到临时变量temp
            返回 None
            
            
         ##查找全部父节点
         定义一个查找父节点的方法,传入一个要查找的数
            如果 根节点的数值等于要查找的数时:
                返回  None
            创建一个临时变量temp等于根节点为数组类型
            创建一个空数组res
            循环 临时变量temp不为空时:
                创建一个临时变量pop等于弹出的临时变量temp的第一个值
                如果 临时变量pop的左孩子不为空 并且 临时变量左孩子的值等于查找的值:
                    临时变量pop添加到数组res中
                否则如果 临时变量pop的右孩子不为空 并且 临时变量右孩子的值等于查找的值
                    临时变量pop添加到数组res中
                如果 临时变量pop左孩子不为空时:
                    临时变量pop的左孩子添加到临时变量temp:
                如果 临时变量pop右孩子不为空时:
                    临时变量pop的有害在添加到临时变量temp
            返回 数组res
            
         def get_parent1(self,item):
            if self.root.data == item:
                return None
            temp = [self.root]
            res = []
            while temp:
                pop_node = temp.pop(0)
                if pop_node.left and (pop_node.left.data == item):
                    res.append(pop_node)
                elif pop_node.right and (pop_node.right.data == item):
                    res.append(pop_node)
                if pop_node.left:
                    temp.append(pop_node.left)
                if pop_node.right:
                    temp.append(pop_node.right)
            return res   
            
            
#### **查询**
    if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(2)
    tree.add(6)
    tree.add(7)
    print(tree.root.left.left)
    print(tree.root.right.right)
    print(tree.get_parent(2))
    print(tree.get_parent1(2))

#### **结果**
    Node(4)
    Node(7)
    Node(1)
    [Node(1), Node(2)]
            
                       
            