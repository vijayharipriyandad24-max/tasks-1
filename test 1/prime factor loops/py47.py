n = int(input())
t = n
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

if t % sum == 0:
    print("harshad")
else:
    print("not harshad")
