# **binary_search_tree**
#### **导入包**
    from pprint import pformat
#### **定义节点类
    定义节点类:  
        定义 init方法,传入节点数,父节点
            创建一个变量value等于传入的节点数
            创建一个变量parent等于父节点
            创建一个左孩子等于None
            创建一个右孩子等于None
        
        定义一个repr方法
            如果 左孩子为空 并且 右孩子为空
                返回 字符串类型的value
            返回 调用pformat包返回树
    
    class Node:
        def __init__(self,data,parent):
            self.value = data
            self.parent = parent
            self.left = None
            self.right = None
    
        def __repr__(self):
            if self.left is None and self.right is None:
                return  str(self.value)
            return pformat({"%s"%(self.value):(self.left,self.right)},indent=1)

    
#### **定义BST类**
        定义init方法:
            创建一个根节点等于None
        def __init__(self,root=None):
            self.root = root
        
        定义一个str方法:
            返回 字符串类型的根节点
        def __str__(self):
            return  str(self.root)   
        
        定义一个是否为空的方法:
            如果 根节点为空
                返回 True
            否则:
                返回 Fasle
        def is_empty(self):
            if self.root is None:
                return True
            else:
                return False  
                
        定义一个is_right方法传入一个节点
            返回 节点等于这个节点的父节点的有节点
        
        def is_right(self,node):
            return node == node.parent.right
          
#### **插入**
        定义一个 私有的查询方法,传入一个要插入的数
            创建一个临时变量new来接收传入数的节点
            如果 调用is_empty方法为True时
                根节点等于临时变量new
            否则:
                创建一个临时边来那个parent等于根节点
                循环 True死循环(不知道执行多少次)
                    如果插入值小于临时变量parent的值
                        如果 临时变量parent的左孩子为空
                            临时变量parent左孩子等于临时变量new
                            跳出循环
                        否则:
                            临时变量parent等于临时变量parent的左孩子
                    否则如果 插入值大于等于临时变量parent的值:
                        如果 临时变量parent的右孩子为空时:
                            临时变量parent的右孩子等于临时变量new
                            跳出循环
                        否则:
                            临时变量parent等于临时变量parent的右孩子
                临时变量new的父节点等于临时变量parent
             
        定义一个插入方法,传入一个数组:
            for循环数组
                调用私有插入方法传入value
            返回 self
         
         
        def __insert(self,value):
            new_node = Node(value,None)
            if self.is_empty():
                self.root = new_node
            else:
                parent_node = self.root
                while True:
                    if value < parent_node.value:
                        if parent_node.left is None:
                            parent_node.left = new_node
                            break
                        else:
                            parent_node = parent_node.left
                    elif value >= parent_node.value:
                        if parent_node.right is None:
                            parent_node.right = new_node
                            break
                        else:
                            parent_node = parent_node.right
                new_node.parent = parent_node
    
        def insert(self,*arges):
            for value in arges:
                self.__insert(value)
            return self
        
#### **查询**
        定义一个查询方法,传入要查询的值
            如果调用is_empty为True:
                返回 错误
            否则:
                创建一个临时变量node 等于根节点
                循环 临时变量node不为空时 并且 临时变量node的值不 等于 查找的值:
                    临时变量node 等于 如果 查找的值小与临时变量node的值 返回 临时变量node的左孩子
                                      否则 返回临时变量node的有孩子
                打印临时变量node
                返回临时变量node
                
        def search(self,value):
            if self.is_empty():
                raise Exception('空树')
            else:
                node = self.root
                while node and node.value != value:
                    node = node.left if value < node.value else node.right
                print(node)
                return node
                
#### **交换**
        定义私有交换方法,传入一个节点,一个新孩子
            如果 新孩子不为空:
                新孩子的父节点等于数的父节点
            如果 数的父节点不为空:
                如果 调用is_right方法,传入这个数,判断这个节点是不是这个节点的父节点的右孩子,是的话:
                    这个节点的父节点的右孩子等于新孩子
                否则:
                    这个节点的父节点的左孩子等于新孩子
            否则:
                根节点等于新孩子
                
        def __reassign_node(self,node,new_children):
            if new_children is not None:
                new_children.parent = node.parent
            if node.parent is not None:
                if self.is_right(node):
                    node.parent.right = new_children
                else:
                    node.parent.left =new_children
            else:
                self.root = new_children
                
                
