import dendroformulas.g


class HL:
    def __init__(self):
        local_g = []
        local_gh = []
        tree_id = str(input('Do you want to add first tree? [Y/N]: '))
        while tree_id == 'Y' or tree_id == 'N':
            if tree_id == 'Y':
                k = float(input('Write bark thickness (cm): '))
                d = float(input('Write diameter (with bark) on 1,3 m height of tree (cm): ')) - k
                h = float(input('Write height of tree (m): '))
                g = round(dendroformulas.g.G(d), 4)
                local_g.append(g)
                local_gh.append(round((g * h), 4))
                tree_id = str(input('Do you want to add next tree? [Y/N]: '))
            elif tree_id == 'N':
                Lorey = round((sum(local_gh) / sum(local_g)), 2)
                id = 1
                print('List of g:')
                for v in local_g:
                    print(str(id) + '. ' + str(v) + ' m2')
                    id += 1
                id = 1
                print('List of gh:')
                for v in local_gh:
                    print(str(id) + '. ' + str(v) + ' m3')
                    id += 1
                print('HL = ' + str(Lorey) + ' m')
                break
            else:
                print('Error')
                break
