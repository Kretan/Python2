
vizsgalando_szo = input("Adj meg egy szót!: ")
hossz = len(vizsgalando_szo)
megforditva =[]

i=len(vizsgalando_szo)-1
while i >=0:
    megforditva +=vizsgalando_szo[i]
    i-=1

print(megforditva)