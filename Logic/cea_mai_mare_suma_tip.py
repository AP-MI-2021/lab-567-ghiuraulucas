from Domain.cheltuiala2 import get_suma, get_tip


def cea_mai_mare_suma_dupa_intretinere(lista):
    a = 0

    for cheltuiala in lista:
        if get_tip(cheltuiala) == "intretinere":
            if get_suma(cheltuiala) > a:
                a = get_suma(cheltuiala)
    return a


def cea_mai_mare_suma_dupa_canal(lista):
    b = 0

    for cheltuiala in lista:
        if get_tip(cheltuiala) == "canal":
            if get_suma(cheltuiala) > b:
                b = get_suma(cheltuiala)
    return b

def cea_mai_mare_suma_dupa_alte_cheltuieli(lista):
    c = 0

    for cheltuiala in lista:
        if get_tip(cheltuiala) == "alte cheltuieli":
            if get_suma(cheltuiala) > c:
                c = get_suma(cheltuiala)
    return c