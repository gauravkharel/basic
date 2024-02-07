# for value in range(1,5):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     squares.append(value**2)

# print(squares)

# digits = [1,2,3,4,5,6,7,8,9,0]
# min(digits)
# max(digits)
# sum(digits)


squares = [value**2 for value in range(1,11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[2:])
# print(players[-3:])

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())