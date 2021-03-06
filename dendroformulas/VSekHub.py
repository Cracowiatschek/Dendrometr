import dendroformulas.VHub


class VSekHub:
    def __init__(self):
        sek = str(input('Do you want to write first section? [Y/N]: '))
        self.Vcdrz = 0
        self.VcdrzList = []  # list of
        while sek == 'Y' or sek == 'N':
            dlist = []
            hlist = []
            if sek == 'Y':
                d = float(input('Write diameter in half of section = d1/2 (cm): '))
                ht = float(input('Write length of section = h (m): '))
                dlist.append(d)
                hlist.append(ht)
                self.V = dendroformulas.VHub.v_hub_use(d1_2=d, h=ht)
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
