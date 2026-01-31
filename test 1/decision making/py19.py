balance = int(input("enter a balance"))
draw = int(input("enter amt to withdraw"))
min=balance-draw
if (draw%100==0 and draw<=balance and min>500) :
    print("sucessfull")
else:
    print("rejected")
     
