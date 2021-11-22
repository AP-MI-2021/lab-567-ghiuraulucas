from Domain.cheltuiala2 import get_data, creeaza_cheltuiala, get_id, get_suma, get_nr_apartament, get_tip


def adunarea_unei_valori_la_toate_cheltuielile_data(valoare, data, lista):
    '''
    Aduna o valoare data la toate cheltuielile dintr-o data citita.
    :param valoare: float
    :param data: string
    :param lista: lista de cheltuieli
    :return: lista cu modificarile cerute
    '''
    if valoare < 0:
        raise ValueError("Nu puteti adauga o suma negativa.")
    l = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            suma_noua = get_suma(cheltuiala) + valoare
            cheltuiala_noua = creeaza_cheltuiala(get_id(cheltuiala), get_nr_apartament(cheltuiala), suma_noua, data, get_tip(cheltuiala))
            l.append(cheltuiala_noua)
        else:
            l.append(cheltuiala)

    return l