"""
Napisati program koji racuna aritmeticku sredinu trocifrenih brojeva
ciji je zbir cifara 15 i zavrsavaju se peticom.
Rjesenje: 555
"""
zavrsava_se_peticom = 105
i=0
suma = 0
while zavrsava_se_peticom <= 999:
    jedinice = zavrsava_se_peticom % 10
    desetice = zavrsava_se_peticom // 10 % 10
    stotine = zavrsava_se_peticom // 100
    if jedinice + desetice + stotine == 15:
        suma += zavrsava_se_peticom
        i += 1
    else:
        pass
    zavrsava_se_peticom += 10
print(suma/i)