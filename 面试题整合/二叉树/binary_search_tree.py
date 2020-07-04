from pprint import pformat

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

class BST:
    def __init__(self,root=None):
        self.root = root

    def __str__(self):
        return  str(self.root)


    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def is_right(self,node):
        return node == node.parent.right

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

    def search(self,value):
        if self.is_empty():
            raise Exception('空树')
        else:
            node = self.root
            while node and node.value != value:
                node = node.left if value < node.value else node.right
            print(node)
            return node

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


    def get_max(self,node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node

    # 前序
    def preorder(self,node):
        if node is None:
            return
        print(node.value,end=',')
        self.preorder(node.left)
        self.preorder(node.right)
        return node
    # 中序
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value,end=',')
        self.inorder(node.right)
        return node
    # 后序
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value,end=',')
        return node


if __name__ == '__main__':
    bst = BST().insert(8,3,1,6,10,14,9)
    print(bst)
    bst.search(3)
    bst.remove(4)
    print(bst)
    print(bst.preorder(bst.root))
    print(bst.inorder(bst.root))
    print(bst.postorder(bst.root))