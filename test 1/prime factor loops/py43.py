a = int(input())
b = int(input())
mnum = max(a, b)

while True:
    if mnum % a == 0 and mnum % b == 0:
        print(mnum)
        break
    mnum += 1
