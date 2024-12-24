#Lists-:
#A.Create an empty list and add 5 user-input integers to it:
# numbers = []
# for i in range(5):
#     numbers.append(int(input("Enter a number: ")))
#     print(numbers)



#B.Take a list of integers as input and print the sum of all the elements in the list:
# numbers = []
# for i in range(5):
#     numbers.append(int(input("Enter number: ")))
#     print(sum(numbers))



#C.Ask the user for a sentence and store each word as an element in a list.:
# sentence = input("Please enter your sentence:")
# words = sentence.split()
# print(words)


#D.Write a program that asks user for six countries. The program should create a list of
# those countries and ask for three countries to delete from the list. Make the program
# user-friendly, and print each time the content of a list to show the user which countries
# are in a list.:
# countries = []
# for i in range(6):
#     countries.append(input("Enter to country:"))
#     print(countries)


#E.Which list method makes any list look the same. The lists are the same if its content,
# elements and all other properties are the same.:
# list1 = [1,2,3,4,5]
# list2 = [1,2,3,4,5]
# if list1 == list2:
#     print("The lists are the same:")
# else:
#     print("The lists are not the same:")



#F.Create an empty list and print its length. Write a function that accepts a list of names and returns the name with the longest length.: 
# names = ["John", "Jane", "Bob", "Alice"]

# def longest_name(names):
#     longest_name = ""
#     for name in names:
#         if len(name) > len(longest_name):
#             longest_name = name
#             return longest_name
        
# print(longest_name(names))



#G.Ask the user for a list of integers and find the second - largest number in the list:
# numbers = []
# for i in range(5):
#     numbers.append(int(input("Enter number: ")))
#     print(max(numbers))



#H. Ask the user for a list of integers and find the mean value of that list.:
# numbers = []
# for i in range(4):
#     numbers.append(int(input("Enter first number: ")))
#     numbers.append(int(input("Enter second number: ")))
#     numbers.append(int(input("Enter third number: ")))
#     numbers.append(int(input("Enter fourth number: ")))
#     print(sum(numbers) / len(numbers))



#I. Ask the user for a list of integers and find the third-smallest number in the list.:
# numbers = []
# for x in range(5):
#     numbers.append(int(input("Enter number: ")))
#     numbers.sort()

# print(numbers[2])



#J.Write a program that asks the user for three colors separated by spaces. The
# program should print all those colors using comma (you should use string 'join' method). 
# For example:
# Your colors are red, blue, white.:
# colors = ["red", "blue", "white"]
# print(",".join(colors))




#K.Write a program that asks the user for four capital cities separated by spaces. 
# The program should print all those cities the following structure:
# There are many capital cities in the world. For example, Baku, Moscow and Kyiv.

# You should follow all instructions, and not make changes to the structure of final sentence.:
# cities = ["Baku", "Moscow", "Kyiv"]
# print("There are many capital cities in the world. For example, " + ", ".join(cities))




#L. Take a list of strings as input and sort it in alphabetical order.:
# words = ["apple", "banana", "orange", "grape", "apple", "kiwi"]
# words.sort()
# print(words)


#M. Take a list of numeric values as input and sort it in descending order.:
# numbers = [2,4,6,8,4,10,4,12,14]
# numbers.sort(reverse=True)
# print(numbers)


#N. Remove duplicates from a list entered by the user while preserving the original order.:
# num = [2,4,6,8,4,10,4,12,14]
# print(set(num))


#O. Write a program that accepts two lists and concatenates them into a single list.:
# lst = [1,2,3,4,5]
# lst2 = [6,7,8,9,10]
# print(lst + lst2)


#P. Write a program that prints 'True' if there is at least one item in a 'my_list' list.:
# my_list = [2,3,4,5,6,7]
# if len(my_list) > 0:
#     print("True")
# else:
#     print("False")




#List Comprehension-:
# Suppose you have the following lists:
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# letters = ['p', 'y', 't', 'h', 'o', 'n']
# times = [1, 2, 3, 4, 5]

#A.Create a list containing raised to power two values of 'digits' list:
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([x**2 for x in digits])


#B.Create a list containing capitalized version of letter values of 'letters' list:
# letters = ['p', 'y', 't', 'h', 'o', 'n']
# print([x.upper() for x in letters])


#C. Create a list containing the 'Comprehension' string value the amount of 'times'
# list's length time.:
# times = [1,2,3,4,5]
# print("Comprehension" * len(times))


#D. Create a list containing 5 random integers between -5 and 5. find the second-smallest 
# number in the list. The program should print 'True' if that number is negative, and 'False'
# otherwise.:
# import random

# numbers = [random.randint(-5, 5) for _ in range(5)]
# numbers.sort()

# if numbers[1] < 0:
#     print("True")
# else:
#     print("False")



