import re
import pandas as pd
from anima import personaje as p
from anima import utils as u

H_SEC_PATT = '^(.*) (-?\d{1,4})( \(-?\d{1,4}\))?$'
H_COMB_PATT = '^\s?(-?\d{1,4}) (.*)$'


def extract_value(df, row, column):
    value = df.iloc[row - 2, column - 1]
    return value if isinstance(value, str) is False else value.lower()


def extract(t_dict: dict, df, name, row, column):
    t_dict[name] = extract_value(df, row, column)


def rellena_pj_desde_excel(xlsm, pj: p.Personaje):
    carga_hoja_resumen(xlsm, pj)

    return pj


def carga_hoja_resumen(xlsm, pj):
    resumen_dict = import_resumen(xlsm)

    # generales
    generales_d = resumen_dict['generales']
    rellenar_pj(generales_d, pj)

    # atributos
    atributos_d = resumen_dict['atributos']
    pj.atributos = {} if pj.atributos is None else pj.atributos
    for k, v in atributos_d.items():
        pj.atributos[k] = u.Atributo(v)

    # resistencias
    resistencias_d = resumen_dict['resistencias']
    pj.resistencias = {} if pj.resistencias is None else pj.resistencias
    for k, v in resistencias_d.items():
        pj.resistencias[k] = u.Resistencia(v)

    # habilidades de combate
    h_combate_d = resumen_dict['h_combate']
    pj.h_combate = {} if pj.h_combate is None else pj.h_combate
    # pj.h_combate['llevar_armadura']

    for k, v in h_combate_d.items():
        lista_h_combate = ['turno', 'h_ataque',
                                 'h_defensa', 'dano']
        if k in lista_h_combate:
            habilidad_combate = u.Combate(None)
            for sub_k, sub_v in v.items():
                habilidad_combate.base_por_obj[sub_k] = sub_v

            pj.h_combate[k] = habilidad_combate
        else:
            pj.h_combate[k] = v

    # Ki
    ki_d = resumen_dict['ki']
    pj.ki = {} if pj.ki is None else pj.ki
    pj.ki = ki_d

    # habilidades sobrenaturales
    sobrenaturales_d = resumen_dict['sobrenaturales']
    pj.h_sobrenaturales = {} if pj.h_sobrenaturales is None else pj.h_sobrenaturales

    for k, v in sobrenaturales_d.items():
        lista_sobren_activas = ['proyeccion_magica_ofensiva', 'proyeccion_magica_defensiva',
                                'dominar', 'atar', 'desconvocar', 'convocar']
        if k in lista_sobren_activas:
            pj.h_sobrenaturales[k] = u.Habilidad(v)
        else:
            pj.h_sobrenaturales[k] = v

    # habilidades psiquicas
    psiquicas_d = resumen_dict['psiquicas']
    pj.h_psiquicas = {} if pj.h_psiquicas is None else pj.h_psiquicas

    for k, v in psiquicas_d.items():
        lista_sobren_activas = ['potencial_psiquico', 'proyeccion_psiquica']
        if k in lista_sobren_activas:
            pj.h_psiquicas[k] = u.Habilidad(v)
        else:
            pj.h_psiquicas[k] = v


    # Secundarias
    secundarias_d = resumen_dict['habilidades_secundarias']
    pj.h_secundarias = {} if pj.h_secundarias is None else pj.h_secundarias

    for k, v in secundarias_d.items():
            pj.h_secundarias[k] = u.Habilidad(v)

