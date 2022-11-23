import random

class KoPapirOllo:
    """
    Osztály, mely kezeli a Kő-papír-olló játék példányát.
    """

    def __init__(self):
        """
        Osztály változóinak inicializálása.
        """
        self.gyozelem = 0
        self.vereseg = 0
        self.dontetlen = 0
        self.lehetoseg = {'ko': 0, 'papir': 1, 'ollo': 2}

    def veletlen_dontes(self):
        """
        A 'lehetoseg' listából kiválaszt egy véletlenszerű elemet.
        Vissza ad egy elemet, mely az ellenfelünk döntése lesz.
        """
        return random.choice(list(self.lehetoseg.keys()))

    def ellenorzes(self, jatekos, ellenfel):
        """
        Ellenőrzi, hogy mi lett a játék kimenetele.
        első paraméter: Szám alapú reprezentációja a döntésünknek a self.lehetoseg listából.
        második paraméter: Szám alapú reprezentációja az ellenfelünk döntésének a self.lehetoseg listából.
        """
        eredmeny = (jatekos - ellenfel) % 3
        if eredmeny == 0:
            self.dontetlen += 1
            print("A jatek dontetlen lett!")
        elif eredmeny == 1:
            self.gyozelem += 1
            print("Te gyoztel! Kihivlak egy visszavagora!")
        elif eredmeny == 2:
            self.vereseg += 1
            print("Haha, vesztettel! Szeretnel visszavagot?")

    def pontszam(self):
        """
        Kiírja a jelenlegi pontszámokat.
        """
        print(f"Van {self.gyozelem} gyozelmed, {self.vereseg} vereseged, es {self.dontetlen} dontetlened.")

    def futtatas(self):
        """
        Lefuttat egy Kő-papír-olló kört.
        """
        while True:
            jatekos_dontes = input("A lehetosegek a kovetkezok: 'ko', 'papir', vagy 'ollo'.\n"
                               "Melyiket valasztod? ").lower()
            if jatekos_dontes not in self.lehetoseg.keys():
                print("Helytelen bemeneti adat!")
            else:
                break
        ellenfel_dontes = self.veletlen_dontes()
        print(f"A te valasztasod: {jatekos_dontes} , az enyem pedig: {ellenfel_dontes}.")
        self.ellenorzes(self.lehetoseg[jatekos_dontes], self.lehetoseg[ellenfel_dontes])