import json
from anima import utils as u

KEY_H_SECUNDARIAS = ['acrobacias', 'atletismo', 'montar', 'nadar', 'trepar', 'saltar', 'pilotar', 'estilo', 'intimidar',
                     'liderazgo',
                     'persuasion', 'comercio', 'callejeo', 'etiqueta', 'advertir', 'buscar', 'rastrear', 'animales',
                     'ciencia', 'ley',
                     'herbolaria', 'historia', 'tactica', 'medicina', 'memorizar', 'navegacion', 'ocultismo',
                     'tasacion',
                     'valoracion_magica', 'frialdad', 'peoezas_fuerza', 'resistir_dolor', 'cerrajeria', 'disfraz',
                     'ocultarse', 'robo',
                     'sigilo', 'tramperia', 'venenos', 'arte', 'baile', 'forja', 'runas', 'alquimia', 'animismo',
                     'musica',
                     'trucos_manos', 'caligrafia', 'ritual', 'orfebreria', 'confeccion', 'confeccion_marionetas']

KEY_H_PSIQUICAS = ['potencial_psiquico', 'proyeccion_psiquica', 'disciplinas_psiquicas', 'poderes_psiquicos',
                   'patrones_mentales', 'cv_libres', 'cv_innatos']

KEY_H_SOBRENATURALES = ['proyeccion_magica_ofensiva', 'proyeccion_magica_defensiva', 'dominar', 'atar', 'desconvocar',
                        'convocar', 'zeon', 'regeneracion_zeon', 'act', 'nivel_magia']

KEY_H_COMBATE = ['turno', 'h_ataque', 'h_defensa', 'dano']

KEY_RESISTENCIAS = ['fisica', 'magica', 'psiquica', 'veneno', 'enfermedad']

KEY_ATRIBUTOS = ['fuerza', 'destreza', 'agilidad', 'constitucion', 'poder', 'inteligencia', 'voluntad',
                 'percepcion']

"""
    Pendientes:
    -   TA
    -   KI
            puntos KI
            Acumulaciones
            Habilidades
            Tecnicas
    -   Nivel de magia
    -   Especial
    -   Artefactos
"""


class Personaje:
    nombre: str
    nivel: int
    clase: str
    categoria: str

    '''Caracteristicas fisicas'''
    pv: int
    cansancio: int
    tipo_movimiento: int
    regeneracion: int
    acciones_turno: int
    presencia: int
    apariencia: int
    tamano: int

    '''Varios'''
    habilidades_naturales: str
    ventajas: str
    # desventajas: str
    lore: str

    '''Inventario'''
    inventario: [u.Objeto]
    '''Grimorio'''
    grimorios: [u.Grimorio]

    '''Atributos'''
    atributos: dict[str, u.Atributo] = {
        'fuerza': None,
        'destreza': None,
        'agilidad': None,
        'constitucion': None,
        'poder': None,
        'inteligencia': None,
        'voluntad': None,
        'percepcion': None
    }

    '''Resistencias'''
    resistencias: dict[str, u.Resistencia] = {
        'fisica': None,
        'magica': None,
        'psiquica': None,
        'veneno': None,
        'enfermedad': None
    }

    '''HABILIDADES'''
    h_combate: dict = {
        'turno': None,
        # HAB. COMBATE
        'h_ataque': None,
        'h_defensa': None,
        'dano': None
        # parada: u.Combate
        # esquiva: u.Combate
        # pasivas
        # 'llevar_armadura': None
        # tablasl
        # artes_marciales
        # tablas_armas
    }

    # Ki
    ki: dict = {}

    # HAB. SOBRENATURALES
    h_sobrenaturales: dict = {
        'proyeccion_magica_ofensiva': None,
        'proyeccion_magica_defensiva': None,
        'dominar': None,
        'atar': None,
        'desconvocar': None,
        'convocar': None,
        # pasivas
        'zeon': None,
        'regeneracion_zeon': None,
        'act': None,
        'nivel_magia': None
        # tablas
        # tablas_proyeccion_magica: Tabla_Anima
    }

    # HAB. PSIQUICAS
    h_psiquicas = {
        # Habilidad
        'potencial_psiquico': None,
        'proyeccion_psiquica': None,
        # pasivas
        'disciplinas_psiquicas': None,
        'poderes_psiquicos': None,
        'patrones_mentales': None,
        'cv_libres': None,
        'cv_innatos': None

        # tablas
        # tablas_proyeccion_psiquica: Tabla_Anima
    }
    # HAB. SECUNDARIAS
    #  atleticas
    h_secundarias: dict[u.Activa] = {

        'acrobacias': None,
        'atletismo': None,
        'montar': None,
        'nadar': None,
        'trepar': None,
        'saltar': None,
        'pilotar': None,
        #  sociales
        'estilo': None,
        'intimidar': None,
        'liderazgo': None,
        'persuasion': None,
        'comercio': None,
        'callejeo': None,
        'etiqueta': None,
        #  perceptivas
        'advertir': None,
        'buscar': None,
        'rastrear': None,
        #  intelectuales
        'animales': None,
        'ciencia': None,
        'ley': None,
        'herbolaria': None,
        'historia': None,
        'tactica': None,
        'medicina': None,
        'memorizar': None,
        'navegacion': None,
        'ocultismo': None,
        'tasacion': None,
        'valoracion_magica': None,
        #  vigor
        'frialdad': None,
        'peoezas_fuerza': None,
        'resistir_dolor': None,
        #  subterfugio
        'cerrajeria': None,
        'disfraz': None,
        'ocultarse': None,
        'robo': None,
        'sigilo': None,
        'tramperia': None,
        'venenos': None,
        #  creativas
        'arte': None,
        'baile': None,
        'forja': None,
        'runas': None,
        'alquimia': None,
        'animismo': None,
        'musica': None,
        'trucos_manos': None,
        'caligrafia': None,
        'ritual': None,
        'orfebreria': None,
        'confeccion': None,
        'confeccion_marionetas': None
    }

    def control_turno(self):
        pass

    def control_h_ataque(self):
        pass

    def control_h_defensa(self):
        pass

    # def control_sobrenaturales(self):
    #     pass

    def control(self, nom_hab, mod=0, objeto=None):
        # checkear tipo? Habilidad, Activa, Combate?
        nom_hab = str(nom_hab).lower()
        objeto = str(objeto).lower()
        attr_na = "no_existe_el_atributo"

        # claves_generales

        tar_dict = None
        if nom_hab in KEY_ATRIBUTOS:
            tar_dict = self.atributos
        if nom_hab in KEY_RESISTENCIAS:
            tar_dict = self.resistencias
        if nom_hab in KEY_H_COMBATE:
            tar_dict = self.h_combate
        # clave_ki
        if nom_hab in KEY_H_SOBRENATURALES:
            tar_dict = self.h_sobrenaturales
        if nom_hab in KEY_H_PSIQUICAS:
            tar_dict = self.h_psiquicas
        if nom_hab in KEY_H_SECUNDARIAS:
            tar_dict = self.h_secundarias

        if tar_dict is None:
            hab_attr = getattr(self, nom_hab, attr_na)
        else:
            hab_attr = tar_dict.get(nom_hab)

#       AUTO-BUSQUEDA por los dicts?
        # if hab_attr == attr_na:
        #     self.

        if isinstance(hab_attr, u.Combate):
            return hab_attr.control(objeto, mod)
        elif isinstance(hab_attr, u.Habilidad):
            return hab_attr.control(mod)
        else:
            return None

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, ensure_ascii=False).encode('utf8').decode()
