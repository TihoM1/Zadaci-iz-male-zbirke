"""
Unose se dva cijela broja. Stampati rezultat i ostatak
dijeljenja koristeci samo sabiranje i oduzimanje
Unos: 31, 4 Izlaz: rez=7, ost=3
Unos: 156, 2 Izlaz: rez=78, ost=0
Unop: 32767, 13 Izlaz: rez = 2520, ost = 7
"""
deljenik = int(input())
delilac = int(input())
rezultat = 0
ostatak = 0
while deljenik >= delilac:
    deljenik -= delilac
    rezultat += 1
ostatak = deljenik
print('rez =', rezultat, 'ost =', ostatak) 
    