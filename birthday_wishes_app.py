# birthday_wishes_app.py
import streamlit as st
import pandas as pd
from datetime import datetime
import os
from fpdf import FPDF

# File to store wishes
FILE_NAME = "birthday_wishes.csv"

# Initialize storage
if not os.path.exists(FILE_NAME):
    pd.DataFrame(columns=["Name", "Wish", "Timestamp"]).to_csv(FILE_NAME, index=False)

# Title
st.title("Happy 50th Birthday / Alles Gute zum 50. Geburtstag")
st.write("Leave your wishes for our line manager's milestone birthday! / "
         "Hinterlassen Sie Ihre Wünsche zum runden Geburtstag unserer Linienmanagerin!")

# Form for input
with st.form("wish_form"):
    name = st.text_input("Your Name / Ihr Name")
    wish = st.text_area("Your Birthday Wish / Ihr Geburtstagswunsch")
    submitted = st.form_submit_button("Submit Wish / Wunsch absenden")

    if submitted and name.strip() and wish.strip():
        new_entry = pd.DataFrame([[name, wish, datetime.now().strftime("%d-%m-%Y %H:%M")]],
                                 columns=["Name", "Wish", "Timestamp"])
        existing = pd.read_csv(FILE_NAME)
        updated = pd.concat([existing, new_entry], ignore_index=True)
        updated.to_csv(FILE_NAME, index=False)
        st.success("Your wish has been added! / Ihr Wunsch wurde hinzugefügt!")

# Display wishes
st.subheader("Collected Wishes / Gesammelte Wünsche")
data = pd.read_csv(FILE_NAME)
if not data.empty:
    for _, row in data.iterrows():
        st.markdown(f"**{row['Name']}** ({row['Timestamp']}):")
        st.write(f"{row['Wish']}")
        st.write("---")
else:
    st.info("No wishes yet. Be the first to send one! / Noch keine Wünsche. Seien Sie der Erste!")

# Download all wishes
if not data.empty:
    wishes_text = "\n\n".join([f"{row['Name']}:\n{row['Wish']}" for _, row in data.iterrows()])
    st.download_button("Download All Wishes / Alle Wünsche herunterladen",
                       wishes_text, file_name="birthday_wishes.txt")

# Greeting card generation (PDF)
if st.button("Generate Greeting Card / Grußkarte erstellen"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Happy 50th Birthday!", ln=True, align="C")
    pdf.ln(10)
    for _, row in data.iterrows():
        pdf.multi_cell(0, 10, f"{row['Name']}:\n{row['Wish']}\n", align="L")
    pdf.output("greeting_card.pdf")
    st.success("Greeting card generated! Check greeting_card.pdf")