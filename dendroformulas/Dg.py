import dendroformulas.g


class Dg:
    def __init__(self):
        local_g = []
        tree_id = str(input('Do you want to add first tree? : '))
        while tree_id == 'Y' or tree_id == 'N':
            if tree_id == 'Y':
                k = float(input('Write bark thickness (cm): '))
                d = float(input('Write diameter (with bark) on 1,3 m height of tree (cm): ')) - k
                g = dendroformulas.g.G(d)
                local_g.append(g)
                print(local_g)
                tree_id = int(input('Do you want to add next tree? : '))
            elif tree_id == 'N':
                g = round((sum(local_g) / len(local_g)), 4)
                id = 1
                for v in local_g:
                    print(str(id) + '. ' + str(v) + ' m2')
                    id += 1
                print('Dg = ' + str(g) + ' m2')
                break
            else:
                print('Error')
                break
