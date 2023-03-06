# create a calculator app 
# ask user to enter two numbers and an operation (+, -, x, /)
# print answer and write each equation entered into a text file 'equations.txt'
# include option for user to read all equations from new text file 'equations.txt' and print out all equations with answers

# function that add two numbers
def add(x, y):
    return(x + y)

# function that subtracts two numbers
def subtract(x, y):
    return(x - y)

# function that multiplies two numbers
def multiply(x, y):
    return(x * y)

# function that divides two numbers
# handling a zero division error by using a try/except clause
def divide(x, y):
    try:
        return(x / y)
    except ZeroDivisionError:
        print("You cannot divide by zero!")

print('''Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. view all equations
''')

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == '5':
        # using .lower function to handle case sensitivity
        file = input("Enter file name, equations: ").lower()
        if file == 'equations':
            # using try-exception block for error handling
            try:
                with open('equations.txt', 'r', encoding='utf-8') as f:
                    lines = f.read()
                    print(lines)
                    break
            except FileNotFoundError as error:
                print('File does not exist')
                print(error)

        # returns user to menu if input is outside the specified parameters
        else: print("Invalid Input. Try again!")


    # check if choice is one of the four options
    elif choice in ('1', '2', '3', '4'):  
        
        # Value error handling using try-except block
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please try again!")  
                continue

        if choice == '1':
            output = add(num1, num2)
            equation = f"{num1} + {num2} = {output}"
            print(equation)
            

        elif choice == '2':
            output = subtract(num1, num2)
            equation = f"{num1} - {num2} = {output}"
            print(equation)

        elif choice == '3':
            output = multiply(num1, num2)
            equation = f"{num1} * {num2} = {output}"
            print(equation)


        elif choice == '4':
            output = divide(num1, num2)           
            equation = f"{num1} \ {num2} = {output}"
            print(equation)


        # opening new text file to write and append user equations and encoding to remove unwanted characters
        # using try-exception block for error handling
        try:   
            with open('equations.txt', 'a+', encoding='utf-8') as f:
                
                f.write(f"{equation}\n")

        except FileNotFoundError as error:
                print('File does not exist')
                print(error)
           

        # check if user wants another calculation
        # break the while loop if answer is 'no'
        # using .lower function to handle case sensitivity
        another_calc = input("Enter another calculation? (y/n): ").lower()
    
        if another_calc == "n":
            print("\nGoodbye!")
            break
    
    else:
        # handling user error by returning user to menu if input is outside the specified parameters
        print("Invalid Input. Try again!")
    
