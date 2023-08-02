import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_livro, create_aprendendo

def app():
    st.title("Projeto Comana")
    # st.image(create_livro())
    st.image(create_aprendendo())
    st.divider()
    st.write("### Por estudantes da UFABC para estudantes da UFABC")
    st.write("Este é um projeto realizado na disciplina Engenharia Unificada I com o objetivo de aproveitar a oportunidade de criar uma visão estratégica sobre a grade curricular do aluno")
    st.write("Na aba Evolução, suba seu arquivo JSON disponibilizado no portal do aluno. Com isso, a plataforma conseguirá lhe retornar uma análise precisa sobre sua grade, assim como realizar sugestão de próximas disciplinas de acordo com sua grade de pós-BI.")
