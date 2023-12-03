import pandas as pd
import streamlit as st
from data.create_data import create_df_lic_matematica, create_df_lic_fisica, create_df_lic_em_quimica, create_df_lic_em_filosofia, create_df_lic_biologia, create_df_lch, create_df_bach_filosofia, create_df_Planej_territorial, create_df_LCNE, create_df_BCH, create_df_Econo, create_df_Politicas_publicas, create_df_Relacoes_internacionais, create_df_engenharia_biomedica, create_df_engenharia_iar, create_df_bacharelado_biologia, create_df_bacharelado_biotecnologia, create_df_bacharelado_fisica, create_df_bacharelado_matematica, create_df_bacharelado_neuro, create_df_bacharelado_quimica, create_df_engenharia_aeroespacial, create_df_engenharia_ambiental, create_df_engenharia_energia, create_df_engenharia_informacao, create_df_engenharia_materiais, create_df_bacharelado_ciencia_tecnologia, create_df_eng_gestao, create_df_bacharelado_ciencia_comp
import numpy as np

def plano_pedagogico_1_materia(option):

    if option == "Licenciatura em Matemática":
        return create_df_lic_matematica()
        
    if option == "Bacharelado em Ciência e Tecnologia":
        return create_df_bacharelado_ciencia_tecnologia()
        
    if option == "Licenciatura em Ciências Humanas":
        return create_df_lch()
        
    elif option == "Engenharia de Gestão":
        return create_df_eng_gestao()
        
    elif option == "Bacharelado de Biotecnologia":
        return create_df_bacharelado_biotecnologia()
        
    elif option == "Bacharelado de Ciência da Computação":
        return create_df_bacharelado_ciencia_comp()
        
    elif option == "Bacharelado de Ciências Biológicas":
        return create_df_bacharelado_biologia()
        
    elif option == "Bacharelado de Física":
        return create_df_bacharelado_fisica()
        
    elif option == "Bacharelado de Matemática":
        return create_df_bacharelado_matematica()
        
    elif option == "Bacharelado de Química":
        return create_df_bacharelado_quimica()
        
    elif option == "Bacharelado de Neurociência":
        return create_df_bacharelado_neuro()
        
    elif option == "Engenharia de Ambiental e Urbana":
        return create_df_engenharia_ambiental()
        
    elif option == "Engenharia de Energia":
        return create_df_engenharia_energia()
        
    elif option == "Engenharia de Informação":
        return create_df_engenharia_informacao()
        
    elif option == "Engenharia de Instrumentação Automação e Robótica":
        return create_df_engenharia_iar()
        
    elif option == "Engenharia de Materiais":
        return create_df_engenharia_materiais()
        
    elif option == "Engenharia de Aeroespacial":
        return create_df_engenharia_aeroespacial()
        
    elif option == "Engenharia de Biomédica":
        return create_df_engenharia_biomedica()
        
    elif option == "Bacharelado em Ciências e Humanidades":
        return create_df_BCH()
        
    elif option == "Bacharelado em Ciências Econômicas":
        return create_df_Econo()
        
    elif option == "Licenciatura em Ciências Naturais e Exatas":
        return create_df_LCNE()
        
    elif option == "Bacharelado em Planejamento Territorial":
        return create_df_Planej_territorial()
        
    elif option == "Bacharelado em Políticas Públicas":
        return create_df_Politicas_publicas()
        
    elif option == "Bacharelado em Relações Internacionais":
        return create_df_Relacoes_internacionais()
        
    elif option == "Bacharelado em Filosofia":
        return create_df_bach_filosofia()
        
    elif option == "Licenciatura em Biologia":
        return create_df_lic_biologia()
        
    elif option == "Licenciatura em Filosofia":
        return create_df_lic_em_filosofia()
        
    elif option == "Licenciatura em Química":
        return create_df_lic_em_quimica()
        
    elif option == "Licenciatura em Física":
        return create_df_lic_fisica()
        
    return  pd.DataFrame()

def app():
    st.header("Veja todas as matérias dos seus cursos de interesse")

    st.write("Quantas matérias pretende fazer?")
    optionQtdMaterias = ""
    optionQtdMaterias = st.selectbox('', ("", "1", "2"),
        key="option_1_unique_key1")

    if optionQtdMaterias != "":

        st.write("Escolha o curso Principal")
        
        df1 = df2 =pd.DataFrame()
         

        df1 = plano_pedagogico_1_materia(st.selectbox(
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
        ),
        key="option_2_unique_key"))

        if not df1.empty:
            if optionQtdMaterias == "2":
                st.write("Escolha a segunda matéria")
                df2 = plano_pedagogico_1_materia(st.selectbox(
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
                ),
                key="option_3_unique_key"))

            if not df2.empty or optionQtdMaterias == "1":
                if df2.empty:
                    df = df1
                else:
                    df = pd.concat([df1,df2],ignore_index=True)
                    df = df.drop_duplicates(['codigo'])
                

                filtro = (df['categoria'] == 'Obrigatória')
                creditos = df[filtro]['creditos'].sum()

                st.write(f"Total de créditos obrigatórios do curso: {creditos}")
                st.write(f"Conseguindo realizar 20 créditos por quad, demorará {np.round(creditos/60, 2)} anos para a conclusão de todas as matérias obrigatórias.")
                st.write("Obs.: Isso não inclui as Opções limitadas e livres.")
                st.write("Detalhes:")
                st.write(df.sort_values(by='categoria', ascending=True))

