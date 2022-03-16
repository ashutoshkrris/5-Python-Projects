from secrets import choice
import string

UPPERCASE = string.ascii_uppercase
LOWECASE = string.ascii_lowercase
NUMBER = string.digits
SYMBOLS = ['@', '#', '$', '%', '&', '_']
DATA = list(UPPERCASE) + list(LOWECASE) + list(NUMBER) + SYMBOLS


def generate_random_password(length, number):
    print(f"Here are your {number} passwords of length {length} characters :\n")
    for _ in range(number):
        password = ''.join(choice(DATA) for _ in range(length))
        print(password)


if __name__ == "__main__":
    number = int(input("How many passwords do you wish to generate ? : "))
    length = int(input("What should be the length of each password ? : "))
    generate_random_password(length, number)
