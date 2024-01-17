import random

def generatePassword(n):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    chosenLetter = random.sample(characters, n)
    password = "".join(chosenLetter)
    return password


if __name__ == "__main__":
    while True:
        usersChoice = input("Please enter 'yes' to generate a password or 'no' to exit: ").lower()

        if usersChoice == 'no':
            break
        elif usersChoice == 'yes':
            try:
                passLen = int(input("Enter the length of the password: "))
                password = generatePassword(passLen)
                print("A randomly selected password is: ", password)
            except ValueError:
                print("Invalid password length. Please enter a valid integer.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")




      