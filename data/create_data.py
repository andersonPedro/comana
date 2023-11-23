import pandas as pd
import os
from PIL import Image

def create_table(n=7):
    df = pd.DataFrame({"x": range(1, 11), "y": n})
    df['x*y'] = df.x * df.y
    return df

## Cursos
def create_df_grade_horas():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_ciencia_tecnologia', 'grade_horas.json'))

def create_df_bacharelado_ciencia_tecnologia():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_ciencia_tecnologia', 'bacharelado_ciencia_tecnologia.json'))

def create_df_eng_gestao():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_gestao', 'engenharia_gestao.json'))

def create_df_eng_gestao_plano():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_gestao', 'eng_gestao_plano.json'))

def create_df_bacharelado_biologia():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_biologia', 'BIOLOGIA.json'))

def create_df_bacharelado_biotecnologia():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_biotecnologia', 'bacharelado_biotecnologia.json'))

def create_df_bacharelado_fisica():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_fisica', 'bacharelado_fisica.json'))

def create_df_bacharelado_matematica():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_matematica', 'mat.json'))

def create_df_bacharelado_neuro():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_neuro', 'NEURO.json'))

def create_df_bacharelado_quimica():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_quimica', 'quimica.json'))

def create_df_engenharia_aeroespacial():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_aeroespacial', 'AERO.json'))

def create_df_engenharia_ambiental():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_ambiental', 'AMBIENTAL.json'))

def create_df_engenharia_energia():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_energia', 'EngEnergia.json'))

def create_df_engenharia_materiais():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_materiais', 'materiais.json'))

def create_df_engenharia_iar():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_iar', 'engenharia_iar.json'))

def create_df_bach_filosofia():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bach_filosofia', 'bach_filosofia.json'))

def create_df_bacharelado_ciencia_comp():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'bacharelado_ciencia_comp', 'bacharelado_ciencia_comp.json'))

def create_df_BCH():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'BCH', 'BCH.json'))

def create_df_Econo():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'Econo', 'Econo.json'))

def create_df_engenharia_biomedica():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_biomedica', 'biomedica.json'))

def create_df_engenharia_informacao():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'engenharia_informacao', 'informacao.json'))

def create_df_lch():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'lch', 'LCH.json'))

def create_df_LCNE():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'LCNE', 'LCNE.json'))

def create_df_lic_biologia():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'lic_biologia', 'lic_biologia.json'))

def create_df_lic_em_filosofia():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'lic_em_filosofia', 'lic_em_filosofia.json'))

def create_df_lic_em_quimica():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'lic_em_quimica', 'lic_em_quimica.json'))

def create_df_lic_fisica():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'lic_fisica', 'lic_fisica.json'))

def create_df_lic_matematica():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'lic_matematica', 'lic_matematica.json'))

def create_df_Planej_territorial():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'Planej_territorial', 'Planej_territorial.json'))

def create_df_Politicas_publicas():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'Politicas_publicas', 'Politicas_publicas.json'))

def create_df_Relacoes_internacionais():
    return pd.read_json(os.path.join(os.getcwd(), 'data', 'courses', 'Relacoes_internacionais', 'Relacoes_internacionais.json'))

## Imagens
def create_ufabc_logo():
    return Image.open(os.path.join(os.getcwd(), 'data', 'images', 'ufabc_logo.png'))

def create_livro():
    return Image.open(os.path.join(os.getcwd(), 'data', 'images', 'livro.png'))

def create_aprendendo():
    return Image.open(os.path.join(os.getcwd(), 'data', 'images', 'aprendendo.png'))

def create_pica_pau():
    return Image.open(os.path.join(os.getcwd(), 'data', 'images', 'pica_pau.png'))

