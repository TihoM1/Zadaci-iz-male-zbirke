"""
Broj četvorocifrenih brojeva ciji je zbir prve i posljednje cifre jednak
proizvodu druge i trece cifre:
Rezultat: 207
"""
i=1000
br_brojeva=0
while i < 9999:
    jedinica = i%10
    desetica = i//10%10
    stotina = i//100%10
    hiljada = i//1000
    if hiljada + jedinica == desetica * stotina:
        br_brojeva+=1
    i+=1
print(br_brojeva)