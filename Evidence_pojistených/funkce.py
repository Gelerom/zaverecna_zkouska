from datetime import datetime
from pojisteni import Pojistenec

class Funkce():
    def __init__(self, seznam_pojistenych):
        self._seznam_pojistenych = seznam_pojistenych

    def uzivatelske_rozhrani(self):
        """
        Funkce pro výběr akcí a ukončení v evidenci pojištěných
        """
        while True:
            print("------------------------------")
            print("Evidence pojištěných")
            print("------------------------------")
            print("\nVyberte si akci:")
            print("1 - Přidat nového pojištěného")
            print("2 - Vypsat všechny pojištěné")
            print("3 - Vyhledat pojištěného")
            print("4 - Konec")

            vstup = input("-> ")

            match vstup:
                case "1":
                    self.pridat_pojistence()
                case "2":
                    self.zobrazit_seznam()
                case "3":
                    self.vyhledat_pojistence()
                case "4":
                    print("\nKONEC")
                    break
                case _:
                    print("Neplatná volba. Zadejte číslo odpovídající vybrané akci.")

            try:
                input("\nPokračujte libovolnou klávesou...")
            except SyntaxError:
                pass

    def pridat_pojistence(self):
        """
        Vytvoření nového pojištěnce a přidání do seznamu
        """
        novy_pojistenec = Pojistenec(self.jmeno_pojisteneho(),
                                     self.prijmeni_pojisteneho(),
                                     self.vek_pojisteneho(),
                                     self.tel_cislo())
        self._seznam_pojistenych.append(novy_pojistenec)
        print("\nData byla uložena.")

    def zobrazit_seznam(self):
        """
        Výpis všech pojištěnců a seřazení podle příjmení
        """
        print()
        if not self._seznam_pojistenych:
            print("Seznam je prázdný.")
        else:
            serazeny_seznam = sorted(self._seznam_pojistenych, key=lambda pojistenec: pojistenec.prijmeni.lower())
            for pojistenci in serazeny_seznam:
                print(pojistenci)

    def vyhledat_pojistence(self):
        """
        Vyhledání pojištěnce podle jména a příjmení
        """
        if not self._seznam_pojistenych:
            print("\nSeznam je prázdný.")
        else:
            jmeno = self.jmeno_pojisteneho().lower()
            prijmeni = self.prijmeni_pojisteneho().lower()
            nalezeni_pojistenci = [pojistenec for pojistenec in self._seznam_pojistenych
                                   if pojistenec.jmeno.lower() == jmeno
                                   and pojistenec.prijmeni.lower() == prijmeni]
            if nalezeni_pojistenci:
                for pojistenec in nalezeni_pojistenci:
                    print(f"\n{pojistenec}")
            else:
                print("Pojištenec nebyl nalezen.")

    def jmeno_pojisteneho(self):
        """
        Validace vstupu pro jméno
        Zarovnání jmen ve výpisu
        :return: jmeno s velkým prvním písmenem
        """
        while True:
            jmeno = input("Zadej jméno pojištěného:\n").strip()
            if not jmeno.isalpha():
                print("\nJméno nesmí obsahovat čísla ani speciální znaky.\n")
            elif len(jmeno) < 3 or len(jmeno) > 10:
                print("\nZadané jméno je moc krátké nebo dlouhé (délka musí být 3 až 10 znaků).\n")
            else:
                jmeno += " " * (11 - len(jmeno))
                return jmeno.capitalize()

    def prijmeni_pojisteneho(self):
        """
        Validace vstupu pro příjmení
        Zarovnání příjmení ve výpisu
        :return: příjmení s velkým prvním písmenem
        """
        while True:
            prijmeni = input("Zadej příjmení pojištěného:\n").strip()
            if not prijmeni.isalpha():
                print("\nPříjmení nesmí obsahovat čísla ani speciální znaky.\n")
            elif len(prijmeni) < 3 or len(prijmeni) > 13:
                print("\nZadané příjmení je moc krátké nebo dlouhé (délka musí být 3 až 13 znaků).\n")
            else:
                prijmeni += " " * (14 - len(prijmeni))
                return prijmeni.capitalize()

    def vek_pojisteneho(self):
        """
        Validace a výpočet věku pojištěného
        :return: vek
        """
        while True:
            try:
                print("Zadej datum narození:")
                den = int(input("Zadej den: "))
                mesic = int(input("Zadej měsíc: "))
                rok = int(input("Zadej rok: "))
                datum_narozeni = datetime(rok, mesic, den)
                dnes = datetime.today()
                vek = dnes.year - datum_narozeni.year
                if (dnes.month, dnes.day) < (datum_narozeni.month, datum_narozeni.day):
                    vek -= 1
                if vek < 0:
                    print("\nNelze pojistit nenarozenou osobu.\n")
                else:
                    return vek

            except ValueError:
                print("Špatný formát data. Zadej platné číslo pro den, měsíc a rok.")

    def tel_cislo(self):
        """
        Validace telefonního čísla
        :return: telefon
        """
        while True:
            telefon = input("Zadej telefonní číslo:\n").strip()
            if not telefon.isdigit():
                print("\nTelefonní číslo nesmí obsahovat písmena.\n")
            elif len(telefon) != 9:
                print("\nTelefonní číslo musí mít 9 čísel.")
            else:
                return telefon

