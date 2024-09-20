from funkce import Funkce

class Evidence:

    def __init__(self):
        self._seznam_pojistenych = []
        self.funkce = Funkce(self._seznam_pojistenych)

    def spustit_evidenci(self):
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
                    self.funkce.pridat_pojistence()
                case "2":
                    self.funkce.zobrazit_seznam()
                case "3":
                    self.funkce.vyhledat_pojistence()
                case "4":
                    print("\nKONEC")
                    break
                case _:
                    print("Neplatná volba. Zadejte číslo odpovídající vybrané akci.")

            try:
                input("\nPokračujte libovolnou klávesou...")
            except SyntaxError:
                pass








