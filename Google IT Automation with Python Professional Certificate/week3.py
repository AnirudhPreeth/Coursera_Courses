#Week 3. 

'''
While loops instruct your computer to continuously execute your code based on the value of a condition. 
This works in a similar way to branching if statements. 
The difference here is that the body of the block can be executed multiple times instead of just once.
Initializing, to give an initial value to a variable.

A while loop will continuously execute code depending on the value of a condition. 
It begins with the keyword while, followed by a comparison to be evaluated, then a colon. 
On the next line is the code block to be executed, indented to the right. 
Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. 
What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. 
Once the statement is no longer true, the loop exits and the next line of code will be executed.  
'''
x = 0
while x<5:
    print("Not there yet,x=" + str(x))
    x = x+1
print("x=" + str(x))

def attempts(n):
    x = 1
    while x<=n:
        print("Attempt" +str(x))
        x+=1
    print("Done")
attempts(5)

username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()

'''
'''
my_variable = 5
while my_variable<10:
    print("Hello")
    my_variable+=1
