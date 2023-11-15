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

## Imagens
def create_ufabc_logo():
    return Image.open(os.path.join(os.getcwd(), 'data', 'images', 'ufabc_logo.png'))

def create_livro():
    return Image.open(os.path.join(os.getcwd(), 'data', 'images', 'livro.png'))

def create_aprendendo():
    return Image.open(os.path.join(os.getcwd(), 'data', 'images', 'aprendendo.png'))

def create_pica_pau():
    return Image.open(os.path.join(os.getcwd(), 'data', 'images', 'pica_pau.png'))

