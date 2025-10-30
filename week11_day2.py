#
# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Frank"
age = 15
favorite_color = "Green"
favorite_number = 22

#  Step 2: Practice String Operations
# 1. Print your name in uppercase
print("uppercasename: ", first_name.upper())


# 2. Print how many letters are in your name

print("Length of name:", len(first_name), "characters") 


# 3. Combine your name and favorite color into one message

print("Hi my name is", first_name, ", my favorite color is", favorite_color)  

#  Step 3: Math Practice
# Use arithmetic operators with your favorite number
add_result = 11 + 11
print("Addition (11 + 11):", add_result)  # 5

# Subtraction
sub_result = 32 - 10
print("Subtraction (32 - 10):", sub_result)  # 3

# Multiplication
mul_result = 11 * 2
print("Multiplication (11 * 2):", mul_result)  # 12

# Division
div_result = 44 / 2
print("Division (44 / 2):", div_result)  # 5.0


#  Step 4: User Input Practice
# Ask the user two questions and combine answers
name = input("Enter your name: ")
print("Hello", name)
W_T_B = input("Would you like to buy something today? : ")
print("ok, bye")





# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together 
number = int(input("What is your favorite number?"))
subb_result = number - 2
print(f"Your favorite number subtracted by two is: ", subb_result)


