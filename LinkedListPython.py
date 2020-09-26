class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_it(self):
        itr = self.head
        while itr:
            print(itr.data,'-->',end = ' ')
            itr = itr.next
    
    def push(self, new_data):  
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node 
        
    def append(self, new_data):
        new_node = Node(new_data)
        
        if(self.head == None):
            self.head = new_node
            return
        
        itr = self.head
        while(itr.next):
            itr = itr.next
        
        itr.next = new_node
        
    def insert_after(self,prev_node,new_data):
        new_node = Node(new_data)
    
        itr = self.head
        while(itr):
            if(itr.data == prev_node ):
                break
            itr = itr.next

            
        prev_node = itr
        new_node.next = prev_node.next
        prev_node.next = new_node
        return
        
    def insert_before(self, before_data, new_data):
        new_node = Node(new_data)
        
        stop_node = self.head
        
        while(stop_node):
            if(stop_node.data == before_data):
                break
            stop_node = stop_node.next
        
        itr = self.head
        
        while(itr):
            if(itr.next == stop_node):
                break
            itr = itr.next
        new_node.next = itr.next
        itr.next = new_node
    
    def delete_node(self,del_node):
        
        itr = self.head
        
        stop_node = self.head
        
        while(stop_node):
            if(stop_node.data == del_node):
                break
            stop_node = stop_node.next
        
        if stop_node is None:
            print('Delete Node Not Available')
            return
            
        to_connect = stop_node.next
        

        while(itr):
            if(itr.next == stop_node):
                break
            itr = itr.next 
        
        itr.next = to_connect
        
    def is_palindrome(self):
        itr = self.head
        lis = []
        
        while(itr):
            lis.append(itr.data)
            itr = itr.next
            
        check = (lis == lis[::-1])
        
        if(check is True):
            print("It is a palindrome")
        
        else:
            print('Not a palindrome')
        
    def rotate(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev
        
    def make_a_loop(self, node_data):
        itr = self.head
        
        while(itr.next is not None):
            itr = itr.next
        
        to_connect = self.head
        
        while(to_connect):
            if(to_connect.data == node_data):
                break
            to_connect = to_connect.next
            
        itr.next = to_connect
    
    def detect_loop(self):
        
        a = []
        itr = self.head
        while(itr):
            
            if(itr.data in a):
                print('A loop exits')
                return
            else:
                a.append(itr.data)
            
            itr = itr.next
            
        print('No loop exits')
        return
            

        
        
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(5)
ll.append(6)
#ll.append(2)
#ll.append(1)
ll.insert_after(2,3)
ll.insert_before(5,4)
ll.delete_node(6)
#ll.push(10)
#ll.rotate()
ll.print_it()
#ll.is_palindrome()
ll.make_a_loop(2)
ll.detect_loop()

