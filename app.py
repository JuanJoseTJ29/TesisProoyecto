import streamlit as st
from multiapp import MultiApp
from apps import home, model #, model1 # import your app modules here

app = MultiApp()

st.markdown("""
#  Inteligencia de Negocios - Grupo 6

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Dolares", model.app)
#app.add_app("Euros", model1.app)
# The main app
app.run()



