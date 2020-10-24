"""
Program koji od broja abc kombinacijom cifara istog broja pravi najveci
broj:
input:412
      123
      243
output:421
       321
       432
"""
def kombinacija_cifara_za_naj_broj(sdj):
    """
    Procedura koja razdvaja broj na tri cifre, uopređuje ih, i
    štampa najveći mogući broj
    """
    jedinice = sdj % 10
    desetice = sdj//10%10
    stotine = sdj//100
    if jedinice > desetice and jedinice > stotine:
        if desetice > stotine:
            naj_broj = jedinice*100 + desetice*10 + stotine
        else:
            naj_broj = jedinice*100 + stotine*10 + desetice
    elif desetice > jedinice and desetice > stotine:
        if jedinice > stotine:
            naj_broj = desetice*100 + jedinice*10 + stotine
        else:
            naj_broj = desetice*100 + stotine*10 + jedinice
    else:
        if jedinice > desetice:
            naj_broj = stotine*100 + jedinice*10 + desetice
        else: 
            naj_broj = stotine*100 + desetice*10 + jedinice
    print(naj_broj)

n = int(input("Unesite trocifren broj: "))
kombinacija_cifara_za_naj_broj(n)