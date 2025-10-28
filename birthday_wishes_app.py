# birthday_wishes_app.py
import streamlit as st
import pandas as pd
from datetime import datetime
import os
import fitz  # PyMuPDF

# File to store wishes
FILE_NAME = "birthday_wishes.csv"

# Default message from The Dev Team
default_message = {
    "Name": "The Dev Team",
    "Wish": (
        "💻 Wishing you a bug-free year ahead, filled with clean commits, zero merge conflicts, "
        "and infinite loops of happiness. May your birthday be as optimized as your favorite algorithm "
        "and as joyful as a successful Friday deployment! 🎂🎈\n\n"
        "🧠 Alles Gute zum Geburtstag! Möge dein neues Lebensjahr frei von Bugs, voller sauberer Commits "
        "und ohne Merge-Konflikte sein. Möge dein Code kompiliert, deine Tests bestehen und dein Glück "
        "unendlich rekursiv sein! 🎉👩‍💻"
    ),
    "Timestamp": datetime.now().strftime("%d-%m-%Y %H:%M")
}

# Initialize storage and insert default message only if file is empty
if not os.path.exists(FILE_NAME):
    pd.DataFrame([default_message]).to_csv(FILE_NAME, index=False)
else:
    existing_data = pd.read_csv(FILE_NAME)
    if existing_data.empty:
        pd.DataFrame([default_message]).to_csv(FILE_NAME, index=False)

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

# Filter out test entries
filtered_data = data[~((data["Name"].str.lower() == "test") & (data["Wish"].str.lower() == "test"))]

if not filtered_data.empty:
    for _, row in filtered_data.iterrows():
        st.markdown(f"**{row['Name']}** ({row['Timestamp']}):")
        st.write(f"{row['Wish']}")
        st.write("---")
else:
    st.info("No wishes yet. Be the first to send one! / Noch keine Wünsche. Seien Sie der Erste!")

# Download all wishes as text
if not filtered_data.empty:
    wishes_text = "\n\n".join([f"{row['Name']}:\n{row['Wish']}" for _, row in filtered_data.iterrows()])
    st.download_button("Download All Wishes / Alle Wünsche herunterladen",
                       wishes_text, file_name="birthday_wishes.txt")

# Greeting card generation (PDF) using PyMuPDF
if st.button("Generate Greeting Card / Grußkarte erstellen"):
    doc = fitz.open()
    page = doc.new_page()

    # Optional background image
    background_path = "background.jpg"
    if os.path.exists(background_path):
        rect = fitz.Rect(0, 0, page.rect.width, page.rect.height)
        page.insert_image(rect, filename=background_path)

    # Starting position
    x, y = 50, 50
    line_height = 20

    # Title
    page.insert_text((x, y), "Happy 50th Birthday!", fontsize=16, fontname="helv", fill=(0, 0, 0))
    y += line_height * 2

    # Add each wish
    for _, row in filtered_data.iterrows():
        message = f"{row['Name']} ({row['Timestamp']}):\n{row['Wish']}\n"
        for line in message.split('\n'):
            page.insert_text((x, y), line, fontsize=12, fontname="helv", fill=(0, 0, 0))
            y += line_height
            if y > page.rect.height - 50:
                page = doc.new_page()
                y = 50

    # Save PDF
    pdf_path = "greeting_card.pdf"
    doc.save(pdf_path)

    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    st.download_button("📥 Download Greeting Card / Grußkarte herunterladen",
                       data=pdf_bytes,
                       file_name="greeting_card.pdf",
                       mime="application/pdf")