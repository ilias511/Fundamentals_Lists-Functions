numbers = [int(n) for n in input().split(',')]


positives = ', '.join([str(p) for p in numbers if p >=0])
negatives = ', '.join([str(n) for n in numbers if n<0])
even = ', '.join([str(e) for e in numbers if e % 2==0])
odd = ', '.join([str(o) for o in numbers if o % 2!=0])

print(f"Positive: {positives}")
print(f"Negative: {negatives}")
print(f"Even: {even}")
print(f"Odd: {odd}")
