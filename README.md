# Maximum-Of-Two-Values
 Compares two user-supplied numbers and prints the greater one.

## Scope
 Write a function named max that accepts two float values as arguments and returns the value that is the greater of the two. For example, if 7.2 and 12.1 are passed as arguments to the function, the function should return 12.1. Use the function in a program that prompts the user to enter two float values. The program should display the value that is the greater of the two.

### Sample Run
    This program calculates which number is higher.
    Enter the first number: 32.3
    Enter the second number: 33.2
    The highest number is: 33.2

## Pseudocode
### Main Program Logic
    START
      INPUT first number
      INPUT second number
      CALL max function (args: first number, second number)
      SET higher number to the return value of the max function
      PRINT the higher number
    END

### max Function
    START
      PASS IN: first number, second number
      SET list of numbers to the first and second numbers
      SET greater number to maximum value in list
      RETURN greater number
    END
