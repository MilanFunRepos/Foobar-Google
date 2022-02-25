from fractions import Fraction


def solution(pegs):
    arrayLength = len(pegs)
    if (not pegs) or arrayLength == 1:
        return [-1, -1]

    even = True if (arrayLength % 2 == 0) else False
    sum = (
        (-pegs[0] + pegs[arrayLength - 1])
        if even
        else (-pegs[0] - pegs[arrayLength - 1])
    )

    if arrayLength > 2:
        for index in range(1, arrayLength - 1):
            sum += 2 * (-1) ** (index + 1) * pegs[index]

    FirstGearRadius = Fraction(
        2 * (float(sum) / 3 if even else sum)
    ).limit_denominator()

    currentRadius = FirstGearRadius
    for index in range(0, arrayLength - 2):
        CenterDistance = pegs[index + 1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if currentRadius < 1 or NextRadius < 1:
            return [-1, -1]
        else:
            currentRadius = NextRadius

    return [FirstGearRadius.numerator, FirstGearRadius.denominator]


pegs = [4, 17, 50]

print(solution(pegs))
