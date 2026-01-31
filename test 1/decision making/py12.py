a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter a third number: "))
if a>b and a>c:
    print(f"{a} is the greatest")
elif b>a and b>c:
    print(f"{b} is the greatest")
elif c>a and c>b :
    print(f"{c} is the greatest")