print('H')
#print(10/0)   //show error in code thats why we write it in try block
try:
     a=10
     print(a/2)
except ZeroDivisionError as z :# (ZeroDivisionError,TypeError) #used as multiple error types
      print('z')
else:
     print('Hello')
print('Z')

#finally

# Python program to demonstrate finally
  
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
  
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
  
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
    