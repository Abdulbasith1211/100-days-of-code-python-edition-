#DAY 16   (Linked lists - problem solving [2])


#PROBLEM :  https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem


def RemoveDuplicates(head):
    node = head
    
    while node.next != None:
        if node.data == node.next.data:
            node.next = node.next.next
            continue
        node = node.next
  
    return head
  
  

#PROBLEM : https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

def Insert(head, data):
    node = head
    if head is None:
        head = Node(data)
        return head
    
    while node.next is not None:
        node = node.next
    
    node.next = Node(data)
    
    return head

def MergeLists(headA, headB):
    list_out = Node()
    node_a = headA
    node_b = headB
    
    while node_a and node_b:
        if node_a.data < node_b.data:
            list_out = Insert(list_out, node_a.data)
            node_a = node_a.next
        else:
            list_out = Insert(list_out, node_b.data)
            node_b = node_b.next
    
    last_node = list_out
    while last_node.next is not None:
        last_node = last_node.next
    
    if node_a:
        last_node.next = node_a
    elif node_b:
        last_node.next = node_b
        
    return list_out.next




#PROBLEM :  https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem


def FindMergeNode(headA, headB):
    values_a = []
    values_b = []
    
    node_a = headA
    node_b = headB
    
    while node_a != None:
        values_a.append(node_a.data)
        node_a = node_a.next
  
    while node_b != None:
        values_b.append(node_b.data)
        node_b = node_b.next
    
    res = values_a[-1]
    ind = 1
    while values_a[-ind] == values_b[-ind]:
        ind += 1
    
    res = values_a[-(ind-1)]
    
    return res
    
  

#PROBLEM  :  https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

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
  

#PROBLEM :  https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem


def SortedInsert(head, data):
    if head == None:
        return Node(data=data, next_node=None, prev_node=None)
    
    node = head
    while node.next != None and node.next.data <= data:
        node = node.next
    
    node.next = Node(data=data, next_node=node.next, prev_node=node)
    
    return head
  
  
#PROBLEM :  https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

def has_cycle(head):
    cnt = 0
    node = head
    
    if head is None:
        return 0
    
    while node != None:
        node = node.next
        cnt += 1
        if cnt > 100:
            return 1
    
    return 0
