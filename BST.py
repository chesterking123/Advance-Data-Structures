class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,insert_data):
        if self.root is None:
            self.root = Node(insert_data)
        else:
            self._insert(insert_data,self.root)
    
    def _insert(self,insert_data,cur_node):
        if cur_node.value < insert_data:
            if cur_node.right is None:
                cur_node.right = Node(insert_data)
            else:
                self._insert(insert_data,cur_node.right)

        elif cur_node.value > insert_data:
            if cur_node.left is None:
                cur_node.left = Node(insert_data)
            else:
                self._insert(insert_data,cur_node.left)
        else:
            print('Value Already Present')
        
    def preorder(self,cur_node):
        if cur_node:
            print(str(cur_node.value),end = ' ')
            self.preorder(cur_node.left)
            self.preorder(cur_node.right)
    
    def inorder(self,cur_node):
        if cur_node:
            self.inorder(cur_node.left)
            print(str(cur_node.value),end = ' ')
            self.inorder(cur_node.right)
    
    def postorder(self,cur_node):
        if cur_node:
            self.postorder(cur_node.left)
            self.postorder(cur_node.right)
            print(str(cur_node.value),end = ' ')
            
    
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

            
bb = BinarySearchTree()
bb.insert(5)
bb.insert(4)
bb.insert(6)
bb.insert(1)
bb.insert(2)
#bb.insert(1)
#bb.insert(2)

bb.inorder(bb.root)
print('\n')
bb.preorder(bb.root)
print('\n')
bb.postorder(bb.root)
print('\n')
bb.height(bb.root)
