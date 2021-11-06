def char(start, stop):
    for i in range(start+1, stop):
        print(chr(i), end=' ')


start = ord(input())
stop = ord(input())
char(start, stop)
