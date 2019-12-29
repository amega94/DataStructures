class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root
    def insert (self, node):
    
        #Case 0 : Empty BST 
        if self.root is None:
            self.root = node
            return
        
        #Case 1: Non-Empty BST
        current = self.root
        parent = None
        while current is not None:
            parent = current
            if current.value < node.value:
                current = current.right
            else:
               current = current.left
               
        #We have determined the location of insertion after breaking out of the while loop (after hitting the NULL)
        #We need to take a step back from the parent's prespective
        if parent.value < node.value:
            parent.right = node
        else:
            parent.left = node

    def printInOrder (self, node):
        if node is  None:
            return
        self.printInOrder(node.left)
        print(node.value)
        self.printInOrder(node.right)
    def printPreOrder (self, node):
        if node is  None:
            return
        print(node.value)
        self.printPreOrder(node.left)
        self.printPreOrder(node.right) 
    def printPostOrder (self, node):
        if node is  None:
            return
        self.printPostOrder(node.left)
        self.printPostOrder(node.right)
        print(node.value)
    def printLevelOrder(self):
        _list = []
        _list.append(self.root)
        
        while _list : # Python allows dynamic typing which means empty sequences evaluate to False and non-empty evalue to True.
            for i in range(len(_list)):
                print(_list[i].value, end = ' ')
                if _list[i].left is not None:
                    _list.append(_list[i].left)
                if _list[i].right is not None:
                    _list.append(_list[i].right)
            _list = _list[i+1:]
            print()
        

_lista = [10, 9, 11, 15, 16]
mybst = BST()

for element in _lista:
    mybst.insert(Node(element))

mybst.printInOrder(mybst.root)
    
# def printer (root, i=0):
#     if root.left is not None:
#         printer(root.left,i+1)
#     print(root.value, i)
#     if root.right is not None:
#         printer(root.right,i+1)
        
# printer(mybst.root)
