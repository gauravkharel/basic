import json

# numbers = [2,3,5,7,11,14]

filename = 'numbers.json'
# you dummp here
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# you write here
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)