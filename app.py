import streamlit as st
from multiapp import MultiApp
from apps import home, sua_evolucao, plano_pedagogico

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Sua evolução", sua_evolucao.app)
app.add_app("Planos Pedagógicos", plano_pedagogico.app)

# The main app
app.run()