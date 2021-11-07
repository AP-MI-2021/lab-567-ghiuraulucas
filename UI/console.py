from Domain.cheltuiala2 import to_string, get_nr_apartament, get_data
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala


def print_menu():
    print("1. Adaugare cheltuiala.")
    print("2. Stergere cheltuiala.")
    print("3. Modificare cheltuiala.")
    print("a. Afisare cheltuieli.")
    print("d. Stergerea tuturor cheltuielilor pentru un apartament dat.")
    print("x. Iesire.")


def ui_adauga_cheltuiala(lista):
# Nu uita sa convertesti la tipul de date corespunzator.

    nr_apartament = int(input("Introduceti numarul apartamentului: "))
    suma = float(input("Introduceti suma cheltuielii: "))
    data = input("Introduceti data la care s-a efectuat cheltuiala (format DD.MM.YYYY): ")
    tip = input("Introduceti tipul cheltuielii (intretinere, canal, alte cheltuieli): ")

    if tip != "intretinere":
        if tip != "canal":
            if tip != "alte cheltuieli":
                tip = input("Ati introdus tipul in mod gresit. Reintroduceti tipul. ")

    return adauga_cheltuiala(nr_apartament, suma, data, tip, lista)


def ui_stergere_cheltuiala(lista):
    nr_apartament = int(input("Introduceti numarul apartamentului cheltuielii pe care doriti sa o stergeti: "))
    data = input("Introduceti data la care s-a efectuat cheltuiala (format DD.MM.YYYY): ")

    return sterge_cheltuiala(nr_apartament, data, lista)


def ui_modificare_cheltuiala(lista):
    print("Se va efectua o modificare la cheltuiala efectuata la apartamentul introdus de dvs, in data introdusa de dvs")
    nr_apartament = int(input("Introduceti numarul apartamentului cheltuielii de modificat: "))
    data = input("Introduceti data la care s-a efectuat cheltuiala (format DD.MM.YYYY): ")
    suma = float(input("Introduceti noua suma a cheltuielii: "))
    tip = input("Introduceti noul tip al cheltuielii (intretinere, canal, alte cheltuieli): ")

    return modifica_cheltuiala(nr_apartament, suma, data, tip, lista)


def show_all(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))

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
        elif optiune == "a":
            show_all(lista)
        elif optiune == "d":
            lista = delete_all_by_nr_apartament(lista)
        elif optiune == "x":
            break
        else:
            print("Opriune gresita. Va rugam reincercati. ")
