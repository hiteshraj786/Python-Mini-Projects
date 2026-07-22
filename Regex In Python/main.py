import urllib.request
from re import findall
import re
#----------------------^^^^^^^^^^^^^^^^^^^^^^^^^------------------

#  MetaCharacters 


# """
# \   --> Used to drop the special meaning of character 
# []  --> Represent a character class 
# ^   --> Matches the beginning 
# $   --> Matches the end 
# .   --> Matches any character except newline 
# |   --> Means 'OR' and It is used to match one pattern or another pattern.
# ?   --> Matches zero or one occurrence 
# *   --> any number of occurrences 
# +   --> one or more occurrences 
# {}  --> Indicate the number of occurrences of a preceding regex to match 
# ()  --> Enclose a group of Regex 

# """

# a = "charlie chchaplin coa and the choclate factory"
# b = "ayushi.jain@gmail.com"
# c = "hello"
# d = "xyz,yz,xyzz,xyyz,xxzzy,zyz,xxyyzz,xyzxyz ,xxyz,xxyyyz"


# match = re.search(r"\.",b)
# match = re.search(r"[@]",b)
# match = re.search(r"[l]",c)
# match = re.findall(r"[l]",c)

# match = re.search(r"^ayu",b)
# match = re.search(r"com$",b)

# match = re.findall(r"c.a",a)

# match = re.findall(r"cha|fac",a)
# match = re.search(r"ali|fac",a)

# match = re.findall(r"ch?a",a)
# match = re.findall(r"ch*a",a)

# match = re.findall(r"xy+z",d)
# match = re.findall(r"y{2,4}",d)
# match = re.findall(r"(x|z)yz",d)

# print(match)

#  -------------------^^^^^^^^^^^^^^^^^^^^----------------------


#   Special Sequences in Regex
# '''
# * Special sequences do not match for the actual character in the string instead it tells the specific location in the search string where the match must occur.

# * It makes it easier to write commonly used paterns 

# \A -> Matches if the string begins with the given character. 


# \b -> Matches if the word begins or ends with the given character. \b(string) will check for the beginning of the word and (string) \b will check for the ending of the word. 

# \B -> it is the opposite of the \b i.e the string should not start  or end with the given regex 


# \d -> Matches any decimal digit, this is equivalent to the set class [0-9]

# \D -> Matches any non-digit character, this is equivalent to the set class [^0-9]

# \s -> Matches any whitespace character 

# \w -> Matches any alphanumeruc character, this is equivalent to the class [a-zA-Z0-9]

# \W -> Matches any non-alphanumeric character. 


# \Z -> Matches if the string ends with the given regex 

# '''

# a = "harry1 potter 23@45"

# match = re.search(r'\Ahar',a)

# match = re.search(r'\bh',a)
# match = re.search(r'h\b',a) #--> None 
# match = re.search(r'er\b',a)

# match = re.search(r'ha\B',a)
# match = re.search(r'\Ber',a)

# match = re.search(r'\d',a)
# match = re.findall(r'\d',a)

# match = re.findall(r'\D',a)

# match = re.findall(r'\s',a)
# match = re.findall(r'\S',a)

# match = re.findall(r'\w',a)
# match = re.findall(r'\W',a)

# match = re.search(r'5\Z',a)
# match = re.findall(r'@5\Z',a)

# print(match)




#  ----------------^^^^^^^^^^^^^^^---------------------------



#   RegEx Sets 🙌🙌

#  --->  A set is a set of characters inside a pair of square brackets [] with a special meaning 


# '''
# [atx] -> returns a match where one of the specified characters (a,t, or x) are present 
# [a-h] -> returns a match for any lower case character, alphabetically between a and h . 
# [^atx] -> returns a match for any character EXCEPT a ,t,and x. 
# [0123] -> Returns a match where any of the specified digits (0,1,2 or 3) are present 
# [0-9]  -> Returns a match for any two-digits numbers from 00 and 79 
# [0-7][0-9] -> Returns a match for any two- digit numbers from 00 and 79 
# [a-zA-z] ->  iska matlab hota hai "A se Z tak koi bhi letter", chahe small letter (a-z) ho ya capital letter (A-Z)  ho vo character return karta hain 
# [+] -> In sets , + , *,.,|,(),$,{} has no special meaning , so [+] means : returns for match for any + character in the string 

# '''

# a  = " charlie and the choclate factory"
# b = "12hi03john@#Z$^67helloHELLO73"

# match = re.findall("[atx]",a)
# match = re.findall("[^atx]",a)
# match = re.findall("[a-t]",a)
# match = re.findall("[1234]",b)
# match = re.findall("[0-9]",b)
# match = re.findall("[0-7[0-9]",b)
# match = re.findall("[a-zA-Z]",b)
# match = re.findall("[$]",b)
# print(match)



#  --------------------^^^^^^^^^^^^^^^^^^^^^^-------------------------

#  Function in RegEx 

# '''
# re.findall() --> Retrun all non-overlapping matches of pattern in  string, as a list of string. The string is scanned left to right, and matches are returned in the order found. 

# re.compile() --> Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches performing string substitutions .

# re.split() --> Split string by the occurrences of a character or a pattern, upon finding that pattern , the remaining characters from the string are returned as part of the resulting list. 

# re.sub()  --> The method returns a string where matched occurrences are replaced with the content of replace variable . 

# re.subn --> subn() is similar to sub() in all ways, except in its way of providing output. It returns a tuple with a count of the total of replacement and the new string rather than just the string. 

# re.escape() --> Returns string with all non-alphanumerics backslashed, this is useful if you want to match an arbitrary literal string that may have 

# re.search() --> This method either returns None (if the pattern doesn't match) , or a re . This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. 
# '''



# a = """John has scored 89 marks 
# Lisa has scored 90 marks 
# David has scored 70 marks"""

# b= "fantastic 5 turtles"


# print(re.findall(r"\d+",a))
# print(re.findall(r'[A-Z][a-z]*',a))

# p = re.compile("[a-d]")
# p = re.compile("\d+")
# print(re.findall(p,a))

# print(re.split("\d+",a))
# print(re.split("\d+",b))


# print(re.sub("\s+","",a))
# print(re.subn("\s+","",a))


# print(re.escape(a))

# print(re.search(r"\d+",a))



#  ------------------^^^^^^^^^^^^^^^^^^^^^^^^^^------------------

#  Match Object: A Match object contains all the information about the search and if there is no match found then None will be returned 

# a =  "John has scored 89 marks"

# match = re.search(r"\d+",a)
# print(match)
# print(match.re)
# print(match.string)
# print(match.start())
# print(match.end())
# print(match.span())
# print(match.group())



# match = re.search(r"\w{2} s",a)
# print(match)
# print(match.re)
# print(match.string)
# print(match.start())
# print(match.end())
# print(match.span())
# print(match.group())



#  -------------------^^^^^^^^^^^^^^^^^^^^------------------------

#  Phone Number and Email Verification and Verification and Web Scrapping Using RegEx


# phn = "222-444-8787"

# if re.search("\d{3}-\d{3}-\d{4}",phn):
#     print("it is a verified number")
# else: 
#     print("incorrect number")



# email = "john78@gmail.com   john@.com   david.989@yahoo.com"
# print(re.findall(r"[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}",email))




# url = "https://www.summet.com/dmsi/html/codesamples/addresses.html"
# a = urllib.request.urlopen(url)
# html = a.read()


# htmlstr = html.decode()

# phn = findall(r"\(\d{3}\) \d{3}-\d{4}",htmlstr)
# for i in phn:
#     print(i)