#DAY 12 - (ARRAYS)

# Python code to demonstrate the working of
# array(), append(), insert()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print ("The new created array is : ",end=" ")
for i in range (0, 3):
	print (arr[i], end=" ")

print("\r")

# using append() to insert new value at end
arr.append(4);

# printing appended array
print("The appended array is : ", end="")
for i in range (0, 4):
	print (arr[i], end=" ")
	
# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)

print("\r")

# printing array after insertion
print ("The array after insertion is : ", end="")
for i in range (0, 5):
	print (arr[i], end=" ")







# Python code to demonstrate the working of
# pop() and remove()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr= array.array('i',[1, 2, 3, 1, 5])

# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
	print (arr[i],end=" ")

print ("\r")

# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2));

# printing array after popping
print ("The array after popping is : ",end="")
for i in range (0,4):
	print (arr[i],end=" ")

print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print ("The array after removing is : ",end="")
for i in range (0,3):
	print (arr[i],end=" ")






# Python code to demonstrate the working of
# index() and reverse()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr= array.array('i',[1, 2, 3, 1, 2, 5])

# printing original array
print ("The new created array is : ",end="")
for i in range (0,6):
	print (arr[i],end=" ")

print ("\r")

# using index() to print index of 1st occurrenece of 2
print ("The index of 1st occurrence of 2 is : ",end="")
print (arr.index(2))

#using reverse() to reverse the array
arr.reverse()

# printing array after reversing
print ("The array after reversing is : ",end="")
for i in range (0,6):
	print (arr[i],end=" ")






# Python code to demonstrate the working of
# typecode, itemsize, buffer_info()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr= array.array('i',[1, 2, 3, 1, 2, 5])

# using typecode to print datatype of array
print ("The datatype of array is : ")
print (arr.typecode)

# using itemsize to print itemsize of array
print ("The itemsize of array is : ")
print (arr.itemsize)

# using buffer_info() to print buffer info. of array
print ("The buffer info. of array is : ")
print (arr.buffer_info())




# Python code to demonstrate the working of
# count() and extend()

# importing "array" for array operations
import array

# initializing array 1 with array values
# initializes array with signed integers
arr1 = array.array('i',[1, 2, 3, 1, 2, 5])

# initializing array 2 with array values
# initializes array with signed integers
arr2 = array.array('i',[1, 2, 3])

# using count() to count occurrences of 1 in array
print ("The occurrences of 1 in array is : ")
print (arr1.count(1))

# using extend() to add array 2 elements to array 1
arr1.extend(arr2)

print ("The modified array is : ")
for i in range (0,9):
	print (arr1[i])



# Python code to demonstrate the working of
# fromlist() and tolist()

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i',[1, 2, 3, 1, 2, 5])

# initializing list
li = [1, 2, 3]

# using fromlist() to append list at end of array
arr.fromlist(li)

# printing the modified array
print ("The modified array is : ",end="")
for i in range (0,9):
	print (arr[i],end=" ")

# using tolist() to convert array into list
li2 = arr.tolist()

print ("\r")

# printing the new list
print ("The new list created is : ",end="")
for i in range (0,len(li2)):
	print (li2[i],end=" ")





