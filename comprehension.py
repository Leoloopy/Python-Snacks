# squares = [num ** 2 for num in range(1, 11)]
# print(squares)
#
# names = ["bimpe", "Banke", "abimbola", "kelechi", "James", "Olalekan", "Rachael"]
# name = [name for name in names if name.istitle()]
# print(name)

# collecting input
#
# my_names = [input(f"{i + 1}. Names?") for i in range(0,5)]
#
# print(my_names)

even_num = [even ** 2 if even % 2 == 0 else even ** 3 for even in range(1, 11)]
print(even_num)



