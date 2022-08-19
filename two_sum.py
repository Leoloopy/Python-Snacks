def two_sum(arr: list, ans: int) -> list:
    result = [-1, -1]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == ans:
                result[0] = i
                result[1] = j

    return result


def two_sum2(arr: list, ans: int) -> list:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == ans:
                return [i, j]
    return [-1, -1]





n = [3, -1, 5, 4]
target = 3

# print(two_sum(n, target))
# print(two_sum2(n, target))


