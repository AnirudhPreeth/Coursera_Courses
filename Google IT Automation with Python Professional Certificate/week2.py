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

#Practice Quiz : Functions. 

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return miles * 1.6 
my_trip_miles = 55
# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)
# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2 * my_trip_km))


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


def lucky_number(name):
  number = len(name) * 9
  greeting = "Hello " + name + ". Your lucky number is " + str(number)
  return greeting
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))


#Comparing Things. 

'''
Python can also compare values. This lets us check whether something is smaller than, equal to, or bigger than something else. 
This allows us to take the result of our expressions and use them to make decisions.
True is a value that belongs to another data type called the Boolean. Booleans represent one of two possible states, either true or false. 
Every time you compare things in Python the result is a Boolean of the appropriate value.
Equality Operator. 
Not equals operator. Negative form of the equality operator. 
Compare integer and string? Type error. 
Logical Operators. Connect multiple statement together. 
AND, OR, NOT.
To evaluate as true the and operator would need both expressions to be true at the same time here. 
Alphabetical order (comparing strings).
If we use the or operator, instead, the expression will be true if either of the expressions are true, and false only when both... 
...expressions are false.
'''
print(10>1)
print("cat" == "dog")
print(1 != 2)
print(1 == "1")
print("Yellow" > "Cyan" and "Brown" > "Magenta")
print(25>50 or 1 != 2)
print(not 42 == "Answer")


print(32 == 30+2)   # The == operator checks if the 2 values are 
True                # equal to each other. If they are equal, 
                    # Python returns a True result.


print(5+10 == 6+7)  # If the two values are not equal, as in the
False               # expression 5+10 == 6+7 (or 15 == 13), Python          
                    # returns a False result.


print(10-4 != 10+4) # The != operator checks if the 2 values are
True                # NOT equal to each other. If true, Python              
                    # returns a True result. 


print(9/3 != 3*1)   # In this last example, 9/3 != 3*1 (or 3 != 3)
False               # is false. So, Python returns a False value.

# The = equals assignment operator is used to assign a value to a 
# variable.

my_variable = 3*5           # Assigns a value to my_variable      
print(my_variable)          # Printing the variable returns the 
15                          # value assigned to the variable.


                              
# The == equality comparison operator checks if the values of the two
# expressions on either side of the == operator are equivalent to one 
# another.
      
print(my_variable == 3*5)   # Printing the variable returns a Boolean 
True                        # True or False result. 

print(11 > 3*3)         # The > operator checks if the left value is
True                    # greater than the right value. If true, it
                        # returns a True result.


print(4/2 > 8-4)        # If the > operator finds that the left value
False                   # is NOT greater than the right value, the
                        # comparison will return a False result.


print(4/2 < 8-4)        # The < operator checks  if the left value is
True                    # less than the right side. If true, the
                        # comparison returns a True result.


print(11 < 3*3)         # If the < operator finds that the left side is False                   # NOT less than the right value, Python returns
                        # a False result.
                        
print(12*2 >= 24)   # The >= operator checks if the left value is
True                # greater than or equal to the right value. 
                    # If one of these conditions is true,  
                    # Python returns a True result. In this case  
                    # the two values are equal. So, the comparison
                    # returns a True result.


print(18/2 >= 15)   # If the >= comparison determines that the left False
False               # value is NOT greater than or equal to the
                    # right, it returns a False result.

print(12*2 <= 30)   # The <= operator checks if the left value is
True                # less than or equal to the right value. In 
                    # this case, the left value is less than the
                    # right value. Again, if one of the two 
                    # conditions is true, Python returns a True
                    # result.


print(15 <= 18/2)   # If the <= comparison determines that the left 
False               # value is NOT less than or equal to the right
                    # value, the comparison returns a False result. 


# The == operator can check if two strings are equal to each other. 
# If they are equal, the Python interpreter returns a True result.
print("a string" == "a string")
True


# In this example, the equality == comparison is between "4 + 5" and
# 4 + 5. Since the left data type is a string and the right data type
# is an integer, the two values cannot be equal. So, the comparison
# returns a False result.
print("4 + 5" == 4 + 5)
False


# The != operator can check if the two strings are NOT equal to each
# other. If they are indeed not equal, then Python returns a True result.
print("rabbit" != "frog")
True


# In this example, the variable event_city has been assigned the string 
# value "Shanghai". This variable is compared to a static string, 
# "Shanghai", using the != operator. As, the strings "Shanghai" and 
# "Shanghai" are the same, the comparison of "Shanghai" != "Shanghai" 
# is false. Accordingly, Python will return a False result.
event_city = "Shanghai"
print(event_city != "Shanghai")
False

# This last example illustrates the result of trying to compare two
# items of different data types using the equality == operator. The
# two items are not equal, so the comparison returns False.
print("three" == 3)
False

# The greater than > operator checks if the left string has a higher 
# Unicode value than the right string. If true, the Python interpreter
# returns a True result. Since W has a Unicode value of 87, and you can 
# easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. As this is true, Python will return a True 
# result.
print("Wednesday" > "Friday")
True
 
 
# The less than < operator checks if the left string has a lower 
# Unicode value than the right string. If you reference the Unicode 
# chart above, you can see that all lowercase letters have higher 
# Unicode values than uppercase letters. We can see that B has a 
# Unicode value of 66 and b has a Unicode value of 98. This 
# comparison is the same as 66 < 98, which is true. So, Python will 
# return a True result.
print("Brown" < "brown")
True

# If the strings have the same first few letters, the comparison will 
# cycle through each letter of each string, from left to right until it 
# finds two letters that have different Unicode values. In this example, 
# both strings share the initial substring "sun", but then have 
# different letters with different Unicode values in the fourth place 
# in each string. So, the fourth letters 'b' and 't' of the two
# strings are used for the comparison. Since 'b' does not have a higher
# Unicode value than 't', the comparison returns a False result.
print("sunbathe" > "suntan")
False


# If two identical strings are compared using the less than < comparison
# operator, this will produce a False result because they are equal.
print("Lima" < "Lima")
False


# This last example illustrates the result of trying to compare two
# items of different data types using the less than < operator. The 
# greater than > and less than operators < cannot be used to compare
# two different data types. 
#print("Five" < 6)
'''
Error on line 1:
    print("Five" < 6)
TypeError: '<' not supported between instances of 'str' and 'int'
'''

# Use the Unicode chart in Part 2 to determine if the Unicode values of 
# the first letters of each string are higher, lower, or equal to one
# another. 


var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
 
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)

print((6*3 >= 18) and (9+9 <= 36/2))
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))
True

# False or True returns True
print(country == "New York City" or city == "New York City")
True

# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)
True

# False or False returns False
#print("B_name" > "C_name" or "B_name" < "A_name”)
False

# Test Example 1:

x = 2*3 > 6
print("The value of x is:")
print(x)
print("")  # Prints a blank line
print("The inverse value of x is:")
print(not x)

# What happens when you negate a False statement? 
# Click Run when you are ready to check your answer.
today = "Monday"
print(not today == "Tuesday") 
# The "today" variable states today is Monday. This makes the comparison
# "today == Tuesday" False. The logical operator "not" inverts the False
# result to become True. In other words, this expression asks if it is
# false that today is not Tuesday. More succinctly, "not False" means 
# True."





