import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import google.generativeai as genai
import requests

# -----------------------
# Google Sheets Connection
# -----------------------

genai.configure(api_key=st.secrets["genai"]["api_key"])

model = genai.GenerativeModel("gemini-2.5-pro")

def get_gemini_response(question):
    response =  model.generate_content(question)
    return response.text.strip()

def connect_gsheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    # Load credentials from Streamlit secrets.toml
    creds_dict = st.secrets["google_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), scope)
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).worksheet("Holdings")
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return sheet, df

def clear_input():
    st.session_state["asset_id"] = ""
    st.session_state["asset_type"] = "Stock"
    st.session_state["asset_name"] = ""
    st.session_state["buy_date"] = None
    st.session_state["buy_price"] = 0.0
    st.session_state["units"] = 0.0
    st.session_state["current_price"] = 0.0
    st.session_state["currency"] = "INR"
    st.session_state["notes"] = ""

def get_usd_to_inr():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']['INR']

def total_invest(df):
    if df.empty:
        return 0.0
    sum = (df['Current Price'] * df['Units']).sum()
    return get_usd_to_inr()*sum



# -----------------------
# Streamlit UI
# -----------------------
st.set_page_config(page_title="Portfolio Holdings", layout="wide")
st.sidebar.success("Select Any page")
st.title("📊 Portfolio Holdings Manager")

# Connect to Google Sheet
SHEET_NAME = "PortfolioTracker"   # Replace with your Google Sheet name
sheet, df = connect_gsheet(SHEET_NAME)

# Show Current Holdings
st.subheader("Current Holdings")
if not df.empty:
    df_display = df.copy()
    df_display.index = df_display.index + 2  # Match Google Sheet row numbers (header = 1)
    st.metric(label="💰 Total Investment (INR)", value=total_invest(df))
    st.dataframe(df_display)
else:
    st.info("No holdings found.")


# -----------------------
# Add Holding Section
# -----------------------
with st.expander("➕ Add New Holding"):
    with st.form("add_holding"):
        col1, col2, col3 = st.columns(3)

        with col1:
            asset_id = st.text_input("Asset ID")
            asset_type = st.selectbox("Asset Type", ["US Stocks","Stock", "MutualFund", "Smallcase", "Other"])
            asset_name = st.text_input("Asset Name")

        with col2:
            buy_date = st.date_input("Buy Date")
            buy_price = st.number_input("Buy Price", min_value=0.0, step=0.01)
            units = st.number_input("Units", min_value=0.0, step=0.01)

        with col3:
            current_price = st.number_input("Current Price", min_value=0.0, step=0.01)
            currency = st.selectbox("Currency", ["INR", "USD"])
            notes = st.text_area("Notes")

        submitted = st.form_submit_button("Save Holding")

        if submitted:
            new_row = [asset_id, asset_type, asset_name, str(buy_date),
                       buy_price, units, current_price, currency, notes]
            sheet.append_row(new_row)
            st.success("✅ Holding added successfully!")
            st.rerun()


# -----------------------
# Delete Holding Section (By Row Index)
# -----------------------
with st.expander("🗑 Remove Holding"):
    st.write("Select a **row number** to delete that record permanently.")
    
    if not df.empty:
        df_display = df.copy()
        df_display.index = df_display.index + 2  # Google Sheet row numbers
        row_numbers = df_display.index.tolist()

        selected_row = st.selectbox("Select Row to Delete", row_numbers)

        # Preview the row before deletion
        st.dataframe(df_display.loc[[selected_row]])

        if st.button("Delete Selected Row"):
            try:
                sheet.delete_rows(selected_row)
                st.success(f"✅ Row {selected_row} deleted successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error deleting row: {e}")
    else:
        st.info("No holdings available to delete.")
