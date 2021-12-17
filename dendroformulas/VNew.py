import dendroformulas.g


class VHoss:
    def __init__(self):  # d1_3 - tree diameter in 1/3 h, dl - tree diameter in top h, h - height
        d0 = float(input('Write diameter in base height of tree: '))
        d1_2 = float(input('Write diameter in 1/2 height of tree: '))
        dl = float(input('Write diameter in top height of tree: '))
        h = float(input('Write height of tree: '))
        if d0 > 0 and h > 0:
            g0 = dendroformulas.g.G(d0)
            g1_2 = dendroformulas.g.G(d1_2)
            gl = dendroformulas.g.G(dl)
            v = (g0 + 4 * g1_2 + gl)/6 * h
            print('V = ' + str(round(v, 4)) + 'm3')
        else:
            print('Error: correct d0')
