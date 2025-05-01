import streamlit as st
import requests

st.set_page_config(page_title="Universal Currency Converter", page_icon="💱", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            font-weight: bold;
        }
        .swap-btn {
            background-color: #4CAF50;
            border: none;
            border-radius: 50%;
            color: white;
            font-size: 20px;
            height: 50px;
            width: 50px;
            cursor: pointer;
        }
        .result-box {
            background-color: #d4edda;
            padding: 1em;
            border-radius: 10px;
            font-weight: bold;
            color: #155724;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>💱 Universal Currency Converter</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Convert between currencies with <b>live exchange rates</b> powered by <a href='https://www.frankfurter.app' target='_blank'>Frankfurter API</a>.</p>", unsafe_allow_html=True)

currencies = {
    'AUD': 'Australia - Australian Dollar',
    'BGN': 'Bulgaria - Bulgarian Lev',
    'BRL': 'Brazil - Brazilian Real',
    'CAD': 'Canada - Canadian Dollar',
    'CHF': 'Switzerland - Swiss Franc',
    'CNY': 'China - Yuan Renminbi',
    'CZK': 'Czech Republic - Czech Koruna',
    'DKK': 'Denmark - Danish Krone',
    'EUR': 'Eurozone - Euro',
    'GBP': 'United Kingdom - Pound Sterling',
    'HKD': 'Hong Kong - Hong Kong Dollar',
    'HRK': 'Croatia - Croatian Kuna',
    'HUF': 'Hungary - Hungarian Forint',
    'IDR': 'Indonesia - Rupiah',
    'ILS': 'Israel - New Shekel',
    'INR': 'India - Indian Rupee',
    'ISK': 'Iceland - Iceland Krona',
    'JPY': 'Japan - Yen',
    'KRW': 'South Korea - Won',
    'MXN': 'Mexico - Mexican Peso',
    'MYR': 'Malaysia - Malaysian Ringgit',
    'NOK': 'Norway - Norwegian Krone',
    'NZD': 'New Zealand - New Zealand Dollar',
    'PHP': 'Philippines - Peso',
    'PLN': 'Poland - Zloty',
    'RON': 'Romania - Romanian Leu',
    'RUB': 'Russia - Russian Ruble',
    'SEK': 'Sweden - Swedish Krona',
    'SGD': 'Singapore - Singapore Dollar',
    'THB': 'Thailand - Baht',
    'TRY': 'Turkey - Turkish Lira',
    'USD': 'United States - US Dollar',
    'ZAR': 'South Africa - Rand'
}

if "from_currency" not in st.session_state:
    st.session_state.from_currency = "USD"
if "to_currency" not in st.session_state:
    st.session_state.to_currency = "INR"

col1, col_swap, col2 = st.columns([5, 1, 5])
with col1:
    from_currency = st.selectbox("From Currency", options=list(currencies.keys()),
                                 index=list(currencies.keys()).index(st.session_state.from_currency),
                                 format_func=lambda x: f"{x} - {currencies[x]}")
with col2:
    to_currency = st.selectbox("To Currency", options=list(currencies.keys()),
                               index=list(currencies.keys()).index(st.session_state.to_currency),
                               format_func=lambda x: f"{x} - {currencies[x]}")
with col_swap:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄", help="Swap currencies"):
        st.session_state.from_currency, st.session_state.to_currency = (
            st.session_state.to_currency,
            st.session_state.from_currency
        )
        st.rerun()

st.session_state.from_currency = from_currency
st.session_state.to_currency = to_currency

amount = st.number_input("Amount to Convert", min_value=0.0, value=1.0, format="%.2f", step=1.0)

if st.button("💸 Convert"):
    if from_currency == to_currency:
        st.warning("Please select two different currencies.")
    else:
        try:
            url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
            response = requests.get(url)
            data = response.json()
            converted = data["rates"][to_currency]
            st.markdown(f"<div class='result-box'>💰 {amount:.2f} {from_currency} = {converted:.2f} {to_currency}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error during conversion: {e}")

st.markdown("---")
st.markdown("<p style='text-align: left;'>🚀 Built by Kshitiz ©</p>", unsafe_allow_html=True)