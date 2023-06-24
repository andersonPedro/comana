import pandas as pd
import os
from PIL import Image

def create_table(n=7):
    df = pd.DataFrame({"x": range(1, 11), "y": n})
    df['x*y'] = df.x * df.y
    return df

def create_df_grade_horas():
    return pd.read_json(os.getcwd()+'\\data\\courses\\bacharelado_ciencia_tecnologia\\grade_horas.json')

def create_df_bacharelado_ciencia_tecnologia():
    return pd.read_json(os.getcwd()+'\\data\\courses\\bacharelado_ciencia_tecnologia\\bacharelado_ciencia_tecnologia.json')

def create_grade_horas():
    return pd.read_json(os.getcwd()+'\\data\\courses\\bacharelado_ciencia_tecnologia\\grade_horas.json')

def create_ufabc_logo():
    return Image.open(os.getcwd()+'\\data\\images\\ufabc_logo.png')
