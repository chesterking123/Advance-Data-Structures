def printLevelOrder(root): 
    if root is None: 
        return
    q = [] 
    q.append(root)     
    while q: 
        count = len(q)   
        while count > 0: 
            temp = q.pop(0) 
            print(temp.val, end = ' ') 
            if temp.left: 
                q.append(temp.left) 
            if temp.right: 
                q.append(temp.right) 
            count -= 1

        print(' ') 


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
