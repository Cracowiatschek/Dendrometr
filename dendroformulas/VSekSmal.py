import dendroformulas.VSmal


class VSekSmal:
    def __init__(self):
        sek = str(input('Do you want to write first section? [Y/N]: '))
        self.Vcdrz = 0
        self.VcdrzList = []  # list of
        while sek == 'Y' or sek == 'N':
            d0list = []
            dllist = []
            hlist = []
            if sek == 'Y':
                d0v = float(input('Write diameter in base of section = d0 (cm): '))
                dlv = float(input('Write diameter in top of section = dl (cm): '))
                ht = float(input('Write length of section = h (m): '))
                d0list.append(d0v)
                dllist.append(dlv)
                hlist.append(ht)
                self.V = dendroformulas.VSmal.v_smal_use(d0=d0v, dl=dlv, h=ht)
                self.Vcdrz += self.V
                self.VcdrzList.append(round(self.V, 4))
                print(self.VcdrzList)
                sek = str(input('Do you want to write next section? [Y/N]: '))
            elif sek == 'N':
                id = 1
                for v in self.VcdrzList:
                    print(str(id) + '. ' + str(v) + ' m3')
                    id += 1
                result = round(self.Vcdrz, 4)
                print('V = ' + str(result) + 'm3')
                break
            else:
                print('Error')
                break
