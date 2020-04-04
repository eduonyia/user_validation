import random
import string


# container
my_container = []


#  Choosing a password:
def choose_password():
    password = input('Enter your preferred password: ')

    while len(password) < 7:
        password = input('Enter password equal to or greater than 7 characters : ')

    return  password

# get basic details
def get_user_details():
    biodata =  {}
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    email = input("Email: ")

    # generate password
    passwd = firstName[:2] + lastName[-2:] + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    print(f'Your password is {passwd}')
    satisfied = input('Satisfied with the password ? (Y or N): ')
    if satisfied.lower() == 'y':
        user_details = {'First Name': firstName, 'Last Name': lastName, 'Email': email, 'Password': passwd}

    else:
        # choose password
        passwd = choose_password()
        user_details = {'First Name': firstName, 'Last Name': lastName, 'Email': email, 'Password': passwd}

    print(user_details)
    biodata.update(user_details)

    return biodata


# testing
new_user = ''

while True:
    user = get_user_details()
    my_container.append(user)

    new_user = input("Capture new user(Y or N): ")
    if new_user.lower() != 'y':
        break


count = 0
for item in my_container:
    count += 1
    print(f'\nUser {count}')
    for key, value in item.items():
        print(f'{key} - {value}')


