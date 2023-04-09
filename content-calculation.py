from math import pi

def obsah_obdelnika(c, d):
    obsah = c * d
    return obsah

def obsah_kruhu(r):
    obsah = pi * (r ** 2)
    return obsah

def obsah_elipsy(a, b):
    obsah = pi * a * b
    return obsah

def pokracovat():  # Výběr, zda chce uživatel pokračovat nebo práci ukončit
    while True:
        pokracovat = input('Přeješ si vypočítat něco dalšího? (odpověz "ano" nebo "ne") ')
        if pokracovat  == 'ano':
            tvar = 0
            return (tvar)
            
        elif pokracovat == 'ne':
            tvar = 'ne'
            return (tvar)

        else:
            print('\nOdpověz prosím pouze "ano" nebo "ne".')

tvar = 0

while tvar != 'ne':

    tvar = input('''
Pro který tvar chceš vypočítat obsah?
1. Čtverec
2. Obdélník
3. Kruh
4. Elipsa

Zadej: ''')

    if tvar == '1' or tvar == '1.' or tvar == 'Čtverec' or tvar == 'čtverec' or tvar == '1. Čtverec' or tvar == '1. čtverec':
        
        while True:
            try:
                c = int(input('Zadej délku strany: '))
                print('Obsah čtverce je: ', obsah_obdelnika(c, c), '.', sep='', end='\n\n')       
                tvar = pokracovat()
                break
            except ValueError: 
                print('\nZadej prosím kladné celé číslo.')

    elif tvar == '2' or tvar == '2.' or tvar == 'Obdélník' or tvar == 'obdélník' or tvar == '2. Obdélník' or tvar == '2. obdélník':

            while True:
                try:
                    c = int(input('Zadej délku první strany: '))
                    d = int(input('Zadej délku druhé strany: '))
                    print ('Obsah obdélníka je: ', obsah_obdelnika(c, d), '.', sep = '', end='\n\n')
                    tvar = pokracovat()
                    break
                except ValueError: 
                    print('\nZadej prosím kladná celá čísla.')

    elif tvar == '3' or tvar == '3.' or tvar == 'Kruh' or tvar == 'kruh' or tvar == '3. Kruh' or tvar == '3. kruh':
                
        while True:
            try:
                r = int(input('Zadej délku poloměru: '))
                print('Obsah kruhu je: ', obsah_kruhu(r), '.', sep = '', end='\n\n')    
                tvar = pokracovat()
                break
            except ValueError: 
                print('\nZadej prosím kladné celé číslo.')

    elif tvar == '4' or tvar == '4.' or tvar == 'Elipsa' or tvar == 'elipsa' or tvar == '4. Elipsa' or tvar == '4. elipsa':
        
            while True:
                try:
                    a = int(input('Zadej délku první poloosy: '))
                    b = int(input('Zadej délku druhé poloosy: '))
                    print('Obsah elipsy je: ', obsah_elipsy(a, b), '.', sep = '', end='\n\n')
                    tvar = pokracovat()
                    break
                except ValueError: 
                    print('\nZadej prosím kladná celá čísla.')

    else:
        print('\nVyber prosím jeden z uvedených tvarů.')

print('Dobrá, tak zase příště nashledanou.')