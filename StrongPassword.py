import re


def hasChar(pin):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if not (regex.search(pin) is None):
        return True
    # else:
    return False


def check_pin(pin):
    state = True
    if len(pin) < 6:
        print("pin too short")
        state = False
    if not any(check.isdigit() for check in pin):
        print("Must contain at least one number")
        state = False
    if not any(check.islower() for check in pin):
        print("Must have at least one lower case")
        state = False
    if not any(check.isupper() for check in pin):
        print("Must have at least one upper case")
        state = False
    if not hasChar(pin):
        print("Must contain a special character")
        state = False
    if state:
        return "Strong pin"


# print(check_pin("2y"))
print(hasChar("2y"))


