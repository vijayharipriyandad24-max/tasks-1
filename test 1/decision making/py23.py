a=int(input())
b=int(input())
c=int(input())
d=b**2-(4*a*c)
if d>0:
    print("Roots are real & distinct")
elif d==0:
    print("Roots are real & equal")
elif d<0:
    print("Roots are imaginary")