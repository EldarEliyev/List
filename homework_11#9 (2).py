#Note . Add the following list at the top of your code.You will use this list during the homework in certain tasks:
# fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]

#Also print the list's modification versions to see the difference:

#List Methods-:
#A.Make up a formula with built-in python 'len' method that finds helps to get the last element from the 'fruits' list:
# print(fruits[len(fruits)-1])

#B.Add any two fruits to the 'fruits' list:
# fruits.append("Pineapple")
# fruits.append("Watermelon")
# print(fruits)


#C.Remove third fruit so you can assign it to a variable:
# third_fruit = fruits.pop(2)
# print(third_fruit)
# print(fruits)


#D.Add a fruit to the 'fruits' list twice, and then print the amount of this fruit in the 'fruits' list:
# fruits.append("Lemon")
# fruits.append("Ananas")
# print(fruits.count("Lemon"))

#E.Find the index of 'Grape' object in the 'fruits' list.:
# print(fruits.index("Grape"))

#G.Remove third fruit without getting the removed fruit:
# third_fruit =  fruits.pop(3)
# print(third_fruit)

#H.Remove a fruit at position one:
# fruits.pop(0)
# print(fruits)

#I.Add 'Blackberry' to the end of the 'fruits' list.Remove it using 'pop' method by finding its positive index:
# fruits.append("Blackberry")
# print(fruits)
# fruits.pop(fruits.index("Blackberry"))
# print(fruits)



#J.Reverse the 'fruits' list with two different methods.Each time print the reversed list:
# fruits.reverse()
# print(fruits)


#K. Sort alphabetically the 'fruits' list. Print the sorted version of the 
# list.:
# fruits.sort()
# print(fruits)


#L.Suppose you have the following list:
# new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]
#Extend the 'fruits' list with the new list.:
# fruits.extend(new_fruits)
# print(fruits)


#M.Make a copy of the 'fruits' list.Remove the last three fruits.Print both of the lists('fruits' and the modified copied version):
# fruits_copy = fruits.copy()
# fruits_copy.pop(3)
# fruits_copy.pop(2)
# fruits_copy.pop(1)
# print(fruits)
# print(fruits_copy)


#N. Create a variable named 'occurrence'. Make it equal True if the 
# 'Papaya' is in the
# 'fruits' list, otherwise False.:
# occurence = "Papaya" in fruits
# print(occurence)


#O.Clear the 'fruits' list.:
# fruits_clear = fruits.clear()
# print(fruits_clear)



#Variables-:
#A. Suppose you have the following variables:
# x = 60
# y = 70

# You need to swap these variables values in one line of code.:
# x,y = y,x
# print(x,y)


#ChatGPT's homework (List Methods) -:
#1. Append and Extend:
#A. Write a Python program that creates an empty list and then appends the following elements to it: 10,20,30,40, and 50.Print the list after each append operation.:
# numbers = []
# numbers.append(10)
# numbers.append(20)
# numbers.append(30)
# numbers.append(40)
# numbers.append(50)
# print(numbers)

#B.Create a second list containign elements [60,70,80]. Extend the first using this second list and print the updated list:
# numbers2 = [60,70,80]
# numbers.extend(numbers2)
# print(numbers)


#2. Insert and Remove:
#A.Write a Python program that creates a list containing the following elements: 'apple', 'banana', 'orange', 'grape', 'apple', 'kiwi'.:
# fruits = ["apple", "banana", "orange", "grape", "apple", "kiwi"]
# print(fruits)


#B.Use the 'insert' method to add 'pear' between 'banana' and 'orange' in the list.Print the updated list:
# fruits.insert(2, "pear")
# print(fruits)



#C.Use the 'remove' method to remove the first occurence of 'apple' from the list.Print the updated list:
# fruits.remove("apple")
# print(fruits)




#3. Count and Index:
#A.Create a list containing the following elements: 2,4,6,8,4,10,4,12,14:
numbers = [2,4,6,8,4,10,4,12,14]
# print(numbers)

#B.Use the 'count' method to find how many times the number 4 appears in the list and print the count:
# print(numbers.count(4))


#C.Use the 'index' method to find the index of the first occurence of 4 in the list and print the index:
# print(numbers.index(4))


#4. Sort and Reverse:
#A.Create a list containing the following integers in random order: 45,23,78,12,98,56:
# num_list = [45,23,78,12,98,56]
# print(num_list)

#B.Use the 'sort' method to sort the list in ascending order and print the sorted list:
# num_list.sort()
# print(num_list)


#C.Use the 'reverse' method to reverse the sorted list and print the reversed list:
# num_list.reverse()
# print(num_list)




#5. Slice and Concatenate:
#A.Create a list containing the following elements: 'red', 'blue', 'green','yellow', 'orange', 'purple:
# colors = ["red", "blue", "green", "yellow", "orange", "purple"]
# print(colors)

#B.Use slicing to extract a new list that contains only the first three colors.Print the new lis:
# print(colors[0:3])


#C.Use slicing again to extract a new list that contains the last three colors. Print the new list:
# print(colors[-3:])


#D.Concatenate the two sliced lists and print the final combined list:
# print(colors[0:3] + colors[-3:])
