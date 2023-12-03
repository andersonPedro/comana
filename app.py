import streamlit as st
from multiapp import MultiApp
from apps import home, sua_evolucao

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Sua evolução", sua_evolucao.app)

# The main app
app.run()