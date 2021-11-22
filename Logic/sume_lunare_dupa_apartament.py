from Domain.cheltuiala2 import get_data, creeaza_cheltuiala, get_id, get_nr_apartament, get_suma, get_tip
from Logic.CRUD import adauga_cheltuiala


def sume_lunare_dupa_apartament(lista):
    list = []
    lista_luni = []
    lista_nr_apartamente = []
    lista_temporara_1 = []

    for cheltuiala in lista:
        lista_nr_apartamente.append(get_nr_apartament(cheltuiala))
    for apartament in lista_nr_apartamente:
        if apartament not in lista_nr_apartamente:
            lista_temporara_1.append(apartament)
    lista_nr_apartamente = lista_temporara_1


    for cheltuiala in lista:
        l = get_data(cheltuiala).split(".")
        luna = l[1]
        list = adauga_cheltuiala(get_id(cheltuiala), get_nr_apartament(cheltuiala), get_suma(cheltuiala), luna, get_tip(cheltuiala), list)


    for cheltuiala in list:
        lista_luni.append(get_data(cheltuiala))
    lista_temporara2 = []
    for luna in lista_luni:
        if luna not in lista_temporara2:
            lista_temporara2.append(luna)
    lista_luni = lista_temporara2

    for apartament in lista_nr_apartamente:
        print("Pentru apartamentul " + str(apartament) + ":")
        for luna in lista_luni:
            a = 0
            for cheltuiala in list:
                if get_nr_apartament(cheltuiala) == apartament:
                    if get_data(cheltuiala) == luna:
                        a = a + get_suma(cheltuiala)
            print("Suma pentru luna " + str(luna) +" este " + str(a))






