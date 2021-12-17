import cmath






# print(VSmal(d0=int(input('Wpisz d0 (cm): ')),
#             dl=int(input('Wpisz dl (cm): ')),
#             h=int(input('Wpisz h (m): '))))


class VHoss:
    def __init__(self, d1_3, k1_3, dl, kl, h):
        if d1_3 >= dl and d1_3 > 0 and h > 0:
            self.V = round((((3 * (cmath.pi * (d1_3 - k1_3) ** 2) / 40000) +
                             ((cmath.pi * (dl - kl) ** 2) / 40000)) / 4 * h), 4)
            print('V = ' + str(self.V) + ' m3')
        else:
            print('Error: correct d1_3/dl')


# print(VHoss(d1_3=int(input('Wpisz d1_3 (cm): ')),
#             dl=int(input('Wpisz dl (cm): ')),
#             h=int(input('Wpisz h (m): '))))

class VNew:
    def __init__(self, d0, k0, d1_2, k1_2, dl, kl, h):
        if d0 >= d1_2 >= dl and d0 > 0 and h > 0:
            self.V = round(((((cmath.pi * (d0 - k0) ** 2) / 40000) + (4 * (cmath.pi * (d1_2 - k1_2) ** 2) / 40000) +
                             ((cmath.pi * (dl - kl) ** 2) / 40000)) / 6 * h), 4)
            print('V = ' + str(self.V) + ' m3')
        else:
            print('Error: correct d0/d1_3/dl')


# print(VNew(d0=int(input('Wpisz 0 (cm): ')),
#            d1_2=int(input('Wpisz d1_2 (cm): ')),
#            dl=int(input('Wpisz dl (cm): ')),
#            h=int(input('Wpisz h (m): '))))


class sekVHub:
    def __init__(self, sek):
        self.Vcdrz = 0
        sek = int(input('Write number of section: '))
        while sek >= 0:
            d = []
            ht = []
            if sek > 0:
                d1_2 = int(input('Write diameter in half of section = d1/2 (cm): '))
                h = int(input('Write length of section = h (m): '))
                d.append(d1_2)
                ht.append(h)
                self.V = ((cmath.pi * d1_2 ** 2) / 40000) * h
                self.Vcdrz += self.V
                print(self.Vcdrz)
                sek = int(input('Write number of section: '))
            elif sek == 0:
                self.id = 0
#                while self.id < len(d) or self.id < len(ht):
#                    print(str(self.id+1) + str(d[self.id]) + ' cm; ' + str(ht[self.id]))
#                    self.id += 1
                self.Vcdrz = round(self.Vcdrz, 4)
                print('V = ' + str(self.Vcdrz) + 'm3')
                break
            else:
                print('Error')
                break


class sekVSmal:
    def __init__(self, sek):
        self.Vcdrz = 0
        sek = int(input('Write number of section: '))
        while sek >= 0:
            if sek > 0:
                d0 = int(input('Write base diameter of section = d0 (cm): '))
                dl = int(input('Write top diameter od section = dl (cm): '))
                h = int(input('Write length of section = h (m): '))
                self.V = (((cmath.pi * d0 ** 2) / 40000) + ((cmath.pi * dl ** 2) / 40000)) / 2 * h
                self.Vcdrz += self.V
                print(self.Vcdrz)
                sek = int(input('Write number of section: '))
            elif sek == 0:
                print('V = ' + str(round(self.Vcdrz, 4)) + 'm3')
                break
            else:
                print('Error')
                break


class Dg:
    def __init__(self, measurement):
        local_g = []
        while measurement == 'Y' or measurement == 'N':
            if measurement == 'Y':
                k = float(input('Write bark thickness (cm): '))
                d = float(input('Write diameter (with bark) on 1,3 m height of tree (cm): ')) - k
                g = (cmath.pi * d ** 2) / 40000
                local_g.append(g)
                print(local_g)
                measurement = input('Do you write next measurement? [Y / N]: ')
            elif measurement == 'N':
                g = round((sum(local_g) / len(local_g)), 4)
                print('Dg = ' + str(g) + ' m2')
                break
            else:
                print('Error')
                break


class HL:
    def __init__(self, measurement):
        local_g = []
        local_gh = []
        while measurement == 'Y' or measurement == 'N':
            if measurement == 'Y':
                k = float(input('Write bark thickness (cm): '))
                d = float(input('Write diameter (with bark) on 1,3 m height of tree (cm): ')) - k
                h = float(input('Write height of tree (m): '))
                g = (cmath.pi * d ** 2) / 40000
                local_g.append(g)
                local_gh.append(g * h)
                print('local_g = ' + str(local_g))
                print('local_gh = ' + str(local_gh))
                measurement = input('Do you write next measurement? [Y / N]: ')
            elif measurement == 'N':
                self.Lorey = round((sum(local_gh) / sum(local_g)), 4)
                print('HL = ' + str(self.Lorey) + ' m')
                break
            else:
                print('Error')
                break


# print(HL(tree_id=1))
