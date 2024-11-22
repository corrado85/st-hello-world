import streamlit as st

# Titolo dell'applicazione
st.title("Calcolo del Quadrato di un Numero")

# Input dell'utente: numero intero
numero = st.number_input("Inserisci un numero", value=0)

# Calcolo del quadrato del numero
quadrato = numero ** 2

# Visualizzazione del risultato
st.write(f"Il quadrato di {numero} è {quadrato}")


import yfinance as yf
from datetime import date, timedelta

today = date.today()
df = yf.download(tickers=symbol, start=today, end=today + timedelta(days=1))['Adj Close']


st.write(f"\n\nIl prezzo di bitcoin oggi è{df}")
