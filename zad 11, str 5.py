"""
Unose se brojevi dok se ne unese 0. Ispisati broj brojeva 
koji imaju tacno jednu neparnu cifru.

32, 4, 7, 0 -> 2
162, 32, 5, 19, 0 -> 2
"""
n = int(input())
neparne_c = 0
n_sa_samo_jednom = 0
while n != 0:
    while n > 0:
        if n%10%2 != 0:
            neparne_c += 1
        n//=10
    if neparne_c == 1:
        n_sa_samo_jednom+=1
    n=int(input())
print(n_sa_samo_jednom)