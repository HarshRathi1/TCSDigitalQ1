bank=[]
principal=int(input())
years=int(input())
for i in range(0,2):
    slab=int(input())
    sum=0
    for i in range(0,slab):
        time,roi=[float(i) for i in input().split()]
        square=pow((1+roi),(time*12))
        emi=(principal*roi)/(1-1/square)
        sum+=emi
    bank.append(sum)
if bank[0]<bank[1]:
    print("Choosing Bank A")
else:
    print("Choosing Bank B")
