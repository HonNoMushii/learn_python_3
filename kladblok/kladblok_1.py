#!/usr/bin/python3

# Global variables
prompt = "> "
program = "script"

# Function 1: Greets the user and asks for their name
def hello_user(to="World"):
    print("Hello", to)
    user_name = input(f"What's your name?\n{prompt}")
    name_user = user_name.title()
    print(f"Welcome {name_user}, I hope you will like the {program} script")
    return name_user

# Function 2: Asks the user which script they want to run
def prompt_user(name_user):
    print(f"\nWell {name_user},\nWhat script do you want to run?")
    print("    > 1. Calculator")
    print("    > 2. Function 4 (Placeholder)")

    while True:  # Loop until the user enters a valid choice
        choice = input(prompt)
        
        if choice in ["1", "2"]:  # Check if the choice is valid (1 or 2)
            return choice
        else:
            print("Sorry, that option is not available. Please choose 1 or 2.")  # Invalid input message

# Function 3: Calculator script (with one input and ability to go back)
def calculator(name_user):
    print(f"\nHello {name_user}, let's do some calculations!")
    print("You can type a mathematical expression (e.g., 1+2, 3 * 5, 10 / 2), or type 'exit' to go back to the script menu.")
    
    while True:
        expression = input("Enter expression: \n")  # Only prompt text required here
        
        if expression.lower() == "exit":
            print("Going back to the script selection menu...")
            return  # Exit to the script selection menu
        
        try:
            # Remove any extra spaces from the expression
            expression = expression.replace(" ", "")
            
            # Evaluate the expression
            result = eval(expression)
            print(f"The result of {expression} is: {result}")
        
        except Exception as e:
            print(f"Error: {e}. Please enter a valid mathematical expression.")

# Function 4: Placeholder function (can be expanded later)
def f4(name_user):
    print(f"\nHello {name_user}, this is the placeholder function 4.")
    print("You can replace this with actual functionality when ready.")  # Placeholder message

# Main block that runs the program
if __name__ == "__main__":
    name_user = hello_user()  # Greet the user and get their name
    
    while True:  # Loop to allow re-running the program if the user wants
        choice = prompt_user(name_user)  # Ask what script they want to run
        
        # Check the user's choice
        if choice == "1":
            calculator(name_user)  # Call the calculator function
        elif choice == "2":
            f4(name_user)  # Call function 4 (Placeholder)
