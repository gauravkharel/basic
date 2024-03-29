# starts with users that needs to be verified
# and an empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []

# verify each user until there are no more unconfirmed users
# move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("verifying users: " + current_user.title())
    confirmed_users.append(current_user)

# display all the confirmed users
    print("\n the following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())