"""
In this section we will see how to write a program for Fibonacci series :
___________________________________________________________________________
Question : Write a function for printing the fibonacci number and the number will be taken from the user :
______________________________________________________________________________________________________
Approach : first we take three input from user the first and second number is Fibonacci series and the third number is
           for end for that series , Now in the second step we will use while loop and increment and assignment
            operate for this executing this series :
"""
A = int(input("Enter the first number : "))
B = int(input("Enter the second number : "))
C = int(input("Enter the third number, where you want to stop this loop : "))
D = 0  # this variable is for assigning the new number to it.
if( B < 0):
    print("it will run infinite loop :")
else:
 while( D <= C ):
    print(D)
    A = B
    B = D
    D = A + B


 def my_function():
     print("Hello from a function")


 my_function()
