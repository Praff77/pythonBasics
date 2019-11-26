# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)
# # re-declaring the variable works
f="abc"
print(f)
# # ERROR: variables of different types cannot be combined
print("this is a string" +f)

# Global vs. local variables in functions
def some():
    global f
    f="def"    
    print(f)

some()
print(f)
del f
print(f)