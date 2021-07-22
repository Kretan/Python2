listam = [2,4,6,8]

"""
osszeg = 0
for x in listam:
    osszeg += x

print (osszeg)
"""

osszeg = 0
i=0
while i < len(listam):
    osszeg += listam[i]
    i +=1

print(osszeg)