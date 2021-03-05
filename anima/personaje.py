import utils as u

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
    desventajas: str
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
    turno: dict[u.Combate]
    # HAB. COMBATE
    h_ataque: dict[u.Combate]
    h_defensa: dict[u.Combate]
    dano: dict[u.Combate]
        # parada: u.Combate
        # esquiva: u.Combate
    # pasivas
    llevar_armadura: u.Habilidad
    # tablas
    # artes_marciales
    # tablas_armas

    # HAB. SOBRENATURALES
    proyeccion_magica: dict[u.Activa]
    proyeccion_magica_defensiva: u.Activa
    convocar: u.Activa
    dominar: u.Activa
    atar: u.Activa
    desconvocar: u.Activa
    # pasivas
    zeon: u.Atributo
    regeneracion_zeon = u.Atributo
    act: u.Atributo
    nivel_magia: str

    # tablas
    # tablas_proyeccion_magica: Tabla_Anima

    # HAB. PSIQUICAS
    proyeccion_psiquica: u.Activa
    # pasivas
    cv: u.Atributo
    # tablas
    # tablas_proyeccion_psiquica: Tabla_Anima

    # HAB. SECUNDARIAS
    #  atleticas
    acrobacias: u.Activa
    atletismo: u.Activa
    montar: u.Activa
    nadar: u.Activa
    trepar: u.Activa
    saltar: u.Activa
    pilotar: u.Activa
    #  sociales
    estilo: u.Activa
    intimidar: u.Activa
    liderazgo: u.Activa
    persuasion: u.Activa
    comercio: u.Activa
    callejeo: u.Activa
    etiqueta: u.Activa
    #  perceptivas
    advertir: u.Activa
    buscar: u.Activa
    rastrear: u.Activa
    #  intelectuales
    animales: u.Activa
    ciencia: u.Activa
    ley: u.Activa
    herbolaria: u.Activa
    historia: u.Activa
    tactica: u.Activa
    medicina: u.Activa
    memorizar: u.Activa
    navegacion: u.Activa
    ocultismo: u.Activa
    tasacion: u.Activa
    valoracion_magica: u.Activa
    #  vigor
    frialdad: u.Activa
    peoezas_fuerza: u.Activa
    resistir_dolor: u.Activa
    #  subterfugio
    cerrajeria: u.Activa
    disfraz: u.Activa
    ocultarse: u.Activa
    robo: u.Activa
    sigilo: u.Activa
    tramperia: u.Activa
    venenos: u.Activa
    #  creativas
    arte: u.Activa
    baile: u.Activa
    forja: u.Activa
    runas: u.Activa
    alquimia: u.Activa
    animismo: u.Activa
    musica: u.Activa
    trucos_manos: u.Activa
    caligrafia: u.Activa
    ritual: u.Activa
    orfebreria: u.Activa
    confeccion: u.Activa
    confeccion_marionetas: u.Activa


    def control(self, nom_hab, mod=0, objeto=None):
        # checkear tipo? Habilidad, Activa, Combate?
        hab_attr = self.__getattribute__(nom_hab)

        if isinstance(hab_attr, u.Combate):
            return hab_attr.control(objeto, mod)
        elif isinstance(hab_attr, u.Activa):
            return hab_attr.control(mod)
        else:
            return None

