num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def smallest(x, y, p):
    if x < y and x < p:
        return x
    elif y < x and y < p:
        return y
    elif p < x and p < y:
        return p


smallest(x=num_1, y=num_2, p=num_3)
