class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} {self.vek}\t\t{self.tel_cislo}"
