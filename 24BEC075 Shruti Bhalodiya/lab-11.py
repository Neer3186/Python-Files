#Lab-11:Exception Handling

def get_integer_input():
    while True:
        user_input = input(" Enter an integer value: ")
        try:
            # Try to convert the input to an integer
            integer_value = int(user_input)
            print(f" You entered a valid integer: {integer_value}")
            break  # Exit the loop if input is valid
        except ValueError:
            # Handle invalid input
            print(" Error: That's not an integer. Please try again...\n")

# Call the function
get_integer_input()
