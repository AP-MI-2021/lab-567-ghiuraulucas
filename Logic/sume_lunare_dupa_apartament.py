from Domain.cheltuiala2 import get_data, get_nr_apartament, get_suma



def sume_lunare_dupa_apartament(lista):
    lista_cheltuieli = []
    lista_date = []
    lista_luni = []
    lista_nr_apartamente = []
    lista_temporara_1 = []
    lista_temporara_2 = []
    lista_temporara_3 = []
    lista_ani = []

    for cheltuiala in lista:
        lista_nr_apartamente.append(get_nr_apartament(cheltuiala))
    for apartament in lista_nr_apartamente:
        if apartament not in lista_temporara_1:
            lista_temporara_1.append(apartament)
    lista_nr_apartamente = lista_temporara_1

    for cheltuiala in lista:
        lista_date.append(get_data(cheltuiala))
    for data in lista_date:
        a = data.split(".")
        lista_luni.append(a[1])
    for luna in lista_luni:
        if luna not in lista_temporara_2:
            lista_temporara_2.append(luna)
    lista_luni = lista_temporara_2

    for cheltuiala in lista:
        lista_date.append(get_data(cheltuiala))
    for data in lista_date:
        a = data.split(".")
        lista_ani.append(a[2])
    for an in lista_ani:
        if an not in lista_temporara_3:
            lista_temporara_3.append(an)
    lista_ani = lista_temporara_3

    for apartament in lista_nr_apartamente:
        print("Pentru apartamentul " + str(apartament) +":")
        for an in lista_ani:
            print("Pentru anul " + an + ":")
            lista_cheltuieli = []
            for cheltuiala in lista:
                a = get_data(cheltuiala)
                b = a.split(".")
                if get_nr_apartament(cheltuiala) == apartament and b[2] == an:
                    lista_cheltuieli.append(cheltuiala)
            for luna in lista_luni:
                suma = 0
                for cheltuiala in lista_cheltuieli:
                    a = get_data(cheltuiala)
                    b = a.split(".")
                    if b[1] == luna:
                        suma = suma + get_suma(cheltuiala)
                print("Pentru luna " + luna + " suma este de: " + str(suma))












