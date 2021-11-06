numbers = input().split(" ")
string_big = ''
big = sorted(numbers, reverse=True)

for s in big:
    string_big += s
print(string_big)