import pandas as pd
import streamlit as st
from data.create_data import create_df_lic_matematica, create_df_lic_fisica, create_df_lic_em_quimica, create_df_lic_em_filosofia, create_df_lic_biologia, create_df_lch, create_df_bach_filosofia, create_df_Planej_territorial, create_df_LCNE, create_df_BCH, create_df_Econo, create_df_Politicas_publicas, create_df_Relacoes_internacionais, create_df_engenharia_biomedica, create_df_engenharia_iar, create_df_bacharelado_biologia, create_df_bacharelado_biotecnologia, create_df_bacharelado_fisica, create_df_bacharelado_matematica, create_df_bacharelado_neuro, create_df_bacharelado_quimica, create_df_engenharia_aeroespacial, create_df_engenharia_ambiental, create_df_engenharia_energia, create_df_engenharia_informacao, create_df_engenharia_materiais, create_df_bacharelado_ciencia_tecnologia, create_df_eng_gestao, create_df_bacharelado_ciencia_comp

def funcao_util(df):
    st.write(df)
    return 

def app():
    option = st.selectbox(
    '',
    (
        "",
        "Bacharelado em Ciência e Tecnologia",
        "Bacharelado de Biotecnologia",
        "Bacharelado de Ciência da Computação",
        "Bacharelado de Ciências Biológicas",
        "Bacharelado de Física",
        "Bacharelado de Matemática",
        "Bacharelado de Química",
        "Bacharelado de Neurociência",
        "Engenharia de Instrumentação Automação e Robótica",
        "Engenharia de Ambiental e Urbana",
        "Engenharia de Energia",
        "Engenharia de Informação",
        "Engenharia de Materiais",
        "Engenharia de Aeroespacial",
        "Engenharia de Biomédica",
        "Engenharia de Gestão",
        "Bacharelado em Ciências Econômicas",
        "Bacharelado em Filosofia",
        "Bacharelado em Planejamento Territorial",
        "Bacharelado em Políticas Públicas",
        "Bacharelado em Relações Internacionais",
        "Bacharelado em Ciências e Humanidades",
        "Licenciatura em Ciências Humanas",
        "Licenciatura em Ciências Naturais e Exatas",
        "Licenciatura em Biologia",
        "Licenciatura em Filosofia",
        "Licenciatura em Química",
        "Licenciatura em Física",
        "Licenciatura em Matemática"
    ))

    if option == "Bacharelado em Ciência e Tecnologia":
        funcao_util(create_df_bacharelado_ciencia_tecnologia())
        pass
    if option == "Licenciatura em Ciências Humanas":
        funcao_util(create_df_lch())
        pass
    elif option == "Engenharia de Gestão":
        funcao_util(create_df_eng_gestao())
        pass
    elif option == "Bacharelado de Biotecnologia":
        funcao_util(create_df_bacharelado_biotecnologia())
        pass
    elif option == "Bacharelado de Ciência da Computação":
        funcao_util(create_df_bacharelado_ciencia_comp())
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
        funcao_util(create_df_engenharia_informacao())
        pass
    elif option == "Engenharia de Instrumentação Automação e Robótica":
        funcao_util(create_df_engenharia_iar())
        pass
    elif option == "Engenharia de Materiais":
        funcao_util(create_df_engenharia_materiais())
        pass
    elif option == "Engenharia de Aeroespacial":
        funcao_util(create_df_engenharia_aeroespacial())
        pass
    elif option == "Engenharia de Biomédica":
        funcao_util(create_df_engenharia_biomedica())
        pass
    elif option == "Bacharelado em Ciências e Humanidades":
        funcao_util(create_df_BCH())
        pass
    elif option == "Bacharelado em Ciências Econômicas":
        funcao_util(create_df_Econo())
        pass
    elif option == "Licenciatura em Ciências Naturais e Exatas":
        funcao_util(create_df_LCNE())
        pass
    elif option == "Bacharelado em Planejamento Territorial":
        funcao_util(create_df_Planej_territorial())
        pass
    elif option == "Bacharelado em Políticas Públicas":
        funcao_util(create_df_Politicas_publicas())
        pass
    elif option == "Bacharelado em Relações Internacionais":
        funcao_util(create_df_Relacoes_internacionais())
        pass
    elif option == "Bacharelado em Filosofia":
        funcao_util(create_df_bach_filosofia())
        pass
    elif option == "Licenciatura em Biologia":
        funcao_util(create_df_lic_biologia())
        pass
    elif option == "Licenciatura em Filosofia":
        funcao_util(create_df_lic_em_filosofia())
        pass
    elif option == "Licenciatura em Química":
        funcao_util(create_df_lic_em_quimica())
        pass
    elif option == "Licenciatura em Física":
        funcao_util(create_df_lic_fisica())
        pass
        