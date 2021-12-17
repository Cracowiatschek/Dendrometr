import dendroformulas.g


class VHub():
    def __init__(self):  # d1_2 - tree diamater in 1/2 h, k - bark thickness, h - height
        self.d1_2 = float(input('Write diameter of tree: '))
        self.k = float(input('Write thickness of bark: '))
        self.h = float(input('Write height of tree: '))
        d = self.d1_2 - self.k
        while d >= 0:
            if d >= 0 and self.h > 0:
                g = dendroformulas.g.G(d)
                v = g * self.h
                print('V = ' + str(round(v, 4)) + 'm3')
                break
            else:
                print('Error: correct d1_2')
                break


def v_hub_use(d1_2, h):
    g = dendroformulas.g.G(d1_2)
    v = g * h
    return v
