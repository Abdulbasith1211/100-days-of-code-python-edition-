

# Python program to demonstrate 
# Creation of List 

# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["tricks", "For", "treats"]
print("\nList Items: ")
print(List[0]) 
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['sugarcrush', 'all'] , ['day']]
print("\nMulti-Dimensional List: ")
print(List)





# Creating a List with 
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a List with 
# mixed type of values
# (Having numbers and strings)
List = [1, 2, ';lulz', 4, 'For', 6, 'sporiano']
print("\nList with the use of Mixed Values: ")
print(List)




# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))




# Python program to demonstrate 
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements 
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'yours truly']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)




# Python program to demonstrate 
# Addition of elements in a List
 
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of Element at 
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Ritsu')
print("\nList after performing Insert Operation: ")
print(List)



# Python program to demonstrate 
# Addition of elements in a List
  
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Weebs', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)




# Python program to demonstrate 
# accessing of element from list

# Creating a List with
# the use of multiple values
List = ["you", "only", "once"]

# accessing a element from the 
# list using index number
print("Accessing a element from the list")
print(List[0]) 
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Feel', 'For'] , ['Good']]

# accessing an element from the 
# Multi-Dimensional List using
# index number
print("Acessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])




List = [1, 2, 'Tricks', 4, 'For', 6, 'Treats']

# accessing a element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list 
print(List[-3])





# Python program to demonstrate 
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6, 
        7, 8, 9, 10, 11, 12]
print("Intial List: ")
print(List)

# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)

# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)



List = [1,2,3,4,5]

# Removing element from the 
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a 
# specific location from the 
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)





# Python program to demonstrate 
# Removal of elements in a List

# Creating a List
List = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
print("Intial List: ")
print(List)

# Print elements of a range
# using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

# Print elements from a 
# pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)

# Printing elements from
# beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)





# Creating a List
List = ['G','E','T','L','U','C',
        'C','K','Y','B','O','Y','H']
print("Initial List: ")
print(List)

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

# Print elements of a range
# using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)



# Python code to demonstrate the working of
# "in" and "not in" 
# initializing list
lis = [1, 4, 3, 2, 5]

# checking if 4 is in list using "in"
if 4 in lis:
        print ("List is having element with value 4")
else :  print ("List is not having element with value 4")

# checking if 4 is not list using "not in"
if 4 not in lis:
        print ("List is not having element with value 4")
else :  print ("List is having element with value 4")





# Python code to demonstrate the working of
# len(), min() and max()
# initializing list 1
lis = [2, 1, 3, 5, 4,8,9]

# using len() to print length of list
print ("The length of list is : ", end="")
print (len(lis))

# using min() to print minimum element of list
print ("The minimum element of list is : ", end="")
print (min(lis))

# using max() to print maximum element of list
print ("The maximum element of list is : ", end="")
print (max(lis))



# Python code to demonstrate the working of
# "+" and "*"
# initializing list 1
lis = [1, 2, 3]

# initializing list 2
lis1 = [4, 5, 6]

# using "+" to concatenate lists
lis2= lis + lis1

# priting concatenated lists
print ("list after concatenation is : ", end="")
for i in range(0,len(lis2)):
         print (lis2[i], end=" ")
         
print ("\r")

#using '*' to combine lists 
lis3 = lis * 3

# priting combined lists
print ("list after combining is : ", end="")
for i in range(0,len(lis3)):
         print (lis3[i], end=" ")




# Python code to demonstrate the working of
# index() and count()
# initializing list 1
lis = [2, 1, 3, 5, 4, 3]

# using index() to print first occurrence of 3
# prints 5
print ("The first occurrence of 3 after 3rd position is : ", end="")
print (lis.index(3, 3, 6))

# using count() to count number of occurrence of 3
print ("The number of occurrences of 3 is : ", end="")
print (lis.count(3))



# Adds List Element as value of List.
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)



List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List.insert(2,10087)     
print(List)        



List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]

# Add List2 to List1
List1.extend(List2)        
print(List1)

# Add List1 to List2 now
List2.extend(List1) 
print(List2)



#python program using sum 
List = [1, 2, 3, 4, 5]
print(sum(List))

#pthon program to count
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))



List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]

"""index(element, start, end) : It will calculate till index end-1. """

# will check from index 2 to 4.
print("After checking in index range 2 to 4")
print(List.index(2,2,5))



#python program using max()

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(max(List))


#python program using sort() and reverse()
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

#Reverse flag is set True`
List.sort(reverse=True) 

#List.sort().reverse(), reverses the sorted list  
print(List)        




List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(0))





# Python code to sort a list by creating 
# another list Use of sorted()
def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2
    

lst = ["rohan", "amy", "sapna", "muhammad", 
       "aakash", "jackson", "chinmay"]
print(Sorting(lst))




# Python code to sort a list without 
# creating another list Use of sort()
def Sorting(lst):
    lst.sort(key=len)
    return lst
    
# Driver code
lst = ["rohan", "amy", "sapna", "muhammad", 
       "aakash", "jackson", "chinmay"]
print(Sorting(lst))


import numpy

