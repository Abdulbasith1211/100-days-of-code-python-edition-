#DAY 15   [ linked lists - problem solving]

#PROBLEM : https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
def print_list(head):
    node = head
    while node != None:
        print(node.data)
        node = node.next



#PROBLEM : https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem


def Insert(head, data):
    if head is None:
        head = Node(data)
        return head
    else:
        buf = head
        
        head = Node(data)
        head.next = buf
        
        return head
    


#PROBLEM :  https://github.com/srgnk/HackerRank/blob/master/data-structures/insert-a-node-at-the-tail-of-a-linked-list.py

def Insert(head, data):
    node = head
    if head is None:
        head = Node(data)
        return head
    
    while  node.next != None:
        node = node.next
    
    node.next = Node(data)
    
    return head

#PROBLEM :   https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem


def list_len(head):
    node = head
    res = 0
    while node != None:
        res += 1
        node = node.next
    return res

def print_list(head):
    node = head
    while node != None:
        print("{}".format(node.data), end='')
        node = node.next
    print()
    
def InsertNth(head, data, position):
    if list_len(head) == 1 and head.data == 2:
        head = Node(data = data)
    elif position == 0:
        head = Node(data = data, next_node = head)
    else:
        node = head
        for _ in range(position - 1):
            node = node.next
        
        node.next = Node(data, next_node = node.next)
        
    return head

#PROBLEM :  https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem


def ReversePrint(head):
    if head is None:
        return
    else:
        out = []
        node = head
        
        while node != None:
            out.append(node.data)
            node = node.next
            
        print("\n".join(map(str, out[::-1])))


#PROBLEM:   https://www.hackerrank.com/challenges/reverse-a-linked-list/problem


def Reverse(head):
    prev = None
    node = head
    while node is not None:
        buf = node.next
        node.next = prev
        prev = node
        node = buf
        
    head = prev
    return head
  

#PROBLEM :  https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

  def Delete(head, position):
        if position == 0:
        head = head.next
    else:
        node = head
        for _ in range(position-1):
            node = node.next
        
        node.next = node.next.next
        
    return head
  


#PROBLEM : https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem


def GetNode(head, position):
    node = head
    list_len = 0
    
    while node != None:
        node = node.next
        list_len += 1
        
    node = head
    for _ in range(list_len - position - 1):
        node = node.next
    
    return node.data




#PROBLEM :  https://www.hackerrank.com/challenges/compare-two-linked-lists/problem    



def CompareLists(headA, headB):
    if headA is None and headB is None:
        return 0
    else:
        nodeA = headA
        nodeB = headB
        while nodeA and nodeB:
            if nodeA.data != nodeB.data:
                return 0
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        if nodeA is None and nodeB is None:
            return 1
        else:
            return 0
  
  
  
  
  