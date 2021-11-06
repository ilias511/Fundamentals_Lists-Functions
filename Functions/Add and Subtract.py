num_1= int(input())
num_2= int(input())
num_3= int(input())

def add_and_subtract(x, y, p):
    def sum_numbers(x, y):
        return x+y
    sum_numbers(x=num_1, y=num_2)

    def subtract(x, y, p):
        return sum_numbers(x, y) - p

    print(subtract(x=num_1, y=num_2, p=num_3))


(add_and_subtract(x=num_1, y=num_2, p=num_3))