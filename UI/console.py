from Domain.cheltuiala2 import to_string, get_nr_apartament, get_data, get_id
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.adunare_valoare_data_citita import adunarea_unei_valori_la_toate_cheltuielile_data
from Logic.cea_mai_mare_suma_tip import cea_mai_mare_suma_dupa_intretinere, cea_mai_mare_suma_dupa_canal, \
    cea_mai_mare_suma_dupa_alte_cheltuieli
from Logic.ordonare_descrescatoare_dupa_suma import ordonare_descrescatoare_dupa_suma


def print_menu():
    print("1. Adaugare cheltuiala.")
    print("2. Stergere cheltuiala.")
    print("3. Modificare cheltuiala.")
    print("4. Adaugarea unei valori la sumele tuturor cheltuielilor dintr-o anumita data.")
    print("5. Afiseaza cele mai mare suma pentru fiecare tip de cheltuiala")
    print("6. Ordonarea cheltuielilor in ordine descrescatoare dupa suma")
    print("a. Afisare cheltuieli.")
    print("d. Stergerea tuturor cheltuielilor pentru un apartament dat.")
    print("x. Iesire.")


def ui_adauga_cheltuiala(lista):
# Nu uita sa convertesti la tipul de date corespunzator.

    try:
        id = int(input("Introduceti id-ul cheltuielii: "))
        nr_apartament = int(input("Introduceti numarul apartamentului: "))
        suma = float(input("Introduceti suma cheltuielii: "))
        data = input("Introduceti data la care s-a efectuat cheltuiala (format DD.MM.YYYY): ")
        tip = input("Introduceti tipul cheltuielii (intretinere, canal, alte cheltuieli): ")

        if tip != "intretinere":
            if tip != "canal":
                if tip != "alte cheltuieli":
                    tip = input("Ati introdus tipul in mod gresit. Reintroduceti tipul. ")

        return adauga_cheltuiala(id, nr_apartament, suma, data, tip, lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def ui_stergere_cheltuiala(lista):
    try:
        id = int(input("Va rugam sa introduceti id-ul cheltuielii pe care doriti sa o stergeti: "))
        return sterge_cheltuiala(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modificare_cheltuiala(lista):
    print("Se va efectua o modificare la cheltuiala cu id-l dat de dumneavoastra: ")
    id = int(input("Introduceti id-ul cheltuielii pe care doriti sa o modificati: "))
    nr_apartament = int(input("Introduceti noul numar de apartament al cheltuielii de modificat: "))
    data = input("Introduceti noua data la care s-a efectuat cheltuiala (format DD.MM.YYYY): ")
    suma = float(input("Introduceti noua suma a cheltuielii: "))
    tip = input("Introduceti noul tip al cheltuielii (intretinere, canal, alte cheltuieli): ")

    return modifica_cheltuiala(id, nr_apartament, suma, data, tip, lista)


def ui_adauga_suma(lista):
    try:
        data = input("Va rugam sa introduceti data: ")
        valoare = float(input("Va rugam sa introduceti suma pe care vrei sa o adaugati sumelor cheltuielilor din data introdusa: "))

        return adunarea_unei_valori_la_toate_cheltuielile_data(valoare, data, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_afiseaza_suma_max_dupa_tip(lista):
    print("Cea mai mare suma pentru tipul intretinere este: " + str(cea_mai_mare_suma_dupa_intretinere(lista)))
    print("Cea mai mare suma pentru tipul canal este: " + str(cea_mai_mare_suma_dupa_canal(lista)))
    print("Cea mai mare suma pentru tipul alte cheltuieli este: " + str(cea_mai_mare_suma_dupa_alte_cheltuieli(lista)))


def show_all(lista):
    try:
        for cheltuiala in lista:
            print(to_string(cheltuiala))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def delete_all_by_nr_apartament(lista):
    l=[]
    nr_apartament = int(input("Introduceti numarul aparamentului ale carui cheltuieli doriti sa le stergeti: "))

    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            pass
        else:
            l.append(cheltuiala)
    return l


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = ui_adauga_cheltuiala(lista)
        elif optiune == "2":
            lista = ui_stergere_cheltuiala(lista)
        elif optiune == "3":
            lista = ui_modificare_cheltuiala(lista)
        elif optiune == "4":
            lista = ui_adauga_suma(lista)
        elif optiune == "5":
            ui_afiseaza_suma_max_dupa_tip(lista)
        elif optiune == "6":
            lista = ordonare_descrescatoare_dupa_suma(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "d":
            lista = delete_all_by_nr_apartament(lista)
        elif optiune == "x":
            break
        else:
            print("Opriune gresita. Va rugam reincercati. ")
