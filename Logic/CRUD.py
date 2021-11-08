from Domain.cheltuiala2 import creeaza_cheltuiala, get_nr_apartament, get_suma, get_data, get_tip


def adauga_cheltuiala(nr_apartament, suma, data, tip, lista):
    '''
    Adauga o cheltuiala intr-o lista
    :param nr_apartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: o lista continand atat elementele vechi cat si noua cheltuiala
    '''

    cheltuiala = creeaza_cheltuiala(nr_apartament, suma, data, tip)
    return lista + [cheltuiala]

def get_by_nr_apartament_si_data(nr_apartament, data, lista):
    '''
    Returneaza o cheltuiala din lista cu numarul apartamentului dat
    :param nr_apartament: int
    :param data: string
    :param lista: lista de cheltuieli
    :return: cheltuiala cu numarul de apartament dat din lista, sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala) == nr_apartament and get_data(cheltuiala) == data:
            return cheltuiala
    return None

# AM PRESUPUS CA NU SE POT EFECTUA 2 CHELTUIELI LA UN APARTAMENT IN ACEEASI ZI (altfel, ca sa obtin o cheltuiala trebuia sa bag
# toate specificatiile: nr apartament, suma, data, tip, deoarece ar fi posibil orice.
# Ce mai puteam sa fac aici e sa iau dupa un singur criteriu (get_by_nr_apartament) si sa returnez O LISTA de cheltuieli efectuate
# la acelasi apartament; dar vreau sa pot lua o singura cheltuiala dupa nr apartamentului si data.

def sterge_cheltuiala(nr_apartament, data, lista):
    l=[]
    '''
    Sterge o cheltuiala dintr-o lista, dupa nr apartamentului si data
    :param nr_apartament: int
    :param data: string
    :param lista: lista de dictionare
    :return:
    '''

    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala) == nr_apartament and get_data(cheltuiala) == data:
            pass
        else:
            l.append(cheltuiala)
    return l


def modifica_cheltuiala(nr_apartament, suma, data, tip, lista):
    # Am bagat aici toti acesti parametri pentru ca ei sunt parametrii noi si cheltuielii. Evident, nr_apartament si data raman la fel.
    '''
    Modifica o lista dupa nr_apartament si data
    :param nr_apartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: Lista cu cheltuiala ceruta modificata
    '''
    lista_noua = []
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala) == nr_apartament and get_data(cheltuiala) == data:
            cheltuiala_noua = creeaza_cheltuiala(nr_apartament, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua