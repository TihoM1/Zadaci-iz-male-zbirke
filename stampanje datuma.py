"""
Unosi se datum u formatu dd. mm. gggg.
Umjesto mm unijeti ime mjeseca.
"""
def mm_to_mjesec(mm):
    mjeseci = ['Januar', 'Februar', 'Mart', 'April', 'Maj', 'Jun','Jul', 'Avgust','Septembar', 'Oktobar', 'Novembar', 'Decembar'] 
    return mjeseci[mm-1]

dani = input()
mjesec = int(input())
godina = input()
print(dani+'.', mm_to_mjesec(mjesec), godina+'.')