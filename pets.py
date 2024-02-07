# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while "cat" in pets:
#     pets.remove('cat')

# print(pets)

def describe_pet(animal_type, pet_name='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is "+ pet_name.title() + ".")

describe_pet(animal_type='kutta')
