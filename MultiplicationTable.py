num = int(input("Enter your Multiplication Table: "))

sentinel = -1
while num != -1:
    for i in range(1, 13):
        result = num * i
        print(num, "*", i, "=", result)
    num = int(input("Enter your Multiplication Table: "))


