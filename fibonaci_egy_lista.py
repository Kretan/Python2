elem=int(input("Hanyadik elemre vagy kíváncsi?: "))
i=0
listam=[0,1]

while i < elem:

    a= listam[-1]
    b= listam[-2]
    c= a+b
    listam.append(c)
    i=i+1
    print(listam)
print ("Az elem értéke:", listam[-3])





