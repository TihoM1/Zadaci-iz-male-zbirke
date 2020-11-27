"""
Uneseni broj rastaviti na dva broja ciji je proizvod minimalan.
unos: 31 izlaz: 3, 1
unos: 234 izlaz: 2, 34
unos: 8615 izlaz: 86, 15
"""
n = int(input())
i = 10
min_br_1=n%10
min_br_2=n//10
while n >= i:
    prvi_br = n % i
    drugi_br = n // i
    if prvi_br * drugi_br < min_br_1 * min_br_2:
        min_br_1 = prvi_br
        min_br_2 = drugi_br
    i*=10
print(min_br_1, min_br_2)