#### **左边节点的最大值**
        定义一个最大值的方法,传入一个节点起始为空
            如果这个节点为空:
                节点等于根节点
            如果 调用is_empty方法Fast时:
                循环 节点的右孩子不为空时:
                    节点等于节点的右孩子
            返回 节点
        def get_max(self,node=None):    
           if node is None:
            node = self.root
            if not self.is_empty():
                while node.right is not None:
                    node = node.right
            return node
            
#### **删除**
        定义一个删除方法,传入要删除的值
            创建一个临时变量seach 等于 调用查询方法查询要删除值的节点
            如果 临时变量seach 不为空:
                如果 临时变量seach的左孩子为空,并且临时变量seach的右孩子为空:
                    调用交换方法,传入临时变量seach和None(当前节点为None 就把要删除的数删除了)
                否则如果 临时变量seach的左孩子为空:
                    调用交换方法,传入临时变量seach和临时变量seach的右孩子(当前节点的值等于右孩子,右孩子为None)
                否则如果 临时变量seach的右孩子为空:
                    调用交换方法,传入临时变量seach和临时变量seach的左孩子(当前节点的值等于左孩子,左孩子为None)
                否则:
                    创建一个临时变量temp等于调左边节点最大值方法,传入临时变量seach的左孩子(最后查找到左边枝杈上的最大值)
                    调用删除方法自身传入临时变量temp(继续判断临时变量temp有没有左孩子,之后进行交换,这个节点等于左边最大值,最大值等于None)
                    临时变量seach的值等于临时变量temp的值
                    
        def remove(self,value):
            seach_node =self.search(value)
            if seach_node is not None:
                if seach_node.left is None and seach_node.right is None:
                    self.__reassign_node(seach_node,None)
                elif seach_node.left is None:
                    self.__reassign_node(seach_node,seach_node.right)
                elif seach_node.right is None:
                    self.__reassign_node(seach_node,seach_node.left)
                else:
                    temp = self.get_max(seach_node.left)
                    self.remove(temp)
                    seach_node.value = temp.value      
                    
                    
### **遍历**
#### **前序遍历**
        定义一个前序遍历的方法,传入一个节点
            如果这个节点为空
                返回
            打印这个节点的值
            调用自身方法传入这个节点的左孩子
            调用自身方法传入这个节点的右孩子
            返回 节点
        
        def preorder(self,node):
            if node is None:
                return
            print(node.value,end=',')
            self.preorder(node.left)
            self.preorder(node.right)
            return node
        
#### 前序图片地址
![https://imgchr.com/i/NxbA1S](https://imgchr.com/i/NxbA1S)
#### **中序遍历**
        定义一个前序遍历的方法,传入一个节点
            如果这个节点为空
                返回
            调用自身方法传入这个节点的左孩子
            打印这个节点的值
            调用自身方法传入这个节点的右孩子
            返回 节点
        
        def preorder(self,node):
            if node is None:
                return
            self.preorder(node.left)
            print(node.value,end=',')
            self.preorder(node.right)
            return node
            
#### 中序图片地址
![https://imgchr.com/i/Nxb8cF](https://imgchr.com/i/Nxb8cF)
          
#### **后序遍历**
        定义一个前序遍历的方法,传入一个节点
            如果这个节点为空
                返回
            调用自身方法传入这个节点的左孩子
            调用自身方法传入这个节点的右孩子
            打印这个节点的值
            返回 节点
        
        def preorder(self,node):
            if node is None:
                return
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.value,end=',')
            return node        
        
#### 后序图片地址
![https://imgchr.com/i/Nxbdtx](https://imgchr.com/i/Nxbdtx)
