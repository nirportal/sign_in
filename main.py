import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        for inx, char in enumerate(self._username):
            if not char.isalpha() and not char.isdigit() and not char == "_":
                print("The username contains an illegal"
                      " character " + char + " at index " + str(inx))


class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        print("Username Too Short")


class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        print("Username Too Long")


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        print("The Password Missing Character", end=' ')


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        super().__str__()
        print("(Uppercase)")


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        super().__str__()
        print("(Lowercase)")


class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        super().__str__()
        print("(Digit)")


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        super().__str__()
        print("(Special)")


class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        print("Password Too short")


class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        print("Password Too Long")


def check_input(username, password):
    """
    func checks if the user input(username and password) is "ligel",
    if one of them is iligel, a specific message for what went wrong will
    be printed.
    :param: username: username input
    :param password: password input
    :type username: str
    :type password: str
    :return: None
    """

    #  checks usename validation
    try:
        if not check_username_validation(username):
            raise UsernameContainsIllegalCharacter(username)
    except UsernameContainsIllegalCharacter as e:
        e.__str__()
        return False
    else:
        try:
            if len(username) < 3:
                raise UsernameTooShort(username)
        except UsernameTooShort as e:
            e.__str__()
            return False
        else:
            try:
                if len(username) > 16:
                    raise UsernameTooLong(username)
            except UsernameTooLong as e:
                e.__str__()
                return False
            else:
                #  checks password validation
                try:
                    if len(password) < 8:
                        raise PasswordTooShort(password)
                except PasswordTooShort as e:
                    e.__str__()
                    return False
                else:
                    try:
                        if len(password) > 41:
                            raise PasswordTooLong(password)
                    except PasswordTooLong as e:
                        e.__str__()
                        return False
                    else:
                        try:
                            if check_password_validation(password)\
                                    == "isupper":
                                raise PasswordMissingUppercase(password)
                        except PasswordMissingUppercase as e:
                            e.__str__()
                            return False
                        else:
                            try:
                                if check_password_validation(password) \
                                        == "islower":
                                    raise PasswordMissingLowercase(password)
                            except PasswordMissingLowercase as e:
                                e.__str__()
                                return False
                            else:
                                try:
                                    if check_password_validation(password) \
                                            == "isdigit":
                                        raise PasswordMissingDigit(password)
                                except PasswordMissingDigit as e:
                                    e.__str__()
                                    return False
                                else:
                                    try:
                                        if check_password_validation(password)\
                                            \
                                                == "isspecial":
                                            raise \
                                                PasswordMissingSpecial(
                                                    password)
                                    except PasswordMissingSpecial as e:
                                        e.__str__()
                                        return False
                                    else:
                                        print("OK")
                                        return True


def check_username_validation(word):
    for char in word:
        if not char.isalpha() and not char.isdigit() and not char == "_":
            return False
    return True


def check_password_validation(word):
    isupper = False
    islower = False
    isdigit = False
    isspecial = False
    for char in word:
        if char.isupper():
            isupper = True
        if char.islower():
            islower = True
        if char.isdigit():
            isdigit = True
        if char in string.punctuation:
            isspecial = True
    if not isupper:
        return "isupper"
    if not islower:
        return "islower"
    if not isdigit:
        return "isdigit"
    if not isspecial:
        return "isspecial"


def main():
    user_username = input("enter a username: ")
    user_password = input("enter a password: ")
    valid_input = check_input(user_username, user_password)
    while not valid_input:
        print("try again")
        user_username = input("enter a username: ")
        user_password = input("enter a password: ")
        valid_input = check_input(user_username, user_password)


if __name__ == '__main__':
    main()
