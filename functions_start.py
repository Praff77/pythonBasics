#
# Example file for working with functions
#

# define a basic function
def fucn1():
    print("can you" )

# function that takes arguments
def fun2(arg1, arg2):
    print(arg1,"",arg2)

# function that returns a value
def cube(c):
    return c*c*c

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result
#function with variable number of arguments

def multiadd(*args):
    result = 0
    for x in args:
        result = result + x

    return result

fucn1()
#print(fucn1())
print(fucn1)

fun2(10,20)
print(fun2(10,20))
print(cube(3))

print(power(2))
print(power(2, 3))

print(power(x=3, num=2))

print(multiadd(4, 5, 10 ,4))