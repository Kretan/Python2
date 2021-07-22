"""
2. Palindrom I.
Írj programot, amelyik eldönti egy szóról, hogy palindrom-e!
Például az „abba” és a „görög” ilyenek: visszafelé olvasva ugyanazt a szót kapjuk.
"""

vizsgalando_szo = (input("Adj meg egy szót!: "))
hossz = len(vizsgalando_szo)
megforditva =[]

i=-1
while i != (-1*hossz)-1:
    megforditva +=(vizsgalando_szo[i])
    i-=1

vegeredmeny = ""
if vizsgalando_szo == megforditva:
    for aktualis_char in vizsgalando_szo:
        vegeredmeny += aktualis_char                #hogy stringként tudjam kiírni
        print("Az a szó, hogy", vegeredmeny, "palindrom.")

else:
    for aktualis_char in vizsgalando_szo:
        vegeredmeny += aktualis_char
        print("Az a szó, hogy", vegeredmeny, " nem palindrom.")

