listam = [1,2,3,4,5,6,3,5,3,8,3,3,3]

keresett_szam=3
szamlalo=0
for x in listam:
    if x==keresett_szam:
        szamlalo +=1

print(szamlalo)

#####

listam = ["a","b","v","b","n","f","d","b"]

keresett_betu="b"
szamlalo=0
for x in listam:
    if x==keresett_betu:
        szamlalo +=1

print(szamlalo)