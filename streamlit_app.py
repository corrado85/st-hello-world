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
import streamlit as st

# Simbolo del ticker
symbol = "BTC-USD"

# Data odierna
today = date.today()

# Scarica i dati
df = yf.download(tickers=symbol, start=today, end=today + timedelta(days=1))['Adj Close']

# Mostra il risultato su Streamlit
if not df.empty:
    st.write(f"Il prezzo di Bitcoin oggi è: {df.iloc[-1]:.2f} USD")
else:
    st.write("Nessun dato disponibile per oggi. Potrebbe essere un giorno festivo o il mercato è chiuso.")


