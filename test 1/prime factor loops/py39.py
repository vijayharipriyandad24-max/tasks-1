n = int(input())
total = 0

for i in range(1, n//2 + 1):
    if n % i == 0:
        total += i

if total == n and n != 0:
    print("perfect")
else:
    print("not perfect")
