n=int(input())
rev =0
while n>0:
    div=n%10
    rev=rev*10+div
    n//=10
print(rev)