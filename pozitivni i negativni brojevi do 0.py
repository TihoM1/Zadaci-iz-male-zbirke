def unosenje_do_nule(n):
    n_poz=0
    n_neg=0
    while n!=0:
        if n>0:
            n_poz+=1
            n=int(input())
    
        else:
            n_neg+=1
            n=int(input())
    print(n_poz," Pozitivnih", n_neg, " Negativnih" )

uneseni_broj=int(input())
unosenje_do_nule(uneseni_broj)