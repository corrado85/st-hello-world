import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Report Interattivo con Streamlit')

# Controlli utente
valore = st.sidebar.slider('Seleziona un valore', 0, 100, 50)
opzione = st.sidebar.selectbox('Seleziona una colonna', ['colonna1', 'colonna2', 'colonna3'])

# Calcoli
risultato = valore * 2
st.write(f'Il doppio di {valore} è {risultato}')

# Grafico interattivo
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
y = np.sin(x) * valore
ax.plot(x, y)
st.pyplot(fig)
