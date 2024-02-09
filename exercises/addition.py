num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

try:
    # Converting input strings to integers
    num1 = int(num1_str)
    num2 = int(num2_str)

    print("First Number: ", num1)
    print("Second Number: ", num2)

except ValueError:
    print("Please enter the valid integers.")