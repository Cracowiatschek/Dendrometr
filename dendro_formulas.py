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


class sekVHub:
    sek = 0
    def __init__(self, sek, d1_2, h):
        Vcdrz = 0
        sek = int(input('Write number of section: '))
        while sek >= 0:
            if sek > 0:
                d1_2 = int(input('Write diameter in half of section = d1/2 (cm): '))
                h = int(input('Write lenght of section = h (m): '))
                V = ((cmath.pi * d1_2 ** 2) / 40000) * h
                Vcdrz += V
                print(Vcdrz)
                sek = int(input('Write number of section: '))
            elif sek == 0:
                print('V = ' + str(Vcdrz) + 'm3')
                break
            else:
                print('Error')
                break


class sekVSmal:
    def __init__(self, sek, d0, dl, h):
        Vcdrz = 0
        sek = int(input('Write number of section: '))
        while sek >= 0:
            if sek > 0:
                d0 = int(input('Write base diameter of section = d0 (cm): '))
                dl = int(input('Write top diameter od section = dl (cm): '))
                h = int(input('Write lenght of section = h (m): '))
                V = (((cmath.pi * d0 ** 2) / 40000) + ((cmath.pi * dl ** 2) / 40000)) / 2 * h
                Vcdrz += V
                print(Vcdrz)
                sek = int(input('Write number of section: '))
            elif sek == 0:
                print('V = ' + str(Vcdrz) + 'm3')
                break
            else:
                print('Error')
                break