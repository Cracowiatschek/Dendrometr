print('Dendrometr 1.0.3')
print('')
print('Hi User!')
print('')


class Main:
    module = 'Run'
    while module == 'A' or module == 'B' or module == 'X' or 'Run':
        if module == 'Run':
            print('Modules:')
            print('A. Module tree volume calculating - simple mod.')
            print('B. Module tree volume calculating - section mod.')
            print('C. Module global diameter calculating - Dg')
            print('D. Module Height of Lorey - HL')
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
                import dendroformulas.VHub
                print(dendroformulas.VHub.VHub())
                module = 'A'
            elif mode == 'B':
                import dendroformulas.VSmal
                print(dendroformulas.VSmal.VSmal())
                module = 'A'
            elif mode == 'C':
                import dendroformulas.VHoss
                print(dendroformulas.VHoss.VHoss())
                module = 'A'
            elif mode == 'D':
                import dendroformulas.VNew
                print(dendroformulas.VNew.VNew)
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
                print('3. Write diameter in half of section - d1/2, bark thickness (cm) and '
                      'lenght of section - h')
                print('4. If you want to end of measurement, write 0 in section')
                import dendroformulas.VSekHub
                print(dendroformulas.VSekHub.VSekHub())
                module = 'B'
            elif mode == 'B':
                print('Instruction')
                print('1. Write number of section')
                print('2. Section must be number from 1')
                print('3. Write base diameter of section - d0 (cm), write top diameter of section = dl (cm), '
                      'bark thickness (cm) and lenght of section = h (m)')
                print('4. If you want to end of measurement, write 0 in section')
                import dendroformulas.VSekSmal
                print(dendroformulas.VSekSmal.VSekSmal)
                module = 'B'
            elif mode == 'X':
                module = 'Run'
        elif module == 'C':
            print('Module global diameter calculating - Dg')
            print('Instruction: ')
            print('1. Write tree_id')
            print('2. tree_id must be number from 1')
            print('3. Write bark thicknes (cm)')
            print('4. Write tree diameter on 1.3 m (cm)')
            print('5. Write height of tree')
            print('6. If you want to end measurement, write 0')
            print('A. Start')
            print('X. Return')
            run = input('Write A or X: ')
            if run == 'A':
                import dendroformulas.Dg
                print(dendroformulas.Dg.Dg())
                module = 'C'
            elif run == 'X':
                module = 'Run'
            else:
                print('Error')
                module = 'C'
        elif module == 'D':
            print('Module Height of Lorey - HL')
            print('Instruction:')
            print('1. Write tree_id')
            print('2. tree_id must be number from 1')
            print('3. Write bark thickness (cm)')
            print('4. Write tree diameter on 1.3 m height of tree (cm)')
            print('5. Write height of tree (m)')
            print('6. If you want to end measurement, write 0')
            print('A. Start')
            print('X. Return')
            run = (input('Write A or X: '))
            if run == 'A':
                import dendroformulas.HL
                print(dendroformulas.HL.HL())
                module = 'D'
            elif run == 'X':
                module = 'Run'
            else:
                print('Error')
                module = 'D'
        elif module == 'X':
            break


print(Main)
