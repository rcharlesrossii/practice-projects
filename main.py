from getpass import getpass
from typing import Optional


MIN_USERNAME_LEN = 8
MAX_USERNAME_LEN = 16
MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 256

user_info = {}


def prompt_for_username() -> Optional[str]:
    """Asks user to input a username.

    Input restrictions:
        * Length between 8 - 16 characters
        * Only alphanumeric characters
        * Must Start with at least 4 letters before use of number
        * Case does NOT matter

    Returns:
        Optional[str]: Username input by user or none if invalid.
    """
    username = input("Enter your username: ")
    error_messages = []
    if len(username) < MIN_USERNAME_LEN or len(username) > MAX_USERNAME_LEN:
        error_messages.append(
            f"The username must be between {MIN_USERNAME_LEN}"
            f" and {MAX_USERNAME_LEN}."
        )
    if not username.isalnum():
        error_messages.append("The username must only use alphanumeric characters.")
    if not username[:4].isalpha():
        error_messages.append("The username must start with 4 alpha characters.")

    if error_messages:
        for error in error_messages:
            print(error)
        return None
    else:
        return username.lower()


def prompt_for_password(username: str) -> Optional[str]:
    """Asks user to input a password.

    Input restrictions:
        * Length between 8 - 256 characters
        * Cannot be the same as the username

    Args:
        username (str): This is the username entered from the prompt_for_username function.

    Returns:
        Optional[str]: Password that was input by user or none if input was invalid.
    """
    password = getpass("Enter your password: ")
    error_messages = []
    if len(password) < MIN_PASSWORD_LEN or len(password) > MAX_PASSWORD_LEN:
        error_messages.append(
            f"The password must be between {MIN_PASSWORD_LEN} and {MAX_PASSWORD_LEN}."
        )
    if password == username:
        error_messages.append("The password cannot be the same as the username.")

    if error_messages:
        for error in error_messages:
            print(error)
        return None
    else:
        return password


def check_create_password(password: str) -> bool:
    """Check to see if the passwords match.

    Args:
        password (str): Password the user entered originally.

    Returns:
        bool: True if the user retyped the password correctly.
    """
    retyped_password = getpass("Confirm your password:")
    if retyped_password != password:
        print("The passwords do not match.")
        return False
    else:
        return True


def store_password(username: str, password: str) -> None:
    """Stores created usernames and passwords in a global dictionary

    Args:
        username (str): created username
        password (str): username's affiliated password
    """
    user_info[username] = password


def check_password(username: str, password: str) -> bool:
    """Look up and check username and password combo in the global dictionary

    Args:
        username (str): username to check
        password (str): password to check

    Returns:
        bool: True only if username exists and the password matches
    """
    try:
        return password == user_info[username]
    except KeyError:
        return False


def create_account():
    username = None
    while username is None:
        username = prompt_for_username()
    password = None
    while password is None:
        password = prompt_for_password(username)
        if password:
            retyped = check_create_password(password)
            if not retyped:
                password = None
    store_password(username, password)


def login():
    # In a real application, we would NOT reuse the "prompt_for"
    # functions, as it gives hints for username & password restrictions
    username = None
    while username is None:
        username = prompt_for_username()
    password = None
    while password is None:
        password = prompt_for_password(username)
    if check_password(username, password):
        print(f"Welcome {username}, thank you for correctly logging in!")
    else:
        print(f"Hey {username}, you may want to doublecheck your password...")


def main():
    command = input("Type 'create' or 'login': ")
    if command == "create":
        create_account()
    elif command == "login":
        login()
    else:
        print("You need to type either 'create' or 'login' to continue.")


# Only run this file if you need to invoke the script
if __name__ == "__main__":
    while True:
        main()
