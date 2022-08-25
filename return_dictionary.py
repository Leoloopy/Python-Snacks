# def return_dictionary(structures):
#     dictKeys = {}
#     for i in structures:
#         if i in structures:
#             dictKeys[i] += 1
#         else:
#             dictKeys[i] = 1
#     return dictKeys
#
#
# num = [1, 2, 4, 5, 6, ]
# print(return_dictionary("Hello"))


def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}
    for item in iterable:
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    return item_dict


# num = [1, 2, 4, 5, 6, ]
print(counter("Hello"))
