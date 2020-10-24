"""
Unose se dva razlomka i operacija koju zelimo da izvrsimo nad njima.
(ovo nije finalna verzija programa, planiram da dodam funkciju koja skracuje razlomke,
radi kraceg koda)
Input:2 3 1 2 sabiranje
Output: 7/6
-Pojasnjenje: prva dva broja su brojilac i imenilac prvog razlomka
              druga dva broja su brojilac i imenilac drugog razlomka
              2/3 + 1/2 = 7/6
"""
def operacije_sa_razlomcima(a, b, c, d, operacija):
    brojilac = 0
    imenilac = 0
    if operacija == 'sabiranje':
        brojilac = a*d+b*c  #racunanje brojioca i imenioca pri sabiranju
        imenilac = b*d
        if brojilac%imenilac == 0: #skracivanje razlomaka ↓
            brojilac //= imenilac
            imenilac //= imenilac
            print(brojilac, '/', imenilac)
        elif imenilac % brojilac ==0:
            imenilac //= brojilac
            brojilac //= brojilac
            print(brojilac, '/', imenilac)
        else:
            print(brojilac, '/',imenilac)
    elif operacija == 'oduzimanje':
        brojilac = 3     #racunanje brojioca i imenioca pri oduzimanju
        imenilac = b*d
        if brojilac % imenilac == 0: #skracivanje razlomaka ↓
            brojilac //= imenilac
            imenilac //= imenilac
            print(brojilac, '/', imenilac)
        elif imenilac % brojilac ==0:
            imenilac //= brojilac
            brojilac //= brojilac
            print(brojilac, '/', imenilac)
        else:
            print(brojilac, '/',imenilac)
    elif operacija=='mnozenje':
        brojilac = a*c          #racunanje brojioca i imenioca pri mnozenju
        imenilac = b*d
        if brojilac % imenilac == 0: #skracivanje razlomaka ↓
            brojilac //= imenilac
            imenilac //= imenilac
            print(brojilac, '/', imenilac)
        elif imenilac % brojilac ==0:
            imenilac //= brojilac
            brojilac //= brojilac
            print(brojilac, '/', imenilac)
        else:
            print(brojilac, '/',imenilac)
    elif operacija=='dijeljenje':
        brojilac = a*d           #racunanje brojioca i imenioca pri mnozenju
        imenilac = b*c
        if brojilac % imenilac == 0:#skracivanje razlomaka ↓
            brojilac //= imenilac
            imenilac //= imenilac
            print(brojilac, '/', imenilac)
        elif imenilac % brojilac ==0:
            imenilac //= brojilac
            brojilac //= brojilac
            print(brojilac, '/', imenilac)
        else:
            print(brojilac, '/',imenilac)
        

A=int(input('Unesite brojeve: '))
B=int(input())
C=int(input())
D=int(input())
op=(input('Unesite operaciju: '))
operacije_sa_razlomcima(A, B, C, D, op)

