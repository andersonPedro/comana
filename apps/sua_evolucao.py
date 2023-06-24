import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO
from data.create_data import create_df_grade_horas, create_df_bacharelado_ciencia_tecnologia


def app():
    st.title('Sua evolução')

    uploaded_file = st.file_uploader(label="Colete o arquivo do seu portal do aluno em formato json e suba aqui.")

    if uploaded_file is not None:
        # Can be used wherevern a "file-like" object is accepted:
        df_ficha = pd.read_json(uploaded_file)
        st.write("Matérias já realizadas:")
        st.write(df_ficha)

        df_bacharelado_ciencia_tecnologia = create_df_bacharelado_ciencia_tecnologia()
        df_grade_horas = create_df_grade_horas()

        df_materias_faltantes = df_bacharelado_ciencia_tecnologia[~df_bacharelado_ciencia_tecnologia['codigo'].isin(df_ficha['codigo'])]

        ficha_soma_creditos_total = df_ficha[df_ficha["situacao"] == "Aprovado"]['creditos'].sum()
        grade_soma_creditos_total = df_grade_horas[df_grade_horas["categoria"] == "Carga horária total do curso"]["creditos"].sum()
        diferenca = grade_soma_creditos_total - ficha_soma_creditos_total
        percentual_progresso = round((ficha_soma_creditos_total / grade_soma_creditos_total) * 100, 2)

        st.write("Total de Créditos já realizados:", ficha_soma_creditos_total)
        st.write("Total de Créditos do curso:" ,grade_soma_creditos_total)
        st.write("Progresso:", percentual_progresso)
        st.write("Quantos créditos faltam:", diferenca)
