PointOne = (2, 3)
PointTwo = (10, 8)

def EuclideanDistance(PointOne, PointTwo):
    differenceX = PointTwo[0] - PointOne[0]
    differenceY = PointTwo[1] - PointOne[1]

    hypotenuse = ((differenceX ** 2) + (differenceY ** 2)) ** 0.5

    return hypotenuse

print(EuclideanDistance(PointOne, PointTwo))