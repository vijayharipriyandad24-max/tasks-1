n=int(input())
ce=0
co=0
while n>0:
    if n%2==0:
        ce+=1
        n//=10
    elif n%2!=0:
        co+=1
        n//=10
print(ce)
print(co)