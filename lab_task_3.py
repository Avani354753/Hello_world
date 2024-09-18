# Continously ask the user for input until a valid number is provided
while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print("You entered a valid number:", number)
        break
    except ValueError:
        print("Invalid input, please enter a number.")


# Nested If - Else Statement Example: Age Category
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Multiple Conditions Example: Positice, Negative, or Zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

#boolen Operations Example: valid Email
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email address")
else:
    print("Invalid email address")