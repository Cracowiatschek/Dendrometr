import dendroformulas.g


class VHub:
    def __init__(self):  # d1_2 - tree diamater in 1/2 h, k - bark thickness, h - height
        d1_2 = float(input('Write diameter of tree: '))
        k = float(input('Write thickness of bark: '))
        h = float(input('Write height of tree: '))
        d = d1_2 - k
        if d >= 0 and h > 0:
            g = dendroformulas.g.G(d)
            v = g * h
            print('V = ' + str(round(v, 4)) + 'm3')
        else:
            print('Error: correct d1_2')


def VHubUse(d1_2, h):
    g = dendroformulas.g.G(d1_2)
    v = g * h
    return v
