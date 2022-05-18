# TASK: Write a Python calculator that can perform: addition, subtraction, division, multiplication and modulus operations. It should accept user input

# A welcome message to users

def welcome():
    print('''
Welcome to Calculator
''')
...
# Call the function
welcome();

# Define a function to handle the ability to perform the program as many times as the user wants:
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

# Accept input from users:
    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))

    # Addition
    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    # Subtraction
    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    # Multiplication
    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    # Division
    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    # Modulus
    elif operation == '%':
        print('{} % {} = '.format(num1, num2));
        print(num1 % num2);

    # If a user enters an invalid operator
    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function so 
    # that it will trigger the code that asks the user whether or not they would like to continue:
    again()

# Define the again() function
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()