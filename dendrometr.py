import dendro_formulas


print('Dendrometr 1.0.1')
print('')
print('Hi User!')


class start:
    print('Moduły:')
    print('A. Moduł obliczania miąższości drzewa - met. proste')
    print('B. Moduł obliczania miąższości - met. sekcyjne')
    print('X. Wyjście')
    print('')


tryb = 0


class modules:
    tryb = input('Wybierz moduł: ')

        while tryb == 'A' or tryb == 'B' or tryb == 'X':
            if tryb == 'A':
                print('Tryby:')
                print('A. wzór Hubera')
                print('B. wzór Smaliana')
                print('C. Wzór Hossfelda')
                print('D. Wzór Newtona')
                module = str(input('Wybierz tryb: '))
                if module == 'A':
                    print(dendro_formulas.VHub(d1_2=int(input('Wpisz d1/2 (cm): ')),
                                               h=int(input('Wpisz h (m): '))))
                    print(start)
                    print(modules)
                elif module == 'B':
                    print(dendro_formulas.VSmal(d0=int(input('Wpisz d0 (cm): ')),
                                                dl=int(input('Wpisz dl (cm): ')),
                                                h=int(input('Wpisz h (m): '))))
                    print(start)
                    print(modules)
                elif module == 'C':
                    print(dendro_formulas.VHoss(d1_3=int(input('Wpisz d1_3 (cm): ')),
                                                dl=int(input('Wpisz dl (cm): ')),
                                                h=int(input('Wpisz h (m): '))))
                    print(start)
                    print(modules)
                elif module == 'D':
                    print(dendro_formulas.VNew(d0=int(input('Wpisz 0 (cm): ')),
                                               d1_2=int(input('Wpisz d1_2 (cm): ')),
                                               dl=int(input('Wpisz dl (cm): ')),
                                               h=int(input('Wpisz h (m): '))))
                    print(start)
                    print(modules)
                elif module == 'X':
                    print(start)
                    print(modules)
                else:
                    print('Error - back to start')
                    print(start)
                    print(modules)
            elif tryb == 'B':
                print(dendro_formulas.Vsek)
            elif tryb == 'X':
                pass
            else:
                print('Error - back to start')
                print(start)
                print(modules)


print(start)
