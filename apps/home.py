import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_df_grade_horas, create_df_bacharelado_ciencia_tecnologia

def app():
    st.write("## Projeto Comana")
    st.write("Veja o quanto ainda falta para você se formar")
   
    st.divider()
    st.write("##### Grade de Horas do Bacharelado em Ciencia e Tecnologia")
    df_grade_horas = create_df_grade_horas()
    st.write(df_grade_horas)
    st.divider()

    st.write("##### Matérias do Bacharelado em Ciencia e Tecnologia")
    df_bacharelado_ciencia_tecnologia = create_df_bacharelado_ciencia_tecnologia()
    st.write(df_bacharelado_ciencia_tecnologia)
    st.divider()



    st.write('Engenharia Unificada')


