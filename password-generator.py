import random

lower_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upper_chars = 'abcdefghijklmnopqrstuvwxyz'
num_chars = '0123456789'
special_chars = '!@£$%^&*().,?'

def ask_for_number_of_passwords():
    '''
    Ask the user to input the number of passwords until the user enters a valid positive integer. Then returns the number as an integer.

    Returns
    -------
    number: int
        The number of passwords to generate.
    '''
    number = input('Amount of passwords to generate: ')
    try:
        number = int(number)
        if number < 1:
            print('Number of passwords too low. Please enter a positive integer!', end = ' ')
            number = ask_for_number_of_passwords()
    except ValueError:
        print('Invalid number of passwords. Please enter an integer!', end = ' ')
        number = ask_for_number_of_passwords()
    return number        

def ask_for_password_length():
    '''
    Ask the user to input the length of passwords until the user enters a valid positive integer. Then returns the number as an integer.

    Returns
    -------
    number: int
        The length of the passwords to generate.
    '''
    length = input('Your password length: ')
    try:
        length = int(length)
        if length < 1:
            print('Password length too short. Please enter a positive integer!', end = ' ')
            length = ask_for_password_length()
    except ValueError:
        print('Invalid password length. Please enter an integer!', end = ' ')
        length = ask_for_password_length()
    return length

def ask_for_complexity_customization_option():
    '''
    Asks the user whether they want to customize the complexity of their passwords. The method defaults to no if an invalid value is entered.

    Returns
    -------
    customization_option: bool
        A boolean representing whether the user wants to customize the complexity of their password or not.
    '''
    customization_option = input('Do you want to customize your password complexity (dy default your password has maximum complexity)? [y/N] ')
    customization_option = True if customization_option in {'y','Y'} else False
    return customization_option

def customize_password_complexity():
    '''
    Asks the user a variety of questions to determine the complexity of the passwords to be generated. Then returns the complexity.
    The complexity of the password is represented as a string of all the symbols allowed for password generation.
    If the complexity string is empty, the method asks the user if they want to retry customizing the complexity.

    Returns
    -------
    chars: str
        A string of distinct characters representing the symbols allowed during password generation.
    '''
    prompt = input('Do you want to use lower-case characters in your password? [Y/n] ')
    add_lower = '' if prompt in {'n','N'} else lower_chars

    prompt = input('Do you want to use upper-case characters in your password? [Y/n] ')
    add_upper = '' if prompt in {'n','N'} else  upper_chars

    prompt = input('Do you want to use numerical characters in your password? [Y/n] ')
    add_num = '' if prompt in {'n','N'} else num_chars

    prompt = input('Do you want to use special characters in your password? [Y/n] ')
    add_special = '' if prompt in {'n','N'} else special_chars

    chars = add_lower + add_upper + add_num + add_special
    if chars == '':
        prompt = input('You included no characters for your password customization. Do you want to retry (if not, the password will be of maximum complexity)? [Y/n] ')
        if prompt in {'n','N'}:
            chars = lower_chars + upper_chars + num_chars + special_chars
        else:
            return customize_password_complexity()
    return chars

def generate_password(chars, length):
    '''
    Generates a single instance of a password of certain complexity and length.

    Parameters
    ----------
    chars: str
        A string of distinct characters representing the symbols allowed during password generation.
    length: int
        The length of the password.

    Returns
    -------
    password: str
        A string containing the password
    '''
    password = ''
    for c in range(length):
        password += random.choice(chars)
    return password

def generate_passwords():
    '''
    Asks the user input the length, number, and complexity of passwords they want to generate, then generates and prints them.
    '''
    # First we ask for the length, number, and complexity of the passwords.
    length = ask_for_password_length()
    number = ask_for_number_of_passwords()
    customization_option = ask_for_complexity_customization_option()

    if customization_option:
        chars = customize_password_complexity()
    else:
        chars = lower_chars + upper_chars + num_chars + special_chars

    # Then we generate the passwords and print them.
    if number == 1:
        print('\nHere is your password: ', end = '')
    else:
        print('\nHere are your passwords:')

    for i in range(number):
        password = generate_password(chars,length)
        print(password)

print('Welcome to your password generator!')

if __name__ == '__main__':
    # Keep generating passwords as long as the user wants.
    while True:
        generate_passwords()

        keep_going = input('\nDo you want to generate more password? [y/N] ')
        keep_going = True if keep_going in {'y','Y'} else False

        if not keep_going:
            break
        else:
            print('') # Line break just for readability of text printed to console.




