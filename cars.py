cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)

# print(cars)

# print("Here is the original list: ")
# print(cars)

# print("\nHere is the sorted list: ")
# print(sorted(cars))

# print("\nHere is the original list again: ")
# print(cars)

# cars.reverse()
# print(cars)
# print(len(cars))

for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age = 12
if age < 4:
 print("Your admission cost is $0.")
elif age < 18:
 print("Your admission cost is $5.")
else:
 print("Your admission cost is $10.")


requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# 122 Using if Statements with Lists