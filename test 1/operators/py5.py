days=int(input())
yer=days//365
remy = days%365
wek= remy // 7
day =remy- (wek*7)
print(yer,wek,day)