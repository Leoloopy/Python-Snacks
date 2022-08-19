import string


def count_words(words) -> string:
    count: int = 0
    for i in words:
        if i.isupper():
            count += 1
    return count


print("There are {} words in this camelCase sentence".format(count_words('youAreTheHandicapYouMustFace')))
