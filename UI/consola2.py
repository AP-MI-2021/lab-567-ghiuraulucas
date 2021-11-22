from Domain.cheltuiala2 import to_string, get_nr_apartament
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.adunare_valoare_data_citita import adunarea_unei_valori_la_toate_cheltuielile_data
from Logic.ordonare_descrescatoare_dupa_suma import ordonare_descrescatoare_dupa_suma
from UI.console import ui_afiseaza_suma_max_dupa_tip


def show_all(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))

def print_meniu():
    print("h. Help.")
    print("x. Iesire.")

def help_menu():
    print("Pentru adaugare cheltuiala: 'add', id, nr_apartament, suma, data, tip")
    print("Pentru stergere cheltuiala: 'delete', id")
    print("Pentru modifica cheltuiala: 'modify', id, nr_apartament, suma, data, tip")
    print("Pentru adaugare valoare la sumele unei dati: 'add_value', suma, data")
    print("Pentru afisarea celei mai mari sume dupa tipul de cheltuiala: 'max'")
    print("Pentru ordonare descrescatoare dupa suma: 'ordonare'")
    print("Pentru stergerea tuturor cheltuielilor unui apartament: 'delete_all_nr', nr_apartament")
    print("Pentru afisare cheltuieli: a")

def delete_all_by_nr_apartament(nr_apartament,lista):
    l=[]

    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            pass
        else:
            l.append(cheltuiala)
    return l

def menu2():
    lista = []
    while True:
        print_meniu()
        optiune = input("""
        Introduceti seria de actiuni dorite separate prin ';' cu argumentele separate prin virgula.
        Introduceti x pentru iesire. 
        Introduceti 'h' pentru ajutor """)
        if optiune == 'h':
            help_menu()
        if optiune == 'x':
            break
        else:
            comenzi = optiune.split(';')
            for c in comenzi:
                actiuni = c.split(',')
                if actiuni[0] == 'add':

                    lista = adauga_cheltuiala(int(actiuni[1]), int(actiuni[2]), float(actiuni[3]), actiuni[4], actiuni[5], lista)

                elif actiuni[0] == 'delete':

                    lista = sterge_cheltuiala((int(actiuni[1])), lista)

                elif actiuni[0] == 'modify':

                    lista = modifica_cheltuiala(int(actiuni[1]), int(actiuni[2]), float(actiuni[3]), actiuni[4], actiuni[5], lista)

                elif actiuni[0] == 'add_value':

                    lista = adunarea_unei_valori_la_toate_cheltuielile_data(float(actiuni[1]), actiuni[2], lista)


                elif actiuni[0] == 'max':

                    ui_afiseaza_suma_max_dupa_tip(lista)

                elif actiuni[0] == 'ordonare':

                    lista = ordonare_descrescatoare_dupa_suma(lista)

                elif actiuni[0] == "a":

                    show_all(lista)

                elif actiuni[0] == "delete_all_nr":

                    lista = delete_all_by_nr_apartament(int(actiuni[1]), lista)

                else:
                    print("Optiune gresita.")