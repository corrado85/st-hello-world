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

# Scarica i dati per il prezzo odierno
df_today = yf.download(tickers=symbol, start=today, end=today + timedelta(days=1))['Adj Close']

# Mostra il prezzo odierno di Bitcoin
st.write(f"Il prezzo di oggi di Bitcoin è {round(df_today.iloc[-1])}")

# Impostazioni iniziali per il grafico temporale
start_date = "2020-01-01"  # Data di inizio
end_date = date.today().strftime('%Y-%m-%d')  # Data di fine: oggi
interval = "1mo"  # Intervallo mensile

# Scarica i dati storici da Yahoo Finance
df_historical = yf.download(tickers=symbol, start=start_date, end=end_date, interval=interval)['Adj Close'].to_period('M')

# Converti il DataFrame in una forma adatta per il grafico
df_reset = df_historical.reset_index()  # Ripristina l'indice temporale in una colonna normale

# Usa la colonna 'Date' per l'asse X e 'Adj Close' per l'asse Y
st.line_chart(df_reset[['Date', 'Adj Close']].set_index('Date'))

# Visualizza il grafico su Streamlit con il titolo
st.title(f"Grafico Temporale dei Prezzi di {symbol}")
st.line_chart(df_historical)