def import_resumen(xlsm):
    df = pd.read_excel(xlsm, sheet_name="Resumen")
    resumen_dict = {}

    # PRINCIPALES
    generales = {}

    extract(generales, df, 'nombre', 3, 13)
    extract(generales, df, 'nivel', 11, 6)
    extract(generales, df, 'clase', 11, 12)
    extract(generales, df, 'pv', 12, 5)
    extract(generales, df, 'categoria', 12, 12)

    extract(generales, df, 'presencia', 15, 8)
    # extract(generales, df, 'apariencia', 15, 8)

    # ATRIBUTOS
    atributos = {}

    extract(atributos, df, 'fuerza', 13, 6)
    extract(atributos, df, 'destreza', 13, 10)
    extract(atributos, df, 'agilidad', 13, 14)
    extract(atributos, df, 'constitucion', 13, 18)
    extract(atributos, df, 'poder', 14, 6)
    extract(atributos, df, 'inteligencia', 14, 10)
    extract(atributos, df, 'voluntad', 14, 14)
    extract(atributos, df, 'percepcion', 14, 18)

    # RESISTENCIAS
    resistencias = {}

    extract(resistencias, df, 'res_fisica', 16, 6)
    extract(resistencias, df, 'res_magica', 16, 10)
    extract(resistencias, df, 'res_psiquica', 16, 14)
    extract(resistencias, df, 'res_veneno', 16, 18)
    extract(resistencias, df, 'res_enfermedad', 16, 22)

    # COMBATE
    h_combate = {}
    # TURNO
    turno_str = extract_value(df, 19, 8)
    turno = {}
    for turno_desc in turno_str.split(','):
        t_ma = re.search(H_COMB_PATT, turno_desc)
        turno[t_ma.group(2)] = t_ma.group(1)

    h_combate['turno'] = turno
    # ATAQUE
    ha_str = extract_value(df, 22, 8)
    ha = {}
    for ha_desc in ha_str.split(','):
        t_ma = re.search(H_COMB_PATT, ha_desc)
        ha[t_ma.group(2)] = t_ma.group(1)

    h_combate['h_ataque'] = ha
    # DEFENSA
    h_def_str = extract_value(df, 25, 8)
    h_def = {}
    for h_def_desc in h_def_str.split(','):
        t_ma = re.search(H_COMB_PATT, h_def_desc)
        h_def[t_ma.group(2)] = t_ma.group(1)

    h_combate['h_defensa'] = h_def
    # DANO
    dano_str = extract_value(df, 28, 8)
    dano = {}
    for dano_desc in dano_str.split(','):
        t_ma = re.search(H_COMB_PATT, dano_desc)
        dano[t_ma.group(2)] = t_ma.group(1)

    h_combate['dano'] = dano
    # TA

    # KI
    ki = {}

    puntos_ki = {'test': 'pendiente'}
    ki['puntos_ki'] = puntos_ki
    acumulaciones_ki = {'test': 'pendiente'}
    ki['acumulaciones_ki'] = acumulaciones_ki

    habilidades_ki = [h_ki for h_ki in extract_value(df, 39, 10).split(',')]
    # habilidades_ki = {}

    ki['habilidades_ki'] = habilidades_ki

    extract(ki, df, 'tecnicas', 43, 7)
    # tecnicas = {}

    # SOBRENATURALES
    sobrenaturales = {}

    extract(sobrenaturales, df, 'act', 48, 6)
    extract(sobrenaturales, df, 'zeon', 50, 6)
    extract(sobrenaturales, df, 'regeneracion_zeon', 50, 14)

    pry_mag_list = [proy_mag for proy_mag in extract_value(df, 52, 10).split(',')]
    pry_mag_of_m = re.search(H_COMB_PATT, pry_mag_list[0])
    pry_mag_def_m = re.search(H_COMB_PATT, pry_mag_list[1])

    sobrenaturales['proyeccion_magica_ofensiva'] = pry_mag_of_m.group(1)
    sobrenaturales['proyeccion_magica_defensiva'] = pry_mag_def_m.group(1)

    extract(sobrenaturales, df, 'nivel_magia', 54, 9)
    extract(sobrenaturales, df, 'convocar', 48, 25)
    extract(sobrenaturales, df, 'dominar', 50, 25)
    extract(sobrenaturales, df, 'atar', 48, 32)
    extract(sobrenaturales, df, 'desconvocar', 50, 32)

    # PSIQUICAS
    psiquicas = {}

    extract(psiquicas, df, 'potencial_psiquico', 62, 10)
    extract(psiquicas, df, 'proyeccion_psiquica', 64, 11)
    extract(psiquicas, df, 'disciplinas_psiquicas', 66, 11)
    extract(psiquicas, df, 'poderes_psiquicos', 68, 10)
    extract(psiquicas, df, 'patrones_mentales', 60, 24)
    extract(psiquicas, df, 'cv_libres', 60, 8)
    extract(psiquicas, df, 'cv_innatos', 60, 15)

    # GENERALES 2
    extract(generales, df, 'ventajas', 73, 11)
    extract(generales, df, 'habilidades_naturales', 76, 11)
    extract(generales, df, 'tamano', 93, 7)
    extract(generales, df, 'tipo_movimiento', 93, 19)
    extract(generales, df, 'cansancio', 95, 8)
    extract(generales, df, 'regeneracion', 95, 17)
    extract(generales, df, 'acciones_turno', 95, 33)

    # SECUNDARIAS
    secundarias = {}

    secund_str = extract_value(df, 98, 4)

    for secund_desc in secund_str.split(','):
        t_ma = re.search(H_SEC_PATT, secund_desc)
        secundarias[t_ma.group(1)] = t_ma.group(2)

    resumen_dict['generales'] = generales
    resumen_dict['atributos'] = atributos
    resumen_dict['resistencias'] = resistencias
    resumen_dict['h_combate'] = h_combate
    resumen_dict['ki'] = ki
    resumen_dict['sobrenaturales'] = sobrenaturales
    resumen_dict['psiquicas'] = psiquicas
    resumen_dict['habilidades_secundarias'] = secundarias

    return resumen_dict


def rellenar_pj(datos_dict, pj: p.Personaje):
    for k, v in datos_dict.items():
        setattr(pj, k, v)
        # getattr(pj, k)
