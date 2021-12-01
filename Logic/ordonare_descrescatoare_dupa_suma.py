from Domain.cheltuiala2 import get_suma


def ordonare_descrescatoare_dupa_suma(lista, undo_list, redo_list):
    l = []
    i = 0
    undo_list.append(lista)
    redo_list.clear()
    lista_noua = []
    for cheltuiala in lista:
        l.append(float(get_suma(cheltuiala)))
        i = i+1

    l.sort(reverse=True)

    for x in range(i):
        lista_noua.append(0)

    for cheltuiala in lista:
        for a in range(i):
            if float(get_suma(cheltuiala)) == l[a]:
                lista_noua[a] = cheltuiala

    return lista_noua
