import cmath


class VHub:
    def __init__(self, d1_2, h):
        if d1_2 >= 0 and h > 0:
            print('V = ' + str(((cmath.pi * d1_2 ** 2) / 40000) * h) + ' m3')
        else:
            print('Error: korekta d1_2')


# print(VHub(d1_2=int(input('Wpisz d1/2 (cm): ')), h=int(input('Wpisz h (m): '))))
class VSmal:
    def __init__(self, d0, dl, h):
        if d0 >= dl and d0 >= 0 and h > 0:
            print('V = ' + str(
                (((cmath.pi * d0 ** 2) / 40000) +
                 ((cmath.pi * dl ** 2) / 40000)) / 2 * h) + ' m3')
        else:
            print('Error: korekta d0/dl')


# print(VSmal(d0=int(input('Wpisz d0 (cm): ')),
#             dl=int(input('Wpisz dl (cm): ')),
#             h=int(input('Wpisz h (m): '))))


class VHoss:
    def __init__(self, d1_3, dl, h):
        if d1_3 >= dl and d1_3 > 0 and h > 0:
            print('V = ' + str(
                ((3 * (cmath.pi * d1_3 ** 2) / 40000) +
                 ((cmath.pi * dl ** 2) / 40000)) / 4 * h) + ' m3')
        else:
            print('Error: korekcja d1_3/dl')


# print(VHoss(d1_3=int(input('Wpisz d1_3 (cm): ')),
#             dl=int(input('Wpisz dl (cm): ')),
#             h=int(input('Wpisz h (m): '))))

class VNew:
    def __init__(self, d0, d1_2, dl, h):
        if d0 >= d1_2 >= dl and d0 > 0 and h > 0:
            print('V = ' + str(
                (((cmath.pi * d0 ** 2) / 40000) +
                 (4 * (cmath.pi * d1_2 ** 2) / 40000) +
                 ((cmath.pi * dl ** 2) / 40000)) / 6 * h) + ' m3')
        else:
            print('Error: korekcja d0/d1_3/dl')


# print(VNew(d0=int(input('Wpisz 0 (cm): ')),
#            d1_2=int(input('Wpisz d1_2 (cm): ')),
#            dl=int(input('Wpisz dl (cm): ')),
#            h=int(input('Wpisz h (m): '))))


class Vsek:
    choose = 0

    def __init__(self, choose):
        print('Moduł obliczania miąższości - met. sekcyjne')
        print('A. wzór Hubera')
        print('B. wzór Smaliana')
        choose = input('Wybierz model pomiaru sekcyjnego: ')
        if choose == 'A':
            print('Instrukcja')
            print('1. Wpisz numer sekcji')
            print('2. Sekcje należy numerować od 1 wzwyż')
            print('3. Uzupełnij średnicę - d1/2 i  długość - h sekcji')
            print('4. Jeśli chcesz zakończyć pomiar w numerze sekcji wpisz 0')
            Vcdrz = 0
            sek = int(input('Wpisz numer sekcji: '))
            while sek >= 0:
                if sek > 0:
                    d1_2 = int(input('Podaj d1_2 sekcji: '))
                    h = int(input('Podaj h sekcji: '))
                    V = ((cmath.pi * d1_2 ** 2) / 40000) * h
                    Vcdrz += V
                    print(Vcdrz)
                    sek = int(input('Wpisz numer sekcji: '))
                elif sek == 0:
                    print('V = ' + str(Vcdrz) + 'm3')
                    break
                else:
                    print('Error')
                    break
        elif choose == 'B':
            print('Instrukcja')
            print('1. Wpisz numer sekcji')
            print('2. Sekcje należy numerować od 1 wzwyż')
            print('3. Uzupełnij średnicę podstawy dolnej - d0, ''średnicę podstawy górnej - dl i  długość - h sekcji')
            print('4. Jeśli chcesz zakończyć pomiar w numerze sekcji wpisz 0')
            Vcdrz = 0
            sek = int(input('Wpisz numer sekcji: '))
            while sek >= 0:
                if sek > 0:
                    d0 = int(input('Podaj d0 sekcji: '))
                    dl = int(input('Podaj dl sekcji: '))
                    h = int(input('Podaj h sekcji: '))
                    V = (((cmath.pi * d0 ** 2) / 40000) + ((cmath.pi * dl ** 2) / 40000)) / 2 * h
                    Vcdrz += V
                    print(Vcdrz)
                    sek = int(input('Wpisz numer sekcji: '))
                elif sek == 0:
                    print('V = ' + str(Vcdrz) + 'm3')
                    break
                else:
                    print('Error')
                    break
            else:
                print('Error')
                pass


class sekVHub:
    sek = 0
    def __init__(self, sek):
        print('Instrukcja')
        print('1. Wpisz numer sekcji')
        print('2. Sekcje należy numerować od 1 wzwyż')
        print('3. Uzupełnij średnicę - d1/2 i  długość - h sekcji')
        print('4. Jeśli chcesz zakończyć pomiar w numerze sekcji wpisz 0')
        Vcdrz = 0
        sek = int(input('Wpisz numer sekcji: '))
        while sek >= 0:
            if sek > 0:
                d1_2 = int(input('Podaj d1_2 sekcji: '))
                h = int(input('Podaj h sekcji: '))
                V = ((cmath.pi * d1_2 ** 2) / 40000) * h
                Vcdrz += V
                print(Vcdrz)
                sek = int(input('Wpisz numer sekcji: '))
            elif sek == 0:
                print('V = ' + str(Vcdrz) + 'm3')
                break
            else:
                print('Error')
                break


class sekVSmal:
    def __init__(self, sek):
        Vcdrz = 0
        sek = int(input('Wpisz numer sekcji: '))
        while sek >= 0:
            if sek > 0:
                d0 = int(input('Podaj d0 sekcji: '))
                dl = int(input('Podaj dl sekcji: '))
                h = int(input('Podaj h sekcji: '))
                V = (((cmath.pi * d0 ** 2) / 40000) + ((cmath.pi * dl ** 2) / 40000)) / 2 * h
                Vcdrz += V
                print(Vcdrz)
                sek = int(input('Wpisz numer sekcji: '))
            elif sek == 0:
                print('V = ' + str(Vcdrz) + 'm3')
                break
            else:
                print('Error')
                break