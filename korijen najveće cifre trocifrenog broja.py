import math
def naj_cifra(trocifren_broj):
    jedinice = trocifren_broj % 10
    desetice = trocifren_broj//10%10
    stotine = trocifren_broj //100
    cifre = {jedinice, desetice, stotine}
    return max(cifre)

def korijen_naj_cifre(n):
    return math.sqrt(naj_cifra(n))

N = int(input())
print(korijen_naj_cifre(N))