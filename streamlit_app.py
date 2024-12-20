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

# Parametri
symbol = "BTC-USD"
today = date.today()
start_date = "2020-01-01"  # Data di inizio



# Scarica i dati per il prezzo odierno
df_today = yf.download(tickers=symbol, start=today, end=today + timedelta(days=1))['Adj Close']


# Mostra il prezzo odierno di Bitcoin
st.write("Il prezzo di oggi di Bitcoin è: ", round(df_today.iloc[-1,0]) )



# Scarica i dati storici da Yahoo Finance
df = yf.download(tickers=symbol, start=start_date, end=today, interval="1m")['Adj Close']


# Visualizza il grafico su Streamlit con il titolo
st.title(f"Grafico Temporale dei Prezzi di {symbol}")
st.line_chart(df)
