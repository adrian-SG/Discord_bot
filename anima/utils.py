import json
from collections import defaultdict

from dado import Dado


class Caracteristica:
    base: int

    def __init__(self, base):
        self.base = base

    def __str__(self):
        return f"base: {self.base}"


class Activa(Caracteristica):
    dado: Dado

    def __init__(self, base, dado: Dado):
        super().__init__(base)
        self.dado = dado

    def control(self, modif=0) -> dict:
        roll_result = self.dado.roll()
        control = {
            'desc': f'({roll_result}) + {int(self.base)} + [{modif}]',
            'result': roll_result + int(self.base) + modif,
            'pifia': True if roll_result <= self.dado.nivel_pifia else False,
            'abierta': True if roll_result >= self.dado.nivel_abierta else False
        }
        return control


class Habilidad(Activa):

    def __init__(self, base):
        dado = Dado(100)
        dado.nivel_pifia = 3
        dado.nivel_abierta = 90
        super().__init__(base, dado)


class Combate(Habilidad):

    def __init__(self, base):
        super().__init__(base)
        self.base_por_obj: defaultdict = defaultdict(lambda: self.base)

    def control(self, objeto: str, modif=0):
        roll_result = self.dado.roll()
        control = {
            'desc': f'({roll_result}) + {int(self.base_por_obj.get(objeto))} + [{modif}]',
            'result': roll_result + int(self.base_por_obj.get(objeto)) + modif,
            'pifia': True if roll_result <= self.dado.nivel_pifia else False,
            'abierta': True if roll_result >= self.dado.nivel_abierta else False
        }
        return control

    def __str__(self):
        return json.dumps(self.base_por_obj, default=lambda o: o.__dict__,
                          indent=4, ensure_ascii=False).encode('utf8').decode()


class Resistencia(Activa):

    def __init__(self, base):
        dado = Dado(100)
        super().__init__(base, dado)


class Atributo(Activa):

    def __init__(self, base):
        dado = Dado(10)
        dado.nivel_pifia = 1
        dado.nivel_abierta = 10
        super().__init__(base, dado)


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

