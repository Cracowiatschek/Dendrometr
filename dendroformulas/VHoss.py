import dendroformulas.g


class VHoss:
    def __init__(self):  # d1_3 - tree diameter in 1/3 h, dl - tree diameter in top h, h - height
        d1_3 = float(input('Write diameter in 1/3 height of tree: '))
        dl = float(input('Write diameter in top height of tree: '))
        h = float(input('Write height of tree: '))
        while d1_3 >= 0:
            if d1_3 >= 0 and h > 0:
                g1_3 = dendroformulas.g.G(d1_3)
                gl = dendroformulas.g.G(dl)
                v = (3 * g1_3 + gl) / 4 * h
                print('V = ' + str(round(v, 4)) + 'm3')
                break
            else:
                print('Error: correct d1/3')
                break
