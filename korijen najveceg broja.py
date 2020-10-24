"""
Program koji štampa kvadratni korijen najvece cifre broja:
(koristimo math biblioteku)
input:412 -> output:2
input:592 -> output:3
"""
import math
def korijen_najvece_cifre(najCifra):
    """
    Funkcija koja vraca korijen od najCifra iz naredne funkcije
    """
    korijen = math.sqrt(najCifra)
    print(korijen)

def najveca_cifra_broja(uneseni_broj):
    """
    Funkcija koja vraca najvecu cifru unesenog broja
    """
    jedinica = uneseni_broj%10
    desetica = (uneseni_broj//10)%10
    stotina = uneseni_broj//100

    if jedinica > desetica and jedinica > stotina:
        return jedinica
    elif desetica > jedinica and desetica > stotina:
        return desetica
    else:
        return stotina

n=float(input("Unesite trocifren broj: "))
korijen_najvece_cifre(najveca_cifra_broja(n))