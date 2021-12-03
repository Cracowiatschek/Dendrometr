import dendro_formulas

print('Dendrometr 1.0.1')
print('')


class main:
    module = 'Run'
    while module == 'A' or module == 'B' or module == 'X' or 'Run':
        if module == 'Run':
            print('Moduły:')
            print('A. Moduł obliczania miąższości drzewa - met. proste')
            print('B. Moduł obliczania miąższości - met. sekcyjne')
            print('X. Wyjście')
            print('')
            module = input('Wybierz moduł: ')
        elif module == 'A':
            print('Moduł obliczania miąższości drzewa - wzory proste')
            print('Tryby:')
            print('A. wzór Hubera')
            print('B. wzór Smaliana')
            print('C. Wzór Hossfelda')
            print('D. Wzór Newtona')
            print('X. Cofnij')
            mode = str(input('Wybierz tryb: '))
            if mode == 'A':
                print(dendro_formulas.VHub(d1_2=int(input('Wpisz d1/2 (cm): ')),
                                           h=int(input('Wpisz h (m): '))))
                module = 'A'
            elif mode == 'B':
                print(dendro_formulas.VSmal(d0=int(input('Wpisz d0 (cm): ')),
                                            dl=int(input('Wpisz dl (cm): ')),
                                            h=int(input('Wpisz h (m): '))))
                module = 'A'
            elif mode == 'C':
                print(dendro_formulas.VHoss(d1_3=int(input('Wpisz d1_3 (cm): ')),
                                            dl=int(input('Wpisz dl (cm): ')),
                                            h=int(input('Wpisz h (m): '))))
                module = 'A'
            elif mode == 'D':
                print(dendro_formulas.VNew(d0=int(input('Wpisz 0 (cm): ')),
                                           d1_2=int(input('Wpisz d1_2 (cm): ')),
                                           dl=int(input('Wpisz dl (cm): ')),
                                           h=int(input('Wpisz h (m): '))))
                module = 'A'
            elif mode == 'X':
                module = 'Run'
            else:
                print('Error')
                module = 'Run'
        elif module == 'B':
            print('Moduł obliczania miąższości - met. sekcyjne')
            print('Tryby: ')
            print('A. wzór Hubera')
            print('B. wzór Smaliana')
            print('X. Cofnij')
            mode = str(input('Wybierz tryb: '))
            if mode == 'A':
                print('Instrukcja')
                print('1. Wpisz numer sekcji')
                print('2. Sekcje należy numerować od 1 wzwyż')
                print('3. Uzupełnij średnicę podstawy dolnej - d0, ''średnicę podstawy górnej - dl '
                      'i  długość - h sekcji')
                print('4. Jeśli chcesz zakończyć pomiar w numerze sekcji wpisz 0')
                print(dendro_formulas.sekVHub)
                module = 'B'
            elif mode == 'B':
                print(dendro_formulas.sekVSmal)
                module = 'B'
            elif mode == 'X':
                module = 'Run'
        elif module == 'X':
            break


print(main)
