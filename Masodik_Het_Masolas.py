"""
Másolás
Egy sorozat elemeit átmásolom egy másik sorozatba, miközben valamilyen átalakítást végzek az egyes elemeken.

"""

listam=["a","b","c","d","e","f"]
listam2=[]

i=0
while i < len(listam):
    listam2 += listam[i].upper()
    i+=1

print(listam2)
