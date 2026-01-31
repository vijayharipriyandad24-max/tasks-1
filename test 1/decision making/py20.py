cp=int(input("enter cost price: "))
sp =int(input("enter selling price"))
if cp>sp:
    print("loss")
elif sp>cp:
    print("profit")
elif cp==sp:
    print ("no profit no loss")
    