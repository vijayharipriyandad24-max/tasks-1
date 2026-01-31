n = int(input())
count = 0
sum=0
t=n
temp =n
while temp>0:
    count+=1
    temp//=10
temp =n
while temp > 0:
    digit = temp % 10
    sum+= digit ** count
    temp //= 10 
if sum == t:
    print("crct")
else:
    print("not crct")


