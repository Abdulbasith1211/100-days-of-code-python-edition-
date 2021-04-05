#DAY 13  - [ LINKED LISTS 1]

# A simple Python program for traversal of a linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function prints contents of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next


# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second; # Link first node with second
	second.next = third; # Link second node with the third node

	llist.printList()







# A complete working Python program to demonstrate all
# insertion methods of linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


	# Functio to insert a new node at the beginning
	def push(self, new_data):

		# 1 & 2: Allocate the Node &
		#	 Put in the data
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to new Node
		self.head = new_node


	# This function is in LinkedList class. Inserts a
	# new node after the given prev_node. This method is
	# defined inside LinkedList class shown above */
	def insertAfter(self, prev_node, new_data):

		# 1. check if the given prev_node exists
		if prev_node is None:
			print ("The given previous node must inLinkedList.")
			return

		# 2. create new node &
		#	 Put in the data
		new_node = Node(new_data)

		# 4. Make next of new Node as next of prev_node
		new_node.next = prev_node.next

		# 5. make next of prev_node as new_node
		prev_node.next = new_node


	# This function is defined in Linked List class
	# Appends a new node at the end. This method is
	# defined inside LinkedList class shown above */
	def append(self, new_data):

		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
		new_node = Node(new_data)

		# 4. If the Linked List is empty, then make the
		# new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# 6. Change the next of last node
		last.next = new_node


	# Utility function to print the linked list
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data),
			temp = temp.next



# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
	llist = LinkedList()

	# Insert 6. So linked list becomes 6->None
	llist.append(6)

	# Insert 7 at the beginning. So linked list becomes 7->6->None
	llist.push(7);

	# Insert 1 at the beginning. So linked list becomes 1->7->6->None
	llist.push(1);

	# Insert 4 at the end. So linked list becomes 1->7->6->4->None
	llist.append(4)

	# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
	llist.insertAfter(llist.head.next, 8)

	print ('Created linked list is:'),
	llist.printList()








# A complete working Python3 program to
# demonstrate deletion in singly
# linked list with class

# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Given a reference to the head of a list and a key,
	# delete the first occurence of key in linked list
	def deleteNode(self, key):
		
		# Store head node
		temp = self.head

		# If head node itself holds the key to be deleted
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		# Search for the key to be deleted, keep track of the
		# previous node as we need to change 'prev.next'
		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		# if key was not present in linked list
		if(temp == None):
			return

		# Unlink the node from linked list
		prev.next = temp.next

		temp = None


	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (" %d" %(temp.data)),
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print ("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print ("\nLinked List after Deletion of 1:")
llist.printList()






# Python program to delete a node in a linked list
# at a given position

# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Constructor to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Given a reference to the head of a list
	# and a position, delete the node at a given position
	def deleteNode(self, position):

		# If linked list is empty
		if self.head == None:
			return

		# Store head node
		temp = self.head

		# If head needs to be removed
		if position == 0:
			self.head = temp.next
			temp = None
			return

		# Find previous node of the node to be deleted
		for i in range(position -1 ):
			temp = temp.next
			if temp is None:
				break

		# If position is more than number of nodes
		if temp is None:
			return
		if temp.next is None:
			return

		# Node temp.next is the node to be deleted
		# store pointer to the next of node to be deleted
		next = temp.next.next

		# Unlink the node from linked list
		temp.next = None

		temp.next = next


	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (" %d " %(temp.data)),
			temp = temp.next


# Driver program to test above function
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print ("Created Linked List: ")
llist.printList()
llist.deleteNode(4)
print ("\nLinked List after Deletion at position 4: ")
llist.printList()




# Python3 program to delete all
# the nodes of singly linked list

# Node class


class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Constructor to initialize the node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def deleteList(self):

		# initialize the current node
		current = self.head
		while current:
			prev = current.next # move next node

			# delete the current node
			del current.data

			# set current equals prev node
			current = prev

		# In python garbage collection happens
		# therefore, only
		# self.head = None
		# would also delete the link list

	# push function to add node in front of llist
	def push(self, new_data):

		# Allocate the Node &
		# Put in the data
		new_node = Node(new_data)

		# Make next of new Node as head
		new_node.next = self.head

		# Move the head to point to new Node
		self.head = new_node


# Use push() to construct below
# list 1-> 12-> 1-> 4-> 1
if __name__ == '__main__':

	llist = LinkedList()
	llist.push(1)
	llist.push(4)
	llist.push(1)
	llist.push(12)
	llist.push(1)

	print("Deleting linked list")
	llist.deleteList()

	print("Linked list deleted")








# A complete working Python program to find length of a
# Linked List iteratively

# Node class
class Node:
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


	# This function is in LinkedList class. It inserts
	# a new node at the beginning of Linked List.
	def push(self, new_data):

		# 1 & 2: Allocate the Node &
		#	 Put in the data
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to new Node
		self.head = new_node


	# This function counts number of nodes in Linked List
	# iteratively, given 'node' as starting node.
	def getCount(self):
		temp = self.head # Initialise temp
		count = 0 # Initialise count

		# Loop while end of linked list is not reached
		while (temp):
			count += 1
			temp = temp.next
		return count


# Code execution starts here
if __name__=='__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(3)
	llist.push(1)
	llist.push(2)
	llist.push(1)
	print ("Count of nodes is :",llist.getCount())



# Iterative Python program to search an element
# in linked list

# Node class
class Node:
	
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null

# Linked List class
class LinkedList:
	def __init__(self):
		self.head = None # Initialize head as None

	# This function insert a new node at the
	# beginning of the linked list
	def push(self, new_data):
	
		# Create a new Node
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to new Node
		self.head = new_node

	# This Function checks whether the value
	# x present in the linked list
	def search(self, x):

		# Initialize current to head
		current = self.head

		# loop till current not equal to None
		while current != None:
			if current.data == x:
				return True # data found
			
			current = current.next
		
		return False # Data Not found


# Code execution starts here
if __name__ == '__main__':

	# Start with the empty list
	llist = LinkedList()

	''' Use push() to construct below list
		14->21->11->30->10 '''
	llist.push(10);
	llist.push(30);
	llist.push(11);
	llist.push(21);
	llist.push(14);

	if llist.search(21):
		print("Yes")
	else:
		print("No")





# Recursive Python program to
# search an element in linked list

# Node class
class Node:
	
	# Function to initialise
	# the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null

class LinkedList:
	
	def __init__(self):
		self.head = None # Initialize head as None

	# This function insert a new node at
	# the beginning of the linked list
	def push(self, new_data):
	
		# Create a new Node
		new_node = Node(new_data)

		# Make next of new Node as head
		new_node.next = self.head

		# Move the head to
		# point to new Node
		self.head = new_node
	
	
	# Checks whether the value key
	# is present in linked list
	def search(self, li, key):
		
		# Base case
		if(not li):
			return False
		
		# If key is present in
		# current node, return true
		if(li.data == key):
			return True
		
		# Recur for remaining list
		return self.search(li.next, key)
	
# Driver Code			
if __name__=='__main__':

	li = LinkedList()
	
	li.push(1)
	li.push(2)
	li.push(3)
	li.push(4)
	
	key = 4
	
	if li.search(li.head,key):
		print("Yes")
	else:
		print("No")
	


# A complete working Python program to find n'th node
# in a linked list

# Node class


class Node:
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function is in LinkedList class. It inserts
	# a new node at the beginning of Linked List.

	def push(self, new_data):

		# 1 & 2: Allocate the Node &
		#	 Put in the data
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to new Node
		self.head = new_node

	# Returns data at given index in linked list
	def getNth(self, index):
		current = self.head # Initialise temp
		count = 0 # Index of current node

		# Loop while end of linked list is not reached
		while (current):
			if (count == index):
				return current.data
			count += 1
			current = current.next

		# if we get to this line, the caller was asking
		# for a non-existent element so we assert fail
		assert(false)
		return 0


# Driver Code
if __name__ == '__main__':

	llist = LinkedList()

	# Use push() to construct below list
	# 1->12->1->4->1
	llist.push(1)
	llist.push(4)
	llist.push(1)
	llist.push(12)
	llist.push(1)

	n = 3
	print("Element at index 3 is :", llist.getNth(n))




# Python3 program to find n'th node in
# linked list using recursion


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	''' Given a reference (pointer to pointer) to the
		head of a list and an int, push a new node on
		the front of the list. '''

	def push(self, new_data): # make new node and add
							# into LinkedList
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def getNth(self, llist, position):

		# call recursive method
		llist.getNthNode(self.head, position, llist)

	# recursive method to find Nth Node
	def getNthNode(self, head, position, llist):
		count = 0 # initialize count
		if(head):
			if count == position: # if count is equal to position,
								# it means we have found the position
				print(head.data)
			else:
				llist.getNthNode(head.next, position - 1, llist)
		else: # if head doesn't exist we have
			# traversed the LinkedList
			print('Index Doesn\'t exist')


# Driver Code
if __name__ == "__main__":
	llist = LinkedList()
	llist.push(1)
	llist.push(4)
	llist.push(1)
	llist.push(12)
	llist.push(1)
	# llist.getNth(llist,int(input()))
	# Enter the node position here
	# first argument is instance of LinkedList

	print("Element at Index 3 is", end=" ")
	llist.getNth(llist, 3)



