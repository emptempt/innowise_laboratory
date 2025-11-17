# Get useer's full name
user_name = input('Enter your full name: ')

# Get and validate birth year with error handing
while True:
    try:
        current_age = 2025 - int(input('Enter your birth year: '))
        if 0 <= current_age <= 150:
            break
        else:
            print('Incorrect year of birth.')
    except ValueError:
        print('Please enter a valid birth year.')

def generate_profile(age):
    """Determine life stage based on age.

    Args:
        age (int): The age of the person.

    Returns:
        str: Life stage category - 'Child', 'Teenager', or 'Adult'.
    """
    if 0 <= age <= 12:
        return 'Child'
    elif 13 <= age <= 19:
        return 'Teenager'
    else:
        return 'Adult'

# Collect user's hobbies
hobbies = list()
while True:
    word = input("Enter a favorite hobby or type 'stop' to finish: ")
    if word == 'stop':
        break
    else:
        hobbies.append(word)

# Create user profile dictionary
user_profile = dict()
user_profile['name'] = user_name
user_profile['age'] = current_age
user_profile['stage'] = generate_profile(current_age)
user_profile['hobbies'] = hobbies

# Display user profile dictionary
print(f'\n---\nProfile Summary:\nName: {user_profile['name']}\nAge: {user_profile["age"]}\nLife Stage: {user_profile["stage"]}')

# Display hobbies or message if not provided
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f'Favorite Hobbies ({len(hobbies)})')
    for i in hobbies:
        print(f'- {i}')
print('---')