class VazitelneInterface:
    def get_vaha_v_kg(self):
        raise NotImplementedError

    def get_cena_za_kg(self):
        raise NotImplementedError


class KusoveInterface:
    def get_pocet_kusu_v_baleni(self):
        raise NotImplementedError

    def get_cena_za_kus(self):
        raise NotImplementedError

    def get_cena_za_baleni(self):
        raise NotImplementedError


class ZlevnitelneInterface:
    def set_sleva(self):
        raise NotImplementedError

    def get_cena_po_sleve(self):
        raise NotImplementedError
