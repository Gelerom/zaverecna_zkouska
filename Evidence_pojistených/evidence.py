from funkce import Funkce

class Evidence:

    def __init__(self):
        self._seznam_pojistenych = []
        self.funkce = Funkce(self._seznam_pojistenych)

    def spustit_evidenci(self):
        return self.funkce.uzivatelske_rozhrani()








