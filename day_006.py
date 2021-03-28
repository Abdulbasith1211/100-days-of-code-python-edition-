

# Creating a Dictionary 
# with Integer Keys
Dict = {1: 'weebs', 2: 'For', 3: 'weebs'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary 
# with Mixed keys
Dict = {'Name': 'Weebs', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)



# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'weebs', 2: 'For', 3:'weebs'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'weebs'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)



# Creating a Nested Dictionary 
# as shown in the below image
Dict = {1: 'heello', 2: 'hola', 
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}

print(Dict) 





# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'life'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values 
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)




# Python program to demonstrate  
# accessing a element from a Dictionary 

# Creating a Dictionary 
Dict = {1: 'life', 'aint': 'that', 3: 'easy'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['aint'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])





# Creating a Dictionary 
Dict = {1: 'lol', 'name': 'me', 3: 'nerd'}

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))




# Creating a Dictionary
Dict = {'Dict1': {1: 'nvm'},
        'Dict2': {'Name': 'For'}}

# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])






# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'wakanda',
        'A' : {1 : 'weebs', 2 : 'For', 3 : 'life'},
        'B' : {1 : 'noob', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)




# Creating a Dictionary

# Creating a Dictionary
Dict = {1: 'my', 'name': 'is your', 3: 'name'}

# Deleting a key 
# using pop() method
pop_ele = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('Value associated to poped key is: ' + str(pop_ele))




# Creating Dictionary
Dict = {1: 'your', 'my': 'our', 3: 'name'}

# Deleting an arbitrary key
# using popitem() function
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))




# Creating a Dictionary
Dict = {1: 'hey', 'name': 'me', 3: 'weeb'}


# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)






# Python code to demonstrate working of
# str() and items()

# Initializing dictionary
dic = { 'Name' : 'Kaneki', 'Age' : 17 }

# using str() to display dic as string
print ("The constituents of dictionary as string are : ")
print (str(dic))

# using str() to display dic as list
print ("The constituents of dictionary as list are : ")
print (dic.items())





# Python code to demonstrate working of
# len() and type()

# Initializing dictionary
dic = { 'Name' : 'Kaneki ken', 'Age' : 17, 'ID' : 2541997 }

# Initializing list
li = [ 1, 3, 5, 6 ]

# using len() to display dic size
print ("The size of dic is : ",end="")
print (len(dic))

# using type() to display data type
print ("The data type of dic is : ",end="")
print (type(dic))

# using type() to display data type
print ("The data type of li is : ",end="")
print (type(li))







# Python code to demonstrate working of
# clear() and copy()

# Initializing dictionary
dic1 = { 'Name' : 'zoro', 'Age' : 19 }

# Initializing dictionary 
dic3 = {}

# using copy() to make shallow copy of dictionary
dic3 = dic1.copy()

# printing new dictionary
print ("The new copied dictionary is : ")
print (dic3.items())

# clearing the dictionary
dic1.clear()

# printing cleared dictionary
print ("The contents of deleted dictionary is : ",end="")
print (dic1.items())





# Python code to demonstrate working of
# fromkeys() and update()

# Initializing dictionary 1
dic1 = { 'Name' : 'Luffy', 'Age' : 19 }

# Initializing dictionary 2
dic2 = { 'ID' : 2541997 }

# Initializing sequence
sequ = ('Name', 'Age', 'ID')

# using update to add dic2 values in dic 1
dic1.update(dic2)

# printing updated dictionary values
print ("The updated dictionary is : ")
print (str(dic1))

# using fromkeys() to transform sequence into dictionary
dict = dict.fromkeys(sequ,5)

# printing new dictionary values
print ("The new dictionary values are : ")
print (str(dict))





# Python code to demonstrate working of
# has_key() and get()




# Python code to demonstrate working of
# setdefault()

# Initializing dictionary
dict = { 'Name' : 'Usopp', 'Age' : 19 }

# using setdefault() to print a key value
print ("The value associated with Age is : ",end="")
print (dict.setdefault('ID', "No ID"))

# printing dictionary values
print ("The dictionary values are : ")
print (str(dict))



# Function to find majority element
from collections import Counter

def majority(arr):

    # convert array into dictionary
    freqDict = Counter(arr)

    # traverse dictionary and check majority element
    size = len(arr)
    for (key,val) in freqDict.items():
         if (val > (size/2)):
             print(key)
             return
    print('None')

# Driver program
if __name__ == "__main__":
    arr = [3,3,4,2,4,4,2,4,4] 
    majority(arr)


#end of day 6 code