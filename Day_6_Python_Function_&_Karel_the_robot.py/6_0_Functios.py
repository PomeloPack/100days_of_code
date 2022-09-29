# built in functions

print("Hello")

len_num = len("hello")
print(len_num)

# our own function 
# using def like definition of function
#defining function example

def  my_function():
    print("This is our first function") # do this
    print("It's cool?") # finally do this

# this is how our function write into the console
# calling function
my_function()

# compare between for loops and while loops

# for 
for item in list_of_items:
    # do something to each item

for number in range(a, b):
    print(number)

# while
while something_is_true:
    # do something repeatedly

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
number_of_jumps = 6
while number_of_jumps > 0:
    jump()
    # -=1 is important because when loops come to the end number_of_jumps -= 1 means that our input 6 is now 5
    # when output will be 0 loops is False so our condition isn't work
    number_of_jumps -= 1