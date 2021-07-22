
szo = input("Mi legyen a szó?:")

# 0 3
# 1 2
# 2 1
#
#
# lapos
#
# 0 4
# 1 3
# 2 2
#
# bal >= jobb        lent ezt negáljuk!


palindrom_e=True
bal_index=0
jobb_index= len(szo) - 1
while bal_index < jobb_index:
    if szo[bal_index] != szo[jobb_index]:
        palindrom_e=False
        break
    bal_index +=1
    jobb_index -=1

if palindrom_e==False:
    print("Nem palindrom")
else:
    print("Palindrom")
