#DAY 17  {Learning stack } 

# Python program to
# demonstrate stack implementation
# using list


stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty





# Python program to
# demonstrate stack implementation
# using collections.deque


from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

# pop() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty





# Python program to demonstrate
# stack implementation using a linked list.
# node class
class Node:
def __init__(self, value):
	self.value = value
	self.next = None

class Stack:
	
# Initializing a stack.
# Use a dummy node, which is
# easier for handling edge cases.
def __init__(self):
	self.head = Node("head")
	self.size = 0

# String representation of the stack
def __str__(self):
	cur = self.head.next
	out = ""
	while cur:
		out += str(cur.value) + "->"
		cur = cur.next
	return out[:-3]

# Get the current size of the stack
def getSize(self):
	return self.size
	
# Check if the stack is empty
def isEmpty(self):
	return self.size == 0
	
# Get the top item of the stack
def peek(self):
	
	# Sanitary check to see if we
	# are peeking an empty stack.
	if self.isEmpty():
		raise Exception("Peeking from an empty stack")
	return self.head.next.value

# Push a value into the stack.
def push(self, value):
	node = Node(value)
	node.next = self.head.next
	self.head.next = node
	self.size += 1
	
# Remove a value from the stack and return.
def pop(self):
	if self.isEmpty():
		raise Exception("Popping from an empty stack")
	remove = self.head.next
	self.head.next = self.head.next.next
	self.size -= 1
	return remove.value

# Driver Code
if __name__ == "__main__":
stack = Stack()
for i in range(1, 11):
	stack.push(i)
print(f"Stack: {stack}")

for _ in range(1, 6):
	remove = stack.pop()
	print(f"Pop: {remove}")
print(f"Stack: {stack}")





# Python code to demonstrate Implementing
# stack using list
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)

# Removes the last item
print(stack.pop())

print(stack)

# Removes the last item
print(stack.pop())

print(stack)




# Python program to reverse a
# stack using recursion

# Below is a recursive function
# that inserts an element
# at the bottom of a stack.
def insertAtBottom(stack, item):
	if isEmpty(stack):
		push(stack, item)
	else:
		temp = pop(stack)
		insertAtBottom(stack, item)
		push(stack, temp)

# Below is the function that
# reverses the given stack
# using insertAtBottom()
def reverse(stack):
	if not isEmpty(stack):
		temp = pop(stack)
		reverse(stack)
		insertAtBottom(stack, temp)

# Below is a complete running
# program for testing above
# functions.

# Function to create a stack.
# It initializes size of stack
# as 0
def createStack():
	stack = []
	return stack

# Function to check if
# the stack is empty
def isEmpty( stack ):
	return len(stack) == 0

# Function to push an
# item to stack
def push( stack, item ):
	stack.append( item )

# Function to pop an
# item from stack
def pop( stack ):

	# If stack is empty
	# then error
	if(isEmpty( stack )):
		print("Stack Underflow ")
		exit(1)

	return stack.pop()

# Function to print the stack
def prints(stack):
	for i in range(len(stack)-1, -1, -1):
		print(stack[i], end = ' ')
	print()

# Driver Code

stack = createStack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)

reverse(stack)

print("Reversed Stack ")
prints(stack)



# Python program to sort a stack using recursion

# Recursive method to insert element in sorted way


def sortedInsert(s, element):

	# Base case: Either stack is empty or newly inserted
	# item is greater than top (more than all existing)
	if len(s) == 0 or element > s[-1]:
		s.append(element)
		return
	else:

		# Remove the top item and recur
		temp = s.pop()
		sortedInsert(s, element)

		# Put back the top item removed earlier
		s.append(temp)

# Method to sort stack


def sortStack(s):

	# If stack is not empty
	if len(s) != 0:

		# Remove the top item
		temp = s.pop()

		# Sort remaining stack
		sortStack(s)

		# Push the top item back in sorted stack
		sortedInsert(s, temp)

# Printing contents of stack


def printStack(s):
	for i in s[::-1]:
		print(i, end=" ")
	print()


# Driver Code
if __name__ == '__main__':
	s = []
	s.append(30)
	s.append(-5)
	s.append(18)
	s.append(14)
	s.append(-3)

	print("Stack elements before sorting: ")
	printStack(s)

	sortStack(s)

	print("\nStack elements after sorting: ")
	printStack(s)

# This code is contributed by Muskan Kalra.
