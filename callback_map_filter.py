

'''
Call Back-functions:
A function passed as a parameter or used inside a function
'''

def addtion(a,b,fun):
    return fun(a+b)
def is_even(n):
    return n%2==0
print(addtion(1,5,is_even))

'''
Higher order functions
-->A function which takes another function as a parameter 
(or)
-->A function which returns a function or both

==> MAP -->Always returns the boolean values
==>FILTER-->Returns Values
'''

s=[1,2,4,5,7,8,9,10]
print(list(map(lambda x : x%2==0,s)))
print(list(filter(lambda x : x%2==0,s)))



# Todays Python tasks

# Task 1: Square All Numbers Using map()
# Given a list of numbers, create a new list containing their squares using map().
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
lo=[1,2,3,4,5]
print(list(map(lambda x:x*x,lo)))

# Task 2: Filter Even Numbers Using filter()
# Given a list of numbers, filter out only the even numbers using filter().
# Input: [10, 15, 22, 33, 40]
# Expected Output: [10, 22, 40]
li=[10, 15, 22, 33, 40]
print(list(filter(lambda x:x%2==0,li)))


# Task 3: Convert All Strings to Uppercase Using map()
# Given a list of lowercase words, convert all words to uppercase using map().
# Input: ['apple', 'banana', 'cherry']
# Expected Output: ['APPLE', 'BANANA', 'CHERRY']
fruits=['apple', 'banana', 'cherry']
print(list(map(lambda x:x.lower(),fruits)))



# Task 4: Filter Words Starting with 'a' Using filter()
# Given a list of words, filter out only the words that start with the letter 'a'.
# Input: ['apple', 'banana', 'apricot', 'grape', 'avocado']
# Expected Output: ['apple', 'apricot', 'avocado']
fi=['apple', 'banana', 'apricot', 'grape', 'avocado']
print(list(filter(lambda x:x[0]=='a',fi)))

# Task 5: Find the Length of Each Word Using map()
# Given a list of words, find the length of each word using map().
# Input: ['hello', 'world', 'python']
# Expected Output: [5, 5, 6]
words=['hello', 'world', 'python']
print(list(map(lambda x:len(x),words)))

# Task 6: Filter Out Numbers Less Than 10
# Given a list of numbers, filter out numbers that are less than 10 using filter().
# Input: [4, 11, 7, 20, 3, 15]
# Expected Output: [11, 20, 15]
nums=[4, 11, 7, 20, 3, 15]
print(list(filter(lambda x:x<10,nums)))



# Task 7: Double Each Number Using map()
# Given a list of numbers, double each number using map().
# Input: [1, 2, 3, 4]
# Expected Output: [2, 4, 6, 8]
nu=[1, 2, 3, 4]
print(list(map(lambda x:x*2,nu)))




# Task 8: Filter Names Longer Than 5 Characters
# Given a list of names, filter out names longer than 5 characters using filter().
# Input: ['John', 'Elizabeth', 'Sam', 'Chris', 'Amanda']
# Expected Output: ['Elizabeth', 'Amanda']
names=['John', 'Elizabeth', 'Sam', 'Chris', 'Amanda']
print(list(filter(lambda x:len(x)>5,names)))


# Task 9: Add Exclamation Mark to Each Word
# Given a list of words, add an exclamation mark at the end of each word using map().
# Input: ['python', 'java', 'ruby']
# Expected Output: ['python!', 'java!', 'ruby!']
pro=['python', 'java', 'ruby']
print(list(map(lambda x:x+'!',pro)))


# Task 10: Filter Numbers That Are Multiples of 3
# Given a list of numbers, filter out only those that are multiples of 3 using filter().
# Input: [3, 4, 9, 10, 15, 17, 21]
# Expected Output: [3, 9, 15, 21]
fact_3=[3, 4, 9, 10, 15, 17, 21]
print(list(filter(lambda x:x%3==0,fact_3)))