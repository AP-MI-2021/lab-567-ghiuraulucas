
def creeaza_cheltuiala(nr_apartament, suma, data, tip):
    '''
    Creeaza un dictionar ce reprezinta o cheltuiala
    :param nr_apartament: int
    :param suma: float
    :param data: string
    :param tip: string (unul din cele 3: intretinere, canal, alte cheltuieli)
    :return: un dictionar ce contine o cheltuiala
    '''

    return{"nr_apartament": nr_apartament, "suma": suma, "data": data, "tip": tip }

# Acesta este un dictionar cu cheile date intre ghilimele. Arata asa:  {13, 324.99, 28.09.2020, intretinere}
# De fiecare data cand apelez aceasta functie dand anumiti parametri, mi se creeaza un aftfel de dictionar.

def get_nr_apartament(cheltuiala):
    '''
    Returneaza numarul apartamentului unei cheltuieli
    :param cheltuiala: DICTIONAR ce contine o cheltuiala
    :return: numarul apartamentului unei cheltuieli
    '''
    return cheltuiala["nr_apartament"]

def get_suma(cheltuiala):
    return cheltuiala["suma"]

def get_data(cheltuiala):
    return cheltuiala["data"]

def get_tip(cheltuiala):
    return cheltuiala["tip"]

def to_string(cheltuiala):
    return "nr_apartament: {}, suma: {}, data: {}, tip: {}".format(
        get_nr_apartament(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala)
    )