listam =[5,6,90,0,0,1]


"""
van_negativ=False
i=0
while i< len(listam) and van_negativ==False:
    if listam[i]<0:
        van_negativ=True
        print("Legalább egy negatív számot találtam")

    i +=1

if van_negativ==False:
    print("Nem találtam negatív számot")
"""

van_negativ=False
for x in listam:
    if x < 0:
        van_negativ=True

if van_negativ==True:
    print("Legalább egy negatív számot találtam")
else:
    print("Nem találtam negatív számot")
