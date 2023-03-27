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

def pokracovat():
    while True:
        pokracovat = input('Přeješ si vypočítat něco dalšího? (odpověz "ano" nebo "ne") ')
        if pokracovat  == 'ano':
            tvar = input('''
Pro který tvar chceš vypočítat obsah?
1. Čtverec
2. Obdélník
3. Kruh
4. Elipsa

Zadej: ''')
            break
            
        elif pokracovat == 'ne':
            tvar = 'ne'
            break

        else:
            print('\nOdpověz prosím pouze "ano" nebo "ne".')
    return (tvar)


tvar = input('''
Pro který tvar chceš vypočítat obsah?
1. Čtverec
2. Obdélník
3. Kruh
4. Elipsa

Zadej: ''')

while True:
    if tvar == '1' or tvar == '1.' or tvar == 'Čtverec' or tvar == 'čtverec' or tvar == '1. Čtverec' or tvar == '1. čtverec':
        c = int(input('Zadej délku strany: '))
        print('Obsah čtverce je: ', obsah_obdelnika(c, c), '.', sep='', end='\n\n')
        
        tvar = pokracovat()

    elif tvar == '2' or tvar == '2.' or tvar == 'Obdélník' or tvar == 'obdélník' or tvar == '2. Obdélník' or tvar == '2. obdélník':
        c = int(input('Zadej délku první strany: '))
        d = int(input('Zadej délku druhé strany: '))
        print ('Obsah obdélníka je: ', obsah_obdelnika(c, d), '.', sep = '', end='\n\n')

        tvar = pokracovat()

    elif tvar == '3' or tvar == '3.' or tvar == 'Kruh' or tvar == 'kruh' or tvar == '3. Kruh' or tvar == '3. kruh':
        r = int(input('Zadej délku poloměru: '))
        print('Obsah kruhu je: ', obsah_kruhu(r), '.', sep = '', end='\n\n')

        tvar = pokracovat()

    elif tvar == '4' or tvar == '4.' or tvar == 'Elipsa' or tvar == 'elipsa' or tvar == '4. Elipsa' or tvar == '4. elipsa':
        a = int(input('Zadej délku první poloosy: '))
        b = int(input('Zadej délku druhé poloosy: '))
        print('Obsah obdélníka je: ', obsah_elipsy(a, b), '.', sep = '', end='\n\n')

        tvar = pokracovat()
    
    elif tvar == 'ne':
        print('Dobrá, tak zase příště nashledanou.')
        break

    else:
        tvar = input('''
Pro který tvar chceš vypočítat obsah?
1. Čtverec
2. Obdélník
3. Kruh
4. Elipsa
    
Zadej: ''')