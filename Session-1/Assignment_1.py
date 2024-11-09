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

#Exercise 10: While Loop

''' 
Write a program that uses a while loop to print numbers from 1 to 5.
Ensure the loop terminates correctly
'''
num1 = 1
while num1 < 6:
    print(num1)
    num1 = num1 +1

#Exercise 11: Match Statement (Python 3.10+)

'''
 Write a program that:
1) Asks the user to input a grade (e.g., "A", "B", "C", "D", or "F").
2) Use a match statement to print a corresponding message for each grade:
■ "A": "Excellent!"
■ "B": "Good job!"
■ "C": "Fair."
■ "D": "Needs improvement."
■ "F": "Failing."
Handle invalid input by printing a default message.

'''

grade = input("Enter a grade (A, B, C, D, or F): ")

match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Good job!")
    case "C":
        print("Fair.")
    case "D":
        print("Needs improvement.")
    case "F":
        print("Failing.")
    case _:
        print("Invalid grade entered.")

#Exercise 12: Define a Function
'''
Write a function called greet that takes a name as an argument and prints "Hello, [name]!".
Call the function with your own name.

'''

def greet(name):
    print("Hello", name)

greet("Konstantinos")

#Exercise 13: Function with Return Value
'''
Define a function called square that takes a number as an argument and returns its square.
Print the result of calling this function with different numbers.

'''

def square(y):
    return (y*y)

print(square(5))
print(square(978))

#Exercise 14: Function with Default Parameters

'''
Write a function called multiply that takes two parameters, a and b, and returns their product. 
Set a default value of 1 for the parameter b.
Test the function with and without providing the second argument.

'''
def multiply(a, b=1):
    return a*b

print(multiply(9,7))
print(multiply(9))

#Exercise 15: List Comprehension
''' 
1) Create a list of numbers from 1 to 10.
2) Use list comprehension to create a new list that contains the squares of these numbers.
3) Print the new list.

'''

my_list = list(range(1,11))
new_list = []
for i in my_list:
    new_list.append(i*i)

print(new_list)

#Exercise 16: Nested Data Structures

'''
1) Create a dictionary where the keys are names of students and the values are lists of their grades.
2) Write a function that takes the dictionary and prints the average grade for each student.

'''

students_grades = {
    "Kostas": [90, 85, 88],
    "Chris": [75, 80, 70],
    "George": [95, 100, 92],
    "Nick": [60, 65, 58]
}

def print_average_grades(grades_dict):
    for student, grades in grades_dict.items():
        average = sum(grades) / len(grades)
        print(f"{student}: {average:.2f}")

print_average_grades(students_grades)

#Exercise 17: Simple Calculator

'''
Write a program that:
1) Defines a function calculate which takes three parameters: two numbers and an operator (+, -, *, /).
2) Performs the operation and returns the result.
3) Ask the user for the two numbers and the operator, then call the function and print the result

'''

def calculate(num1, num2, operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            return "Invalid operator"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"The result is: {result}")


#End of Excercises of Assignment 1. Any suggestions or recommondations are welcomed and appreciated. 