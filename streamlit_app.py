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
st.write(f"Il prezzo di oggi di bitcoing è {round(df.iloc[-1,0])}")





# Impostazioni iniziali
start_date = "2020-01-01"  # Data di inizio
end_date = date.today().strftime('%Y-%m-%d')  # Data di fine: oggi
interval = "1mo"  # Intervallo mensile

# Scarica i dati da Yahoo Finance
df = yf.download(tickers=symbol, start=start_date, end=end_date, interval=interval)['Adj Close'].to_period('M')




# Converti il DataFrame in una forma adatta per il grafico
df_reset = df.reset_index()  # Ripristina l'indice temporale in una colonna normale

# Usa la colonna 'Date' per l'asse X e 'Adj Close' per l'asse Y
st.line_chart(df_reset[['Date', 'Adj Close']].set_index('Date'))





# Visualizza il grafico su Streamlit
st.title(f"Grafico Temporale dei Prezzi di {symbol}")
st.line_chart(df)






