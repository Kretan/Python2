listam=[1,10,3,1,4,0,0,2,12,4]

#listam2=[]
listam3=[]

"""
i=0
for x in listam:
    if listam[i] < 5:
        listam2.append(listam[i])
    i +=1
"""


i=0
while i < len(listam):
    if listam[i]<5:
        listam3.append(listam[i])
    i+=1


#print(listam2)
print(listam3)