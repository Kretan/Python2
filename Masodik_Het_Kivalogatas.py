"""
Kiválogatás
A tömb elemit egy másik tömbbe rakom, feltételhez kötve.

Például: Adott a és b tömb. Az a tömb egész számokat tartalmaz. Az a tömbből az 5-nél kisebb számokat átrakom b tömbbe.
"""

listam=[1,2,3,12,15,17,15,7,8,9]
listam2=[]

i=0
while i< len(listam):
    if listam[i]<5:
        listam2.append(listam[i])
    i+=1

print (listam)
print(listam2)