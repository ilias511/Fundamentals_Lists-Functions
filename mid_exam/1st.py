orders = int(input())
total_price = 0

for order in range(1,orders+1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    order_price = ((days * capsules_count) * price_per_capsule)
    print(f"The price for the coffee is: ${order_price:.2f}")
    total_price+=order_price

print(f"Total: ${total_price:.2f}")