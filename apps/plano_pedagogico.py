import pandas as pd
import streamlit as st
from data.create_data import create_df_bacharelado_biologia, create_df_bacharelado_biotecnologia, create_df_bacharelado_fisica, create_df_bacharelado_matematica, create_df_bacharelado_neuro, create_df_bacharelado_quimica, create_df_engenharia_aeroespacial, create_df_engenharia_ambiental, create_df_engenharia_energia, create_df_engenharia_materiais, create_df_grade_horas, create_df_bacharelado_ciencia_tecnologia, create_df_eng_gestao, create_df_eng_gestao_plano

def funcao_util(df):
    st.write(df)
    return 

def app():
    option = st.selectbox(
    '',
    (
        "",
        "Bacharelado em Ciência e Tecnologia",
        "Engenharia de Gestão",
        "Bacharelado de Biotecnologia",
        # "Bacharelado de Ciência da Computação",
        "Bacharelado de Ciências Biológicas",
        "Bacharelado de Física",
        "Bacharelado de Matemática",
        "Bacharelado de Química",
        "Bacharelado de Neurociência",
        "Engenharia de Ambiental e Urbana",
        "Engenharia de Energia",
        # "Engenharia de Informação",
        # "Engenharia de Instrumentação Automação e Robótica",
        "Engenharia de Materiais",
        "Engenharia de Aeroespacial"#,
        # "Engenharia de Biomédica"
    ))
    
    if option == "Bacharelado em Ciência e Tecnologia":
        funcao_util(create_df_bacharelado_ciencia_tecnologia())
        pass
    if option == "Engenharia de Gestão":
        funcao_util(create_df_eng_gestao())
        pass
    elif option == "Bacharelado de Biotecnologia":
        funcao_util(create_df_bacharelado_biotecnologia())
        pass
    elif option == "Bacharelado de Ciência da Computação":
        pass
    elif option == "Bacharelado de Ciências Biológicas":
        funcao_util(create_df_bacharelado_biologia())
        pass
    elif option == "Bacharelado de Física":
        funcao_util(create_df_bacharelado_fisica())
        pass
    elif option == "Bacharelado de Matemática":
        funcao_util(create_df_bacharelado_matematica())
        pass
    elif option == "Bacharelado de Química":
        funcao_util(create_df_bacharelado_quimica())
        pass
    elif option == "Bacharelado de Neurociência":
        funcao_util(create_df_bacharelado_neuro())
        pass
    elif option == "Engenharia de Ambiental e Urbana":
        funcao_util(create_df_engenharia_ambiental())
        pass
    elif option == "Engenharia de Energia":
        funcao_util(create_df_engenharia_energia())
        pass
    elif option == "Engenharia de Informação":
        pass
    elif option == "Engenharia de Instrumentação Automação e Robótica":
        pass
    elif option == "Engenharia de Materiais":
        funcao_util(create_df_engenharia_materiais())
        pass
    elif option == "Engenharia de Aeroespacial":
        funcao_util(create_df_engenharia_aeroespacial())
        pass
    elif option == "Engenharia de Biomédica":
        pass

        