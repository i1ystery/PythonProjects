import re


class VazitelneInterface:
    def get_vaha_v_kg(self):
        raise NotImplemented

    def get_cena_za_kg(self):
        raise NotImplemented


class KusoveInterface:
    def get_pocet_kusu_v_baleni(self):
        raise NotImplemented

    def get_cena_za_kus(self):
        raise NotImplemented

    def get_cena_za_baleni(self):
        raise NotImplemented


class ZlevnitelneInterface:
    def set_sleva(self):
        raise NotImplemented

    def get_cena_po_sleve(self):
        raise NotImplemented


class Zbozi:
    def __init__(self, nazev, cena):
        """
        Nastavi cenu a nazev zbozi
        :param nazev: str Nazev jen znaky anglicke abecedy 2-50
        :param cena: float 0 az 1mio, kladne cislo
        """
        assert type(nazev) == str and re.match(r"[a-zA-Z]{2,50}", nazev)
        assert (type(cena) == float or type(cena) == int) and cena > 0 and cena < 1000000
        self._nazev = nazev
        self._cena = cena

    def get_cena(self):
        """
        Vrati cenu
        :return: int
        """
        return self._cena


class ZlevneneZbozi(Zbozi, ZlevnitelneInterface):
    pass


a = ZlevneneZbozi('Ahoj',23)
a.set_sleva()
