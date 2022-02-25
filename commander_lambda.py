from enum import unique


def solution(x, y):
    unique = [item for item in x if item not in y] + [
        item for item in y if item not in x
    ]
    return int(unique[0])


x = [13, 5, 2, 5]
y = [5, 2, 5, 7, 13]

print(solution(x, y))
