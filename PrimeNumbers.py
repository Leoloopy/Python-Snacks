value = int(input("Enter a number: "))
sentinel = -1

while value != sentinel:
    if value == 2:
        print("YOUR NUMBER IS A PRIME NUMBER!")
    if value > 1 and value % 2 == 1:
        print("YOUR NUMBER IS A PRIME NUMBER!")
    else:
        print("YOUR NUMBER (IS NOT) A PRIME NUMBER!")
    value = int(input("Enter a number or enter -1 to quit: "))
