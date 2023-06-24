import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO


def app():
    st.title('Sua evolução')

    uploaded_file = st.file_uploader(label="Colete o arquivo do seu portal do aluno em formato json e suba aqui.")

    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)