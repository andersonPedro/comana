import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO
from data.create_data import create_df_grade_horas, create_df_bacharelado_ciencia_tecnologia


def app():
    st.title('Sua evolução')

    materias_ja_desenvolvidas = [""]

    uploaded_file = st.file_uploader(label="Colete o arquivo do seu portal do aluno em formato json e suba aqui.")

    if uploaded_file is not None:
        # Can be used wherevern a "file-like" object is accepted:
        
        df_ficha = pd.read_json(uploaded_file)
        df_ficha["ano"] = df_ficha["ano"].astype(str).replace(",", "")
        
        df_bacharelado_ciencia_tecnologia = create_df_bacharelado_ciencia_tecnologia()
        
        df_grade_horas = create_df_grade_horas()
        
        st.write("### Bacharelado em Ciência e Tecnologia")
        
        df_materias_aprovadas = df_ficha[df_ficha["situacao"] == "Aprovado"].copy()
        
        ficha_soma_creditos_total = df_materias_aprovadas['creditos'].sum()
        grade_soma_creditos_total = df_grade_horas[df_grade_horas["categoria"] == "Carga horária total do curso"]["creditos"].sum()
        
        diferenca = grade_soma_creditos_total - ficha_soma_creditos_total
        
        percentual_progresso = round((ficha_soma_creditos_total / grade_soma_creditos_total), 3)
        
        df_visao_historica = df_materias_aprovadas[["ano", "periodo", "creditos"]].copy()
        df_visao_historica = df_visao_historica.groupby(by=["ano", "periodo"], as_index=False).sum()
        df_visao_historica["ano-periodo"] = df_visao_historica["ano"].astype(str) + "-" + df_visao_historica["periodo"].astype(str).str.zfill(2)
        df_visao_historica = df_visao_historica[["ano-periodo", "creditos"]]
        
        df_materias_faltantes = df_bacharelado_ciencia_tecnologia[~df_bacharelado_ciencia_tecnologia['codigo'].isin(df_ficha['codigo'])].copy()

        ficha_conceitoxcreditos = 0
        dict_conceitos = {
            "A": 4,
            "B": 3,
            "C": 2,
            "D": 1,
            "F": 0,
            "O": 0
        }

        # Mapear os valores de "conceito" para os valores numéricos correspondentes
        df_ficha['conceito_num'] = df_ficha['conceito'].map(dict_conceitos)

        # Calcular a média ponderada
        cr = round((df_ficha['creditos'] * df_ficha['conceito_num']).sum() / df_ficha['creditos'].sum(), 3)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Coeficiente de progressão (CP)", percentual_progresso)
        col2.metric("Coeficiente de Rendimento (CR)", cr)
        col3.metric("Total de créditos realizados", ficha_soma_creditos_total)
        col4.metric("Quantos créditos faltam", diferenca)
    
        
        st.write("Matérias já realizadas:")
        st.write(df_ficha)

        
        st.write("Créditos por Quadrimestre")
        tab1, tab2 = st.tabs(["Gráfico", "Dados"])
        tab1.bar_chart(df_visao_historica, x="ano-periodo", y="creditos")
        tab2.write(df_visao_historica)
        
        st.write("Lista de Matérias que ainda podem ser feitas:")
        st.write(df_materias_faltantes)
        
        option = st.selectbox(
            'Qual seu pós-BI',
            (
                "",
                "Bacharelado de Biotecnologia",
                "Bacharelado de Ciência da Computação",
                "Bacharelado de Ciências Biológicas",
                "Bacharelado de Física",
                "Bacharelado de Matemática",
                "Bacharelado de Química",
                "Bacharelado de Neurociência",
                "Engenharia de Ambiental e Urbana",
                "Engenharia de Energia",
                "Engenharia de Informação",
                "Engenharia de Instrumentação",
                "Automação e Robótica",
                "Engenharia de Materiais",
                "Engenharia de Aeroespacial",
                "Engenharia de Biomédica",
                "Engenharia de Gestão"
            ))
        

        if option in materias_ja_desenvolvidas:
            pass
        else:
            st.write("Em desenvolvimento")
