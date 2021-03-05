from collections import defaultdict

from dado import Dado


class Caracteristica:
    base: int

    def __init__(self, base):
        self.base = base


class Activa(Caracteristica):
    dado: Dado

    def __init__(self, base, dado: Dado):
        super().__init__(base)
        self.dado = dado

    def control(self, modif=0):
        return self.dado.roll() + self.base + modif


class Habilidad(Activa):

    def __init__(self, base):
        super().__init__(base, Dado(100))


class Combate(Habilidad):

    def __init__(self, base):
        super().__init__(base)
        self.base_por_obj: defaultdict = defaultdict(lambda: self.base)

    def control(self, objeto: str, modif=0):
        return self.dado.roll() + self.base_por_obj.get(objeto) + modif


class Resistencia(Activa):

    def __init__(self, base):
        super().__init__(base, Dado(100))


class Atributo(Activa):

    def __init__(self, base):
        super().__init__(base, Dado(10))


class Grado:
    nombre: str
    int_req: int
    zeon: int
    mant: int
    efecto: int


class Hechizo:
    nombre: str
    nivel: int
    desc: str
    tipo: str
    accion: str
    via: str
    mant_diario: bool

    grados: dict[Grado]


class Grimorio:
    hechizos: list[Hechizo]


class Dinero:
    oro: int
    plata: int
    cobre: int

    def __str__(self):
        return f"{self.oro} Oro, {self.plata} Plata, {self.cobre} Cobre"

    def add(self, oro, plata, cobre):
        self.cobre += cobre
        self.plata += plata
        self.oro += oro

    def normalizar(self):
        # parte entera
        # mas resto de cobre, parte entera
        # mas resto de plata
        pass

    def __init__(self, oro=0, plata=0, cobre=0):
        self.oro, self.plata, self.cobre = oro, plata, cobre


class Objeto:
    nombre: str
    tipo: str
    peso: int
    coste: Dinero

