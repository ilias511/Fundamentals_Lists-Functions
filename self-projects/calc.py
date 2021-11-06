import tkinter


def plus(x, y):
    print(x + y)


def minus(x, y):
    print(x - y)


def multi(x, y):
    print(x * y)


def div(x, y):
    print(x / y)
def user_select(number):
    if number == 1:
       plus(x=int(input()), y=int(input()))
    elif number == 2:
        minus(x=int(input()), y=int(input()))

    elif number == 3:

        multi(x=int(input()), y=int(input()))
    elif number == 4:

        div(x=int(input()), y=int(input()))
user_select(number=int(input()))
