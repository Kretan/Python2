
"""
Keresés
Lineáris vagy szekvenciális keresés néven is ismert, mivel végig megyünk a számokon sorba.

Adott elem szerepel-e a tömbben és hányadik helyen.
"""

keresett_szam=int(input("Milyen számot keressek?: "))

listam=[2,3,4,-6,7,-6]

szerepel=False
i=0
while i < len(listam):
    if listam[i]==keresett_szam:
        szerepel=True
        print(keresett_szam, "szerepel, és a(z)", i, "indexű helyen van a listában")

    i+=1

if szerepel==False:
    print(keresett_szam, "nem szerepel a listában")




