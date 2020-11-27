"""
Napisati program koji ce pronaci broj za koji vazi:
1*2*3*...*n=3628800. Rjesenje = 10
"""
fact_n=1    
i=1
while i > 0:
    if fact_n == 3628800:
        print(i)
        break
    else:
        i+=1
        fact_n*=i
    