def Sorting(lst):

    # list for storing the length of each string in list 
    lenlist=[]   
    for x in lst:
         lenlist.append(len(x))     

    # return a list with the index of the sorted
    # items in the list
    sortedindex = numpy.argsort(lenlist)  

    # creating a dummy list where we will place the 
    # word according to the sortedindex list 
    lst2 = ['dummy']*len(lst)   

    # print(sortedindex,lenlist)
    for i in range(len(lst)):    

        # placing element in the lst2 list by taking the
        # value from original list lst where it should belong 
        # in the sorted list by taking its index from sortedindex
        lst2[i] = lst[sortedindex[i]]     
                                        
    return lst2
    
# Driver code
lst = ["rohan", "amy", "sapna", "muhammad", 
       "aakash", "raunak", "chinmoy"]
print(Sorting(lst))




# Python program to illustrate union
# Maintained repetition 
def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))



# Python program to illustrate union
# Maintained repetition and order 
def Union(lst1, lst2):
    final_list = sorted(lst1 + lst2)
    return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))



# Python program to illustrate union
# Without repetition 
def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))




# Python program to illustrate union
# Union of three lists
def Union(lst1, lst2, lst3):
    final_list = list(set().union(lst1, lst2, lst3))
    return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
lst3 = [4, 78, 5, 6, 9, 25, 64, 32, 59]
print(Union(lst1, lst2, lst3))




# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))




# Python program to illustrate the intersection
# of two lists using set() method
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))





# Python program to illustrate the intersection
# of two lists using set() and intersection()
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)
    
# Driver Code
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))




# Python program to illustrate the intersection
# of two lists
def intersection(lst1, lst2):

    # Use of hybrid method
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3

# Driver Code
lst1 = [9, 9, 74, 21, 45, 11, 63]
lst2 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
print(intersection(lst1, lst2))




# Python program to illustrate the intersection
# of two lists, sublists and use of filter()
def intersection(lst1, lst2):
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    return lst3

# Driver Code
lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print(intersection(lst1, lst2))


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




# Python code to demonstrate Implementing 
# Queue using list
queue = ["Amar", "Akbar", "Anthony"]
queue.append("Ram")
queue.append("Iqbal")
print(queue)

# Removes the first item
print(queue.pop(0))

print(queue)

# Removes the first item
print(queue.pop(0))

print(queue)



# Python code to demonstrate Implementing 
# Stack using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.pop())                 
print(queue.pop())                 
print(queue)




# Python code to demonstrate Implementing 
# Queue using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())                 
print(queue.popleft())                 
print(queue)



# Python program to count the 
# number of numbers in a given range
# using traversal and mutliple line code

def count(list1, l, r):
    c = 0 
    # traverse in the list1
    for x in list1:
        # condition check
        if x>= l and x<= r:
            c+= 1 
    return c
    
# driver code
list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
l = 40
r = 80 
print (count(list1, l, r))



# Function to find intersection of two arrays

def interSection(arr1,arr2):

     # filter(lambda x: x in arr1, arr2)  -->
     # filter element x from list arr2 where x
     # also lies in arr1
     result = list(filter(lambda x: x in arr1, arr2)) 
     print ("Intersection : ",result)

# Driver program
if __name__ == "__main__":
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    interSection(arr1,arr2)




#Creating a Tuple
#with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'wakanda')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

#Creating a Tuple
#with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('wakanda', 'forever')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

#Creating a Tuple
#with repetition
Tuple1 = ('weebs',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

#Creating a Tuple 
#with the use of loop
Tuple1 = ('noobs')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)




#Accessing Tuple
#with Indexing
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[1])


#Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")

#This line unpack 
#values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)




# Concatenaton of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('weebs', 'For', 'life')

Tuple3 = Tuple1 + Tuple2

# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)

# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)

# Printing Final Tuple
print("\nTuples after Concatenaton: ")
print(Tuple3)




# Slicing of a Tuple

# Slicing of a Tuple
# with Numbers
Tuple1 = tuple('WEEBSFORNEEDS')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple 
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])



# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))



# Python code to count the number of occurrences
def countX(lst, x):
    return lst.count(x)

# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))




# Python code to sort a list of tuples 
# according to given key.

# get the last key.
def last(n):
    return n[m]  
 
# function to sort the tuple   
def sort(tuples):

    # We pass used defined function last
    # as a parameter. 
    return sorted(tuples, key = last)
 
# driver code  
a = [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
m = 2
print("Sorted:"),
print(sort(a))





# Reversing a tuple using slicing technique
# New tuple is created
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup
    
# Driver Code
tuples = ('z','a','d','f','g','e','e','k')
print(Reverse(tuples))



# Reversing a list using reversed()
def Reverse(tuples):
    new_tup = ()
    for k in reversed(tuples):
        new_tup = new_tup + (k,)
    print (new_tup)

# Driver Code
tuples = (10, 11, 12, 13, 14, 15)
Reverse(tuples)



# Python program to remove empty tuples from a 
# list of tuples function to remove empty tuples 
# using list comprehension
def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples

# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))



# Python program to remove empty tuples from 
# a list of tuples function to remove empty 
# tuples using filter
def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples

# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print (Remove(tuples))



# Python program to print 
# duplicates from a list 
# of integers
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40, 
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))
    

#end of day 5





