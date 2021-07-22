"""
1. Mindentegybevéve
Írj egy olyan programot, mely egy szövegből kiszedi a szóközöket!
"""

szoveg = "Ez itt a való világ."

szoveg2 =""

for aktualis_char in szoveg:

    if aktualis_char != " ":
        szoveg2 += aktualis_char
print(szoveg2)
