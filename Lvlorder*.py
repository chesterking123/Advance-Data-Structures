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
