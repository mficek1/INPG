
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os  # moduł udostępniający funkcję isfile()

slownik = {}  # pusty słownik
sPlik = "slownik.txt"  # nazwa pliku zawierającego wyrazy i ich tłumaczenia
def otworz(plik):
    if os.path.isfile(sPlik):  # czy istnieje plik słownika?
        with open(sPlik, "r") as pliktxt:  # otwórz plik do odczytu
            for line in pliktxt:  # przeglądamy kolejne linie
                # rozbijamy linię na wyraz obcy i tłumaczenia
                t = line.split(":")
                wobcy = t[0]
                # usuwamy znaki nowych linii
                znaczenia = t[1].replace("\n", "")
                znaczenia = znaczenia.split(",")  # tworzymy listę znaczeń
                # dodajemy do słownika wyrazy obce i ich znaczenia
                slownik[wobcy] = znaczenia
<<<<<<< HEAD
    return len(slownik)  # zwracamy ilość elementów w słowniku312312312
=======
    return len(slownik)  # zwracamy ilość elementów w słowniku
>>>>>>> remotes/origin/inpg


def zapisz(slownik):
    
    pliktxt = open(sPlik, "w")
    for wobcy in slownik:
        
        znaczenia = ",".join(slownik[wobcy])
        # wyraz_obcy:znaczenie1,znaczenie2,...
        linia = ":".join([wobcy, znaczenia])
        pliktxt.write(linia)  
        # można też tak:
        
    pliktxt.close()  # zamykamy plik


def oczysc(str):
    str = str.strip()  # usuń początkowe lub końcowe białe znaki
<<<<<<< HEAD
    str = str.lower()  # zmień na małe litery
=======
    str = str.lower()  # zmień na małe litery3124124124
>>>>>>> remotes/origin/inpg
    return str


def main(args):
    print("""Podaj dane w formacie:
    wyraz obcy: znaczenie1, znaczenie2
    Aby zakończyć wprowadzanie danych, podaj 0.
    """)

    # wobce = set() # pusty zbiór wyrazów obcych
    # zmienna oznaczająca, że użytkownik uzupełnił lub zmienił słownik
    nowy = False
    ileWyrazow = otworz(sPlik)
    print("Wpisów w bazie:", ileWyrazow)

    # główna pętla programu
    while True:
        dane = input("Podaj dane: ")
        t = dane.split(":")
        wobcy = t[0].strip().lower()  # robimy to samo, co funkcja oczysc()
        if wobcy == 'koniec':
            break
        elif dane.count(":") == 1:  # sprawdzamy poprawność danych
            if wobcy in slownik:
                print("Wyraz", wobcy, " i jego znaczenia są już w słowniku.")
                op = input("Zastąpić wpis (t/n)? ")
            # czy wyrazu nie ma w słowniku? a może chcemy go zastąpić?
            if wobcy not in slownik or op == "t":
                znaczenia = t[1].split(",")  # znaczenia zapisujemy w liście
                znaczenia = list(map(oczysc, znaczenia))  # oczyszczamy listę
                slownik[wobcy] = znaczenia
                nowy = True
        else:
            print("Błędny format!")

    if nowy:
        zapisz(slownik)

    print(slownik)

    print("=" * 50)
    print("{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia"))
    print("=" * 50)
    for wobcy in slownik:
        print("{0: <15}{1: <40}".format(wobcy, ",".join(slownik[wobcy])))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
