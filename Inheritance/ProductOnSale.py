import re


class Zbozi:
    def __init__(self, nazev, cena):
        """
        Nastavi cenu a nazev zbozi
        :param nazev: str Nazev jen znaky anglicke abecedy 2-50
        :param cena: float 0 az 1mio, kladne cislo
        """
        assert type(nazev) == str and re.match(r"[a-zA-Z]{2,50}", nazev)
        assert (type(cena) == float or type(cena) == int) and 0 < cena < 1000000
        self._nazev = nazev
        self._cena = cena

    def get_cena(self):
        """
        Vrati cenu
        :return: float
        """
        return self._cena


class ZlevneneZbozi(Zbozi):
    def __init__(self, nazev, cena, sleva):
        """
        Nastavi nazev, cenu, slevu
        :param nazev: str Nazev jen znaky anglicke abecedy 2-50
        :param cena: float 0 az 1mio, kladne cislo
        :param sleva: float 0.0 az 0.5, kladne cislo
        """
        super().__init__(nazev, cena)
        assert type(sleva) == float and 0 <= sleva <= 0.5
        self._sleva = sleva

    def get_cena(self):
        """
        Vrati zlevnenou cenu
        :return: float
        """
        return self._cena - self._cena * self._sleva


a = ZlevneneZbozi('Rohlik', 2, 0.0)
print(a.get_cena())
