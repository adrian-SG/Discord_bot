import re
import pandas as pd

H_SEC_PATT = '^(.*) (-?\d{1,4})( \(-?\d{1,4}\))?$'
H_COMB_PATT = '^\s?(-?\d{1,4}) (.*)$'


def extract(t_dict: dict , df, name, row, column):
    t_dict[name] = df.iloc[row-2, column-1]

def extract_value(df, row, column):
    return df.iloc[row-2, column-1]

def import_resumen(xlsm):
    df = pd.read_excel(xlsm, sheet_name="Resumen")
    extracted = {}

    # PRINCIPALES
    generales = {}

    extract(generales, df, 'nombre', 3, 13)
    extract(generales, df, 'nivel', 11, 6)
    extract(generales, df, 'clase', 11, 12)
    extract(generales, df, 'pv', 12, 5)
    extract(generales, df, 'categoria', 12, 12)

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
    ki['puntos_ki']=puntos_ki
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

    proyeccion_magica = {
        'ofensiva': pry_mag_of_m.group(1),
        'defensiva': pry_mag_def_m.group(1)
    }

    sobrenaturales['proyeccion_magica'] = proyeccion_magica

    extract(sobrenaturales, df, 'nivel_magia', 54, 9)
    extract(sobrenaturales, df, 'convocar', 48, 25)
    extract(sobrenaturales, df, 'dominar', 50, 25)
    extract(sobrenaturales, df, 'atar', 48, 32)
    extract(sobrenaturales, df, 'desconvocar', 50, 32)

    # GENERALES 2
    extract(generales, df, 'ventajas', 73, 11)
    extract(generales, df, 'habilidades_naturales', 76, 11)
    extract(generales, df, 'tamano',93, 7)
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

    extracted['generales'] = generales
    extracted['atributos'] = atributos
    extracted['resistencias'] = resistencias
    extracted['sobrenaturales'] = sobrenaturales
    extracted['ki'] = ki
    extracted['habilidades_secundarias'] = secundarias


    return extracted



