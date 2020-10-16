from collections import deque
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
    
    def check_node(self,find_node,node):
        if (node == None):  
            return False
        if(node.value ==  find_node):
            is_found = True
            return is_found
        left_traversal = self.check_node(find_node,node.left)
        if left_traversal is True:
            return True
        right_traversal = self.check_node(find_node,node.right)
        
        return(right_traversal)
        
    def print_inrange(self,l,h,node):
        if node is None:
            return 
        if(node.value > l and node.value<h):
            print(node.value,end=' ')
        left_traversal = self.print_inrange(l,h,node.left)
        right_traversal = self.print_inrange(l,h,node.right) 
        return
    
    def level_order(self):
        root = self.root
        if(root is None):
            return
        q = deque()
        q.append(root)

        while(len(q)>0):
            node= q.popleft()
            print(node.value,end=' ')
            if(node.left is not None):
                q.append(node.left)
            if(node.right is not None):
                q.append(node.right)
                
    def top_view(self):
        root = self.root
        move_right = root.right
        stack = []

        while(root != None):
            stack.append(root.value)
            root = root.left
        
        stack = stack[::-1]
        
        
        while(move_right !=None):
            stack.append(move_right.value)
            move_right = move_right.right
        print(stack)

            
       def countLeaves(root):
            if(root is None):
                return
            q = deque()
            q.append(root)
            counter = 0
            while(len(q)>0):
                node= q.popleft()
                if(node.left is None and node.right is None):
                    counter = counter+1
                if(node.left is not None):
                    q.append(node.left)
                if(node.right is not None):
                    q.append(node.right)
            return(counter)
        

            
bb = BinarySearchTree()
bb.insert(4)
bb.insert(2)
bb.insert(6)
bb.insert(1)
bb.insert(3)
bb.insert(5)
bb.insert(7)



# bb.inorder(bb.root)
# print('\n')
# bb.preorder(bb.root)
# print('\n')
# bb.postorder(bb.root)
# print('\n')
# bb.height(bb.root)
# print(bb.check_node(7,bb.root))
# bb.print_inrange(2,5,bb.root)
# print('\n')
# bb.level_order()


## To do list:-
#def is_cousin(self,a,b):
#is mirror
#sumofnodes equeals k

bb.top_view()
