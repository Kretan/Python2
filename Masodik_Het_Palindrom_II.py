"""

3. Palindrom II.
Írj programot, amelyik egy mondatról eldönti, hogy palindrom-e. Közismert magyar nyelvű palindrom mondat
az „Indul a görög aludni.” Ez abban különbözik az előző feladattól, hogy most a szóközöket és az írásjeleket
ki kell szűrnöd, vagyis csak a betűket kell megtartani, és úgy kell vizsgálni a sztringet.
És persze figyelni arra is, hogy a kisbetűk és a nagybetűk nem különböznek.
"""



vizsgalando_mondat = list(input("Adj meg egy mondatot!: "))
megforditva =[]
vizsgalando_mondat2 =[]


for aktualis_char in vizsgalando_mondat:
    if aktualis_char != " " and aktualis_char.isalnum()==True:
        vizsgalando_mondat2 += aktualis_char.lower()
print(vizsgalando_mondat2)

hossz=len(vizsgalando_mondat2)
i=-1
while i != (-1*hossz)-1:
    megforditva += vizsgalando_mondat2[i]
    i-=1
print(megforditva)

if megforditva == vizsgalando_mondat2:
    print("Palindrom")
else:
    print("Nem palindrom")

