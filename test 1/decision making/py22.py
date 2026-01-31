a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print("Equilateral")
if a==b or b==c or c==a:
    print("Isosceles")
if a!=b and b!=c and c!=a:
    print("Scalene")