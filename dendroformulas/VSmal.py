import dendroformulas.g


class VSmal:
    def __init__(self):  # d0 - tree diamater in base h, dl - tree diamater in top h, h - height
        d0 = float(input('Write diameter in base of tree: '))
        dl = float(input('Write diameter in top of tree: '))
        h = float(input('Write height of tree: '))
        d = (d0 + dl)/2
        if d >= 0 and h > 0:
            g = dendroformulas.g.G(d)
            v = g * h
            print('V = ' + str(round(v, 4)) + 'm3')
        else:
            print('Error: correct d0/dl')
