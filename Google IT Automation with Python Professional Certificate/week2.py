def greeting(name):
    print("Welcome," + name)

greeting("Kay")
greeting("Cameron")

def greeting(name, department):
    print("Welcome," + name)
    print("You are a part of " + department)

greeting("Blake", "IT support")
greeting("Ellis", "Software Engineering")

def area_triangle(base,height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is : " + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, reamaining_seconds

def greeting(name):
    print("Welcome, " + name)

result = greeting("Christine")
print(result)

name = "Kay"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))
name = "Cameron"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))
lucky_number = "Kay"
lucky_number = "Cameron"


'''
For def convert_seconds(seconds) -> 
First operation is calculating how many hours are in a given amount of seconds. 
While the second works out how many minutes are left once we subtract the hours and then how many...
...seconds remain after subtracting minutes. We end up with three numbers as a result. 
So the function returns all three of them.
Because we know that the function returns three values, we assign the result of the function...
...to three different variables. 

'''
