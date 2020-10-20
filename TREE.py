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



def inOrder_itr(root): 
    current = root  
    stack = [] # initialize stack 
    done = 0 
    while True:          
        if current is not None: 
            stack.append(current) 
            current = current.left  
        elif(stack): 
            current = stack.pop() 
            print(current.data, end=" ") 
            current = current.right   
        else: 
            break

def iterativePreorder(root):  
    nodeStack = [] 
    nodeStack.append(root) 
    while(len(nodeStack) > 0): 
        node = nodeStack.pop() 
        print node.data, 
        if node.right is not None: 
            nodeStack.append(node.right) 
        if node.left is not None: 
            nodeStack.append(node.left)
            
def mirror_a_tree(root): #invert a tree
    # Code here
    if (root == None): 
        return
    else: 
        mirror(root.left)  
        mirror(root.right)  
        root.left,root.right = root.right,root.left 

def Checkif2treeMirror(a, b): 
    if a is None and b is None: 
        return True
    if a is None or b is None: 
        return False 
    return (a.data == b.data and areMirror(a.left, b.right) and areMirror(a.right , b.left)) 

def isSymmetric( root) : #if a tree is a mirror of itself 
q = []      
q.append(root)  
q.append(root)   
leftNode = 0
rightNode = 0
while(not len(q)):  
    leftNode = q[0]  
    q.pop(0)  
    rightNode = q[0]  
    q.pop(0)   
    if(leftNode.data != rightNode.data): 
        return False
    if(leftNode.left and rightNode.right) : 
        q.append(leftNode.left)  
        q.append(rightNode.right)  .  
    elif (leftNode.left or rightNode.right) : 
        return False
    if(leftNode.right and rightNode.left):  
        q.append(leftNode.right)  
        q.append(rightNode.left)  
    elif(leftNode.right or rightNode.left): 
        return False

return True


def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    lvl=0
    check=[]
    node=root
    def check_cousin(root,lvl,check,node):
        #print(a,c,root)
        if len(check)==4 or root==None:
            return
        if root.val==x:
            check.append(lvl)
            check.append(node.val)
        if root.val==y:
            check.append(lvl)
            check.append(node.val)
        lvl+=1
        m=root
        check_cousin(root.left,lvl,check,node)
        check_cousin(root.right,lvl,check,node)
    check_cousin(root,lvl,check,node)
    print(check)
    if check[0]==check[2] and check[1]!=check[3]:
        return True

   
###COMMON ANSESTOR PROGRAm
def findLCA(root, n1, n2): 
    if root is None: 
        return None
    # If either n1 or n2 matches with root's key, report 
    #  the presence by returning root (Note that if a key is 
    #  ancestor of other, then the ancestor key becomes LCA 
    if root.data == n1 or root.data == n2: 
        return root  
    # Look for keys in left and right subtrees 
    left_lca = findLCA(root.left, n1, n2)  
    right_lca = findLCA(root.right, n1, n2) 
    # If both of the above calls return Non-NULL, then one key 
    # is present in once subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca: 
        return root  
    # Otherwise check if left subtree or right subtree is LCA 
    if left_lca is not None:
        return left_lca
    else:
        return right_lca
  

def printkDistanceNodeDown(root, k): 
    if root is None or k< 0 : 
        return 
    # If we reach a k distant node, print it 
    if k == 0 : 
        print root.data  
        return 
    # Recur for left and right subtee 
    printkDistanceNodeDown(root.left, k-1) 
    printkDistanceNodeDown(root.right, k-1) 
