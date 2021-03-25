
# Python3 program to show that 
# a string can be appended to a string.

a = 'Yikes'

# output is displayed
print(a)
a = a + 'for what'

print(a) # works fine





# Python3 program to show that
# both string hold same identity

string1 = "YOLO"
string2 = "YOLO"

print(id(string1))
print(id(string2))




# Modifying a string

string1 = "Hello"

# identity of string1
print(id(string1))

string1 += "World"
print(string1)

# identity of modified string1
print(id(string1))




print("Hi Mr Robot.")

# use of escape sequence
print("He said, \"Welcome to Wakanda\"")    

print('Hey so happy to be here')

# use of mix quotes
print ('Getting cocky, "huh"')        


 
# A python program to illustrate 
# print substrings of a string 
x = "Welcome to Wakanda"

# Prints substring from 2nd to 5th character 
print (x[2:5])     

# Prints substring stepping up 2nd character 
# from 4th to 10th character 
print (x[4:10:2])     

# Prints 3rd character from rear from 3 to 5 
print (x[-4:-3])       




# Python code to demonstrate working of 
# find() and rfind()
str = "weebs  community is  for weebs"
str2 = "weebs"

# using find() to find first occurrence of str2
# returns 25
print ("The first occurrence of str2 is at : ", end="")
print (str.find( str2, 4) )

# using rfind() to find last occurrence of str2
# returns 21
print ("The last occurrence of str2 is at : ", end="")
print ( str.rfind( str2, 4) )




# Python code to demonstrate working of 
# startswith() and endswith() 
str = "weebs"
str1 = "weebsforlife"

# using startswith() to find if str 
# starts with str1 
if str1.startswith(str): 
        print ("str1 begins with : " + str) 
else : print ("str1 does not begin with : "+ str) 

# using endswith() to find 
# if str ends with str1 
if str1.endswith(str): 
    print ("str1 ends with : " + str) 
else : 
    print ("str1 does not end with : " + str) 






# Python code to demonstrate working of 
# isupper() and islower()
str = "wEEBsforWEEbs"
str1 = "weebs"

# checking if all characters in str are upper cased
if str.isupper() :
    print ("All characters in str are upper cased")
else : 
    print ("All characters in str are not upper cased")

# checking if all characters in str1 are lower cased
if str1.islower() :
    print ("All characters in str1 are lower cased")
else : 
    print ("All characters in str1 are not lower cased")



 
# Python code to demonstrate working of 
# upper(), lower(), swapcase() and title()
str = "WeebCommunity is fOr WeeEBs"

# Coverting string into its lower case
str1 = str.lower()
print (" The lower case converted string is : " + str1)

# Coverting string into its upper case
str2 = str.upper()
print (" The upper case converted string is : " + str2)

# Coverting string into its swapped case
str3 = str.swapcase()
print (" The swap case converted string is : " + str3)

# Coverting string into its title case
str4 = str.title()
print (" The title case converted string is : " + str4)




# Python code to demonstrate working of 
# len() and count()
str = "wubba lubba dub dub"
 
# Printing length of string using len()
print (" The length of string is : ", len(str))

# Printing occurrence of "geeks" in string
# Prints 2 as it only checks till 15th element
print (" Number of appearance of ""dub"" is : ",end="")
print (str.count("dub",0,15))



# Python code to demonstrate working of 
# center(), ljust() and rjust()
str = "wubbalubbadubdub"
 
# Printing the string after centering with '-'
print ("The string after centering with '-' is : ",end="")
print ( str.center(20,'-'))

# Printing the string after ljust()
print ("The string after ljust is : ",end="")
print ( str.ljust(20,'-'))

# Printing the string after rjust()
print ("The string after rjust is : ",end="")
print ( str.rjust(20,'-'))



# Python code to demonstrate working of 
# isalpha(), isalnum(), isspace()
str = "likesforlikes"
str1 = "231211"
 
# Checking if str has all alphabets 
if (str.isalpha()):
       print ("All characters are alphabets in str")
