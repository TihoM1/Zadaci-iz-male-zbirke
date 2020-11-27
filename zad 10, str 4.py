"""
Unose se brojevi dok se ne unese 0. Treba ispisati
koliko brojeva je imalo bar jednu parnu cifru.

Unos: 31, 4, 7, 0  Izlaz: 1
Unos: 156, 2, 322, 17, 4, 0  Izlaz: 4
Unos: 32767, 13, 27, 46, 89, 0  Izlaz: 4
"""
n = int(input())
n_sa_parnom_c = 0
while n != 0:
    while n > 0:
        if n%10%2 == 0:
            n_sa_parnom_c+=1
            break
        else:
            n//=10
    n=int(input())
print(n_sa_parnom_c)