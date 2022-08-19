def perfectSquare(num):
    num_result = str(num * num)
    num_str = str(num)
    num_result_slice = num_result[-len(num_str)::]
    if num_str == num_result_slice:
        print(num, "is a perfect square")
    else:
        print(num, "is not a perfect square")


perfectSquare(5)

