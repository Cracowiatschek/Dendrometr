import dendro_formulas

print('Dendrometr 1.0.1')
print('')
print('Hi User!')


class main:
    module = 'Run'
    while module == 'A' or module == 'B' or module == 'X' or 'Run':
        if module == 'Run':
            print('Modules:')
            print('A. Module tree volume calculating - simple mod.')
            print('B. Module tree volume calculating - section mod.')
            print('X. Exit')
            print('')
            module = input('Choose your module: ')
        elif module == 'A':
            print('Module tree volume calculating - simple mod. ')
            print('Models:')
            print("A. Huber's model")
            print("B. Smalian's model")
            print("C. Hossfeld's model")
            print("D. Newton's model")
            print('X. Return')
            mode = str(input('Choose model: '))
            if mode == 'A':
                print(dendro_formulas.VHub(d1_2=int(input('Write diameter in half lenght of tree = d1/2 (cm): ')),
                                           h=int(input('Write lenght of tree = h (m): '))))
                module = 'A'
            elif mode == 'B':
                print(dendro_formulas.VSmal(d0=int(input('Write base diameter = d0 (cm): ')),
                                            dl=int(input('Write top diameter = dl (cm): ')),
                                            h=int(input('Write lenght of tree = h (m): '))))
                module = 'A'
            elif mode == 'C':
                print(dendro_formulas.VHoss(d1_3=int(input('Write diameter in 1/3 lenght of tree = d1/3 (cm): ')),
                                            dl=int(input('Write top diameter = dl (cm): ')),
                                            h=int(input('Write lenght of tree = h (m): '))))
                module = 'A'
            elif mode == 'D':
                print(dendro_formulas.VNew(d0=int(input('Write diameter in base of tree = 0 (cm): ')),
                                           d1_2=int(input('Write diameter in half lenght of tree = d1/2 (cm): ')),
                                           dl=int(input('Write top diameter = dl (cm): ')),
                                           h=int(input('Write lenght of tree = h (m): '))))
                module = 'A'
            elif mode == 'X':
                module = 'Run'
            else:
                print('Error')
                module = 'Run'
        elif module == 'B':
            print('Module tree volume calculating - section mod.')
            print('Models: ')
            print("A. Huber's model")
            print("B. Samlian's model")
            print('X. Return')
            mode = str(input('Choose your model: '))
            if mode == 'A':
                print('Instruction')
                print('1. Write number of section')
                print('2. Section must be number from 1')
                print('3. Write diameter in half of section - d1/2 and lenght of section - h')
                print('4. If you want to end of measurement write 0 in section')
                print(dendro_formulas.sekVHub(sek='Run', d1_2=0, h=0))
                module = 'B'
            elif mode == 'B':
                print('Instruction')
                print('1. Write number of section')
                print('2. Section must be number from 1')
                print('3. Write base diameter of section - d0 (cm), write top diameter of section = dl (cm) '
                      'and lenght of section = h (m)')
                print('4. If you want to end of measurement write 0 in section')
                print(dendro_formulas.sekVSmal(sek='Run', d0=0, dl=0, h=0))
                module = 'B'
            elif mode == 'X':
                module = 'Run'
        elif module == 'X':
            break


print(main)
