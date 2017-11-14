
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os  # modu� udost�pniaj�cy funkcj� isfile()

slownik = {}  # pusty s�ownik
sPlik = "slownik.txt"  # nazwa pliku zawieraj�cego wyrazy i ich t�umaczenia


def otworz(plik):
    if os.path.isfile(sPlik):  # czy istnieje plik s�ownika?
        with open(sPlik, "r") as pliktxt:  # otw�rz plik do odczytu
            for line in pliktxt:  # przegl�damy kolejne linie
                # rozbijamy lini� na wyraz obcy i t�umaczenia
                t = line.split(":")
                wobcy = t[0]
                # usuwamy znaki nowych linii
                znaczenia = t[1].replace("\n", "")
                znaczenia = znaczenia.split(",")  # tworzymy list� znacze�
                # dodajemy do s�ownika wyrazy obce i ich znaczenia
                slownik[wobcy] = znaczenia
    return len(slownik)  # zwracamy ilo�� 
def zapisz(slownik):
    # otwieramy plik do zapisu, istniej�cy plik zostanie nadpisany(!)
    pliktxt = open(sPlik, "w")
    for wobcy in slownik:
        # "sklejamy" znaczenia przecinkami w jeden napis
        znaczenia = ",".join(slownik[wobcy])
        # wyraz_obcy:znaczenie1,znaczenie2,...
        linia = ":".join([wobcy, znaczenia])
        pliktxt.write(linia)  # zapisujemy w pliku kolejne linie
        # mo�na te� tak:
        # print(linia, file=pliktxt)
    pliktxt.close()  # zamykamy plik
def oczysc(str):
    str = str.strip()  # usu� pocz�tkowe lub ko�cowe bia�e znaki
    str = str.lower()  # zmie� na ma�e litery
    return str
def main(args):
    print("""Podaj dane w formacie:
    wyraz obcy: znaczenie1, znaczenie2
    Aby zako�czy� wprowadzanie danych, podaj 0.
    """)

    # wobce = set() # pusty zbi�r wyraz�w obcych
    # zmienna oznaczaj�ca, �e u�ytkownik uzupe�ni� lub zmieni� s�ownik
    nowy = False
    ileWyrazow = otworz(sPlik)
    print("Wpis�w w bazie:", ileWyrazow)

    # g��wna p�tla programu
    while True:
        dane = input("Podaj dane: ")
        t = dane.split(":")
        wobcy = t[0].strip().lower()  # robimy to samo, co funkcja oczysc()
        if wobcy == 'koniec':
            break
        elif dane.count(":") == 1:  # sprawdzamy poprawno�� danych
            if wobcy in slownik:
                print("Wyraz", wobcy, " i jego znaczenia s� ju� w s�owniku.")
                op = input("Zast�pi� wpis (t/n)? ")
            # czy wyrazu nie ma w s�owniku? a mo�e chcemy go zast�pi�?
            if wobcy not in slownik or op == "t":
                znaczenia = t[1].split(",")  # znaczenia zapisujemy w li�cie
                znaczenia = list(map(oczysc, znaczenia))  # oczyszczamy list�
                slownik[wobcy] = znaczenia
                nowy = True
        else:
            print("B��dny format!")

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