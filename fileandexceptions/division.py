# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by zero.")

print("Give me two numbers, and, I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\n First Number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try: 
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: 
        print("you can't divide by 0!")
    else:
        print(answer)