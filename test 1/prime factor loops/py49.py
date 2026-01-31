n = int(input())
largest = -1
second = -1

while n > 0:
    d = n % 10
    if d > largest:
        second = largest
        largest = d
    elif d != largest and d > second:
        second = d
    n //= 10

print(second)
