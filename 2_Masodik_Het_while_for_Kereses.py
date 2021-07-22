#vleg a for ciklus nem a legjobb, ha az index kiírására is szükség van

keresett_szam=int(input("Milyen számot keressek?: "))

listam=[2,3,4,-6,7,-6]

szamlalo = 0
index=0
szerepel=False
for x in listam:
    if x ==keresett_szam:
        szerepel=True
        index=listam.index(x)
        szamlalo +=1

if szerepel ==True:
    print("A keresett szam", szamlalo, "alkalommal szerepel a listában", "és az első előfordulás indexe:", index)
else:
    print("A keresett számot nem találtam")



"""
szerepel=False
i=0
while i < len(listam):
    if listam[i]==keresett_szam:
        szerepel=True
        print(keresett_szam, "szerepel, és a(z)", i, "indexű helyen van a listában")

    i+=1

if szerepel==False:
    print(keresett_szam, "nem szerepel a listában")
"""
