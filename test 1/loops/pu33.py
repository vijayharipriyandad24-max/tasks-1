n=int(input())
rev =0
t=n
while n>0:
    div=n%10
    rev=rev*10+div
    n//=10
print(rev)
if t == rev:
    print("palindrome")
else:
    print("not palindrome")