#E. Create a list of 10 random numbers and find the maximum and minimum values.:
# import random

# numbers = [random.randint(0, 100) for _ in range(10)]
# print(max(numbers))
# print(min(numbers))


#- Chat GPT's Homework -:
#A. Create a list of colors and write a function that duplicates each color in the 
# list. For example, if the list contains "red," it should become ["red", "red"]. 
# Print the modified list.:
# colors = ["red", "blue", "green"]
# def dublicate_color(colors):
#     return [ color for color in colors for _ in range(2)]

# print(dublicate_color(colors))


#B.How many methods do you know to create an empty list in Python? :
#There are 2 methods: list() and []


#C. Which list method is used to add an element to the end of a list?:
# append() method is used to add an element to the end of a list.

#D. Write a Python code snippet to access the third element in a list named my_list. :
# my_list = [1,2,3,4,5]
# print(my_list[2])


#E. Which list method is used to remove the last element from a list? :
# pop() method is used to remove the last element from a list.

#F. What list method is used to insert an element at a specific position? :
# insert() method is used to insert an element at a specific position.


#G. Write Python code to reverse a list called my_list in-place. :
# my_number = [1,2,3,4,5,6,7,8,9,10]
# my_number.reverse()
# print(my_number)


#H. How can you create a shallow copy of a list in Python? :
# You can use the copy() method to create a shallow copy of a list in Python.

# I. Which list method is used to count the number of occurrences of a specific element in a list?:
# count() method is used to count the number of occurrences of a specific element in a list.


#J. Write a Python code snippet to concatenate two lists, list1 and list2. :
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# print(list1 + list2)


#K. What list method can be used to sort a list in ascending order? :
# sort() method can be used to sort a list in ascending order.


#L. Write Python code to remove the first occurrence of an element 'x' from a list. :
# list1 = [1,2,3,4,5]
# x = 3
# list1.remove(x)
# print(list1)


#M. Explain the difference between append() and extend() methods when adding elements to a list. :
# The append() method adds a single element to the end of the list, while the extend() method adds multiple elements to the end of the list.


#N. Which list method can be used to remove all elements from a list? :
# clear() method can be used to remove all elements from a list.


#O. Write Python code to find the index of the first occurrence of an element 'x' in a list. :
# number = [1,2,3,4,5]
# x = 4
# print(number.index(x))


#P. What list method can be used to remove and return an element from a specific index in a list?:
# pop() method can be used to remove and return an element from a specific index in a list.


#Quiz:
#1.Which method is used to add an element to the end of a list in Python?:
#d) append()


#2.What is the purpose of the insert() method for lists in Python?:
#c) Add an element at a specific index in the list.


#3.Which list method is used to remove and return the last element of a list?:
#a) pop()


#4.What does the extend() method do when used on a list in Python?:
#b) Adds a new list as elements to the existing list.


# 5.Which list method is used to reverse the order of elements in a list in Python?:
#a) reverse()


#6. What does the sort() method do when used on a list in Python?:
#c) Sorts the list in ascending order.


#7. Which method is used to find the index of the first occurrence of an element in a list?:
#a) index()


#8.What is the purpose of the pop() method when used on a list in Python?:
#b) Removes and returns the last element of the list.



#9.How can you count the number of occurrences of a specific element in a list?:
#a) Use the count() method



#10.How can you check if a list is empty in Python?:
#c) Use the len() function and check if it's equal to zero



#11.Which method is used to copy the elements of one list to another in Python?:
#a) copy()


#12. How do you remove an element by index from a list in Python?:
#a) Use the remove() method with the index as an argument



#13.What does the len() method do when applied to a list?:
#c)Returns the number of elements in the list



#14.Given the following list, what is the output of min(my_list)?:
# my_list = [0, 2, 4, 1, 5]
# result = min(my_list)
# print(result)
#a)0


#15.Given the following list, what is the output of max(my_list)?
# my_list = [0, 2, 4, 1, 5]
# print(max(my_list))
#d)5



#16.Which list method can be used to find the number of occurrences 
# of a specific element in a list?:
#a) count()



#17. What is the output of the following code snippet?
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list)
#b)[5, 4, 3, 2, 1]


#18.What is the output of the following code snippet? 
# my_list = [1, 2, 3] 
# my_list.insert(1, 4) 
# print(my_list)

#b)[1, 4, 2, 3]



#19.Which method is used to remove all elements from a list? :
#a)clear()



#20. What is the output of the following code snippet?
# my_list = [1,2,3,4,5]
# result = sum(my_list)
# print(result)
#a)15   



#21.What is the output of the following code snippet? 
# my_list = [1, 2, 3, 4, 5] 
# result = my_list.index(3) 
# print(result)

#c)2