"""
Program koji stampa broj nula na kraju faktorijela:
input:4
      6
      12
output:0
       1
       2
"""
def faktorijel_broja_n(n):
    """
    Funkicja koja racuna faktorijel broja n
    """
    fact_n=1
    i=1
    for i in range (1,n+1):
        fact_n*=i
    return fact_n

def broj_nula_na_kraju_faktorijela(factorijel):
    """
    Procedura koja stampa broj nula na kraju faktorijela
    """
    broj_nula=0
    posljednja_cifra_fact=0
    while factorijel>=0:
        posljednja_cifra_fact=factorijel%10
        factorijel//=10
        if posljednja_cifra_fact==0:
            broj_nula+=1
        else:
            print( 'Broj nula na kraju faktorijela iznosi: ', broj_nula)
            break

x =int(input('Unesite neki broj: '))
f = faktorijel_broja_n(x)
print(f)
broj_nula_na_kraju_faktorijela(f)