else : print ("All characters are not alphabets in str")

# Checking if str1 has all numbers
if (str1.isalnum()):
       print ("All characters are numbers in str1")
else : print ("All characters are not numbers in str1")

# Checking if str1 has all spaces
if (str1.isspace()):
       print ("All characters are spaces in str1")
else : print ("All characters are not spaces in str1")




# Python code to demonstrate working of 
# join()
str = "_"
str1 = ( "omou", "wa", "shinderou" )

# using join() to join sequence str1 with str
print ("The string after joining is : ", end="")
print ( str.join(str1))



# Python code to demonstrate working of 
# strip(), lstrip() and rstrip()
str = "---kanouitokanna---"

# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )

# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )

# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )




# Python code to demonstrate working of 
# min() and max()
str = "sedlifebro"

# using min() to print the smallest character
# prints 'e'
print ("The minimum value character is : " + min(str))

# using max() to print the largest character
# prints 's'
print ("The maximum value character is : " + max(str))






# Python code to demonstrate working of 
# replace()

str = "weebsneedweebs for survival"

str1 = "weebs"
str2 = "nerds"

# using replace() to replace str2 with str1 in str
# only changes 2 occurrences 
print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2)) 




# Python code to illustrate expandtabs()
string = 'WEEBS\tFOR\tLIFE'

# No parameters, by default size is 8
print (string.expandtabs())

# tab size taken as 2
print(string.expandtabs(2))

# tab size taken as 5
print(string.expandtabs(5))

# Python code to illustrate expandtabs()
string = 'WEEBS\tFOR\tLIFE'

# No parameters, by default size is 8
print (string.expandtabs())

# tab size taken as 2
print(string.expandtabs(2))

# tab size taken as 5
print(string.expandtabs(5))




# Python code to convert string to list

def Convert(string):
    li = list(string.split(" "))
    return li

# Driver code    
str1 = "Weens for Beans"
print(Convert(str1))




# Python code to find the URL from an input string
# Using the regular expression
import re

def Find(string):

    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
    
# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/'
print("Urls: ", Find(string))



# Python Program for
# Creation of String

# Creating a String 
# with single Quotes
String1 = 'Welcome to the Noobs World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Noob"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String
# with triple Quotes
String1 = '''I'm a noob and I live in a world of "weebs"'''
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Noobs
            For
            Life'''
print("\nCreating a multiline String: ")
print(String1)



# Python Program to Access
# characters of String

String1 = "Weebsyoweebs"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])



# Python Program to Access
# characters of String

String1 = "yikes i love ya"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])




# Python Program to
# demonstrate String slicing

# Creating a String
String1 = "hellavafun"
print("Initial String: ") 
print(String1)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between 
# 3rd and 2nd last character
print("\nSlicing characters between " +
    "3rd and 2nd last character: ")
print(String1[3:-2])



# Python Program to Update
# entire String

String1 = "Hello, I'm a NEET"
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Transferred to the fantasy World"
print("\nUpdated String: ")
print(String1)




# Python Program for
# Escape Sequencing 
# of String

# Initial String
String1 = '''Im a "noob"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quote 
String1 = 'Im a "noob"'
print("\nEscaping Single Quote: ")
print(String1)

# Escaping Doule Quotes
String1 = "Im a \"noob\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the 
# use of Escape Sequences
String1 = "C:\\Python\\noob\\"
print("\nEscaping Backslashes: ")
print(String1)





# Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)

# Using raw String to 
# ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)




# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Weebs', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Weebs', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g = 'Weebs', f = 'For', l = 'Life')
print("\nPrint String in order of Keywords: ")
print(String1)




# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)



# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces 
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)





# Python Program for
# Old Style Formatting
# of Integers

Integer1 = 1212.3456789
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' %Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %3.4f' %Integer1)




# Python program to illustrate
# Matching regex objects
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 425-534-4241.')
print('Phone number found: ' + mo.group())

#end of day 3


