
# Maximum of Two Values
# Shaun Hayworth
# CIS 2
# 12-09-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/Maximum-Of-Two-Values

# Prompts user for two floating-point numbers, compares them, and prints the
# greater one to the screen.

# NOTE: The name of the maximum() function was changed from the assignment
# instructions to avoid confusion with the max() built-in function.


def main():
    '''This is the mainline program logic.'''
    print('This program calculates which number is higher.')

    # Prompts the user for two floats and passes them to the max() function
    # as arguments.
    first_number = float(input('Enter the first number: '))
    second_number = float(input('Enter the second number: '))
    max_value = maximum(first_number, second_number)
    print('The highest number is: {max_value}')


def  maximum(number_1, number_2):
    '''Puts values into a list and returns the greater number.'''
    # Create a list of the values passed as arguments and return the highest
    # value.
    values = [number_1, number_2]
    greater_number = max(values)
    return greater_number


# Call the main() function to execute program.
main()
