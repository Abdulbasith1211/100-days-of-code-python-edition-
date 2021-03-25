
# Python program to illustrate
# while loop
count = 0
while (count < 5):    
    count = count + 1
    print("COYG")



#Python program to illustrate
# combining else with while
count = 0
while (count <= 5):    
    count = count + 1
    print("COYG")
else:
    print("COYG AGAIN")



# Python program to illustrate for loop
# Iterating over range 0 to n-1

n = 7
for i in range(0, n):
    print(i)



# Python program to illustrate
# Iterating over a list
print("List Iteration eg")
l = ["Come ", "on", "you", "gooner"]
for i in l:
    print(i)
     
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("Come", "on", "you", "gooner")
for i in t:
    print(i)
     
# Iterating over a String
print("\nString Iteration")    
s = "Gooner"
for i in s :
    print(i)
     
# Iterating over dictionary
print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 231
d['abc'] = 211
for i in d :
    print("%s  %d" %(i, d[i]))



# Python program to illustrate
# Iterating by index

list = ["Gonner", "for", "life"]
for index in range(len(list)):
    print (list[index])



# Python program to illustrate
# combining else with for loop

list = ["Gooner", "for", "life"]
for index in range(len(list)):
    print (list[index])
else:
    print("Not givin up")    




# Python program to illustrate 
# nested for loops in Python

for i in range(2, 10):
    for j in range(i):
         print(i, end=' ')
    print()


# Prints all letters except 'e' and 's'
for letter in 'gooner for sev': 
    if letter == 'e' or letter == 's':
         continue
    print ('Current Letter :', letter)
  





# Python program for an empty loop
for letter in 'server':
    pass
print ('Last Letter :', letter)


# A simple for loop example

giv_fruits = ["apricot", "guava", "passionfruit"]

for fruit in giv_fruits:

 print(fruit)




# python3 code to 
# illustrate the 
# difference between
# == and is operator
# [] is an empty list
list1 = []
list2 = []
list3=list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:    
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:    
    print("False")


fruits = ["apple", "orange", "kiwi"]

# Creating an iterator object 
# from that iterable i.e fruits
iter_obj = iter(fruits)

# Infinite while loop
while True:
  try:
      
      # getting the next item
      fruit = next(iter_obj)
      print(fruit)
  except StopIteration:
       
      # if StopIteration is raised, 
      # break from loop
       break


 
# A C-style way of accessing list elements
players = ["Ronaldo", "Messi", "Auba"]
i = 0
while (i < len(players)):
    print (players[i])
    i += 1
   
 

#Accessing items using for-in loop

players=["auba", "saka", "odegaard"]
for i in players:
    print(i)


#Accessing items using indexes and for-in

players=["auba", "saka", "odegaard"]
for i in range(len(players)):
    print(players[i])

#Accessing items using enumerate()

players=["laca", "saka", "xhaka"]
for i,y in enumerate(players):
    print(y)



# Accessing items and indexes enumerate()

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars):
    print (x[0], x[1])



# demonstrating the use of start in enumerate

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars, start=1):
    print (x[0], x[1])




# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

# Single dictionary holds prices of cars and 
# its accessories.
# First three items store prices of cars and
# next two items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$",
          4:"8900$", 5:"4500$"}

# Printing prices of cars
for index, c in enumerate(cars, start=1):
    print ("Car: %s Price: %s"%(c, prices[index]))

# Printing prices of accessories
for index, a in enumerate(accessories,start=1):
    print ("Accessory: %s Price: %s"\
           %(a,prices[index+len(cars)]))




# Python program to demonstrate the working of zip

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit", 
               "Dolby sound kit"]

# Combining lists and printing
for c, a in zip(cars, accessories):
    print ("Car: %s, Accessory required: %s"\
          %(c, a))




# Python program to demonstrate unzip (reverse 
# of zip)using * with zip function

# Unzip lists
l1,l2 = zip(*[('Aston', 'GPS'), 
              ('Audi', 'Car Repair'), 
              ('McLaren', 'Dolby sound kit') 
           ])

# Printing unzipped lists      
print(l1)
print(l2)





# Python 3.x program to check if an array consists 
# of even number
def even_number(l):
    for num in l:
        if num % 2 == 0:
            print ("list contains an even number")
            break

    # This else executes only if break is NEVER
    # reached and loop terminated after all iterations.
    else:     
        print ("list does not contain an even number")

# Driver code
print ("For List 1:")
even_number([1, 9, 8])
print (" \nFor List 2:")
even_number([1, 3, 5])




count = 0
while (count < 1):    
    count = count+1
    print(count)
    break
else:
    print("No Break")



#

# Python code to demonstrate range() vs xrange()
# on  basis of operations usage 

# initializing a with range()
a = range(1,6)


# testing usage of slice operation on range()
# prints without error
print ("The list after slicing using range is : ")
print (a[2:5])


#end of day 2

