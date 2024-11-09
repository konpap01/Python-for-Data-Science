'''
Below are the exercises on materials we covered in Session 1. 

For each Question, I am writing my suggested solution

'''

#Exercise 1: Print a Greeting

''' 
Write a Python program that prints a greeting message, such as "Hello, Python!". 

'''

print("Hello, Python!")

#Exercise 2: Basic Arithmetic

''' 
Create a program that:
1) Defines two variables, a and b, with numerical values.
2) Prints their sum, difference, product, and quotient. 
'''

a = 5
b = 4
print(a+b, a-b, a*b, a/b)


#Exercise 3: String Manipulation

''' 
Define a variable name and assign it your name. Write a program that prints a message saying 
"Hello, [name]!" where [name] is the value of the variable. 
'''

name = "Konstantinos"
print("Hello", name)

#Exercise 4: Lists

''' 
1) Create a list called universities with at least five different university names.
2) Print the entire list.
3) Print the first and last university in the list. 

'''

uni = ["Bocconi", "Esade", "Harvard", "UCL", "EADA"]
print(uni)
print(uni[0], uni[-1])

#Exercise 5: Dictionaries

''' 
Create a dictionary called student with keys: name, age, and grade, and assign appropriate 
values to each key.
Write a program that prints each key-value pair in the dictionary. 
'''

student = {"name": "kon", "age": 23, "grade": 9}
print(student)

#Exercise 6: Tuples
''' 
1) Define a tuple called coordinates with two values representing a point in 2D space (e.g., (x, y)).
2) Print the value of coordinates and access each element by its index 

''' 

coordinates = (10, 20)
print("Coordinate X", coordinates[0], "Coordinate Y", coordinates[1])

#Exercise 7: Sets
''' 
    1)Create a set called colors with the values: "red", "green", "blue".
    2) Add another color to the set.
    3)Try adding a duplicate color and observe what happens.
    4)Print the set and remove one color from it.
    5)Create another set named light_colors and merge colors and light_colors 

'''
colors = {"red", "green", "blue"}
colors.add("black")
colors.add("red")
colors
colors.remove("black")
colors
light_colors = {"yellow", "white"}
colors.union(light_colors)

#Exercise 8: Conditional Statements

'''
Write a program that:
1) Takes an input number from the user.
2) Checks if the number is positive, negative, or zero.
3) Prints an appropriate message based on the result.

'''

x = int(input())
if x > 0:
    print("number is positive")

elif x < 0:
    print("number is negative")

else: 
    print("number is zero")

#Exercise 9: For Loop
'''
Create a list of numbers from 1 to 5.
Use a for loop to iterate through the list and print each number.
'''
my_list1 = []
for i in range(1,6):
    my_list1.append(i)
for i in my_list1:
    print(i)
