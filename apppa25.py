import streamlit as st

# Define Colors based on Arcadis rebranding
arcadis_colors = {
    "primary": "#F05A28",       # Bold Orange
    "accent": "#000000",        # Black
    "background": "#F5F5F5",    # Light Gray
    "text": "#333333"           # Dark Gray
}

# Title and Introduction
st.set_page_config(page_title="Probezeit-Gespräch", page_icon=":clipboard:", layout="wide", initial_sidebar_state="expanded")
st.title("Probezeit-Gespräch nach 3 Monaten")
st.write("Hier ist eine Übersicht Ihrer Leistungen und Fortschritte während der Probezeit.")

# Navigation Sidebar for Clickable Sections
st.sidebar.title("Navigation")
sections = st.sidebar.radio("Sections", ["Persönliche Informationen", "Aufgaben und Erfolge", "Projektarbeiten", "Teambeiträge", "Schulungen"])

# Personal Information Section
if sections == "Persönliche Informationen":
    st.header("Persönliche Informationen")
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'>**Name:** Vorname</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'>**Eintrittsdatum:**</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'>**Name der Führungskraft:**</p>", unsafe_allow_html=True)

# Tasks and Achievements Section
elif sections == "Aufgaben und Erfolge":
    st.header("Aufgaben und Erfolge")
    tasks = st.text_area("Aufgaben:", "- Erstellung und Verwaltung von GeoDin-Datenbanken\n- Durchführung von GIS-Analysen mit ArcGIS\n- Erstellung von Karten und Berichten für verschiedene Projekte\n- Datenimport aus Monitoring Report, SensorWeb, Excel Tabulation, Sorting, Datenlogger\n- Teamarbeit mit Daniel, Diskussionen mit Clemens und Volker\n- Unterstützung der Projektassistenz mit Franziska, regelmäßige Updates mit Michaela\n- Projektorientierungsrunde mit Daniel für Gabriel Knorr (Halle Team) für GeoDin, GIS, WebGIS, Survey123-App, SENSOweb")

# Project Works Section
elif sections == "Projektarbeiten":
    st.header("Projektarbeiten")
    project_data = [
        {"Projekt Nummer": "30071603", "Kategorie": "SL PA4_Monitoring_Phase 1.2 B3, C1 4610", "Aufgabenknoten": "PA4 – 30071603\nSL_PA4_AP Monitoring Phase 2.0 Los 1 B3_0621 13010\nSL_PA4_AP Monitoring Phase 2.0 Los 2 C1_0622 14020"},
        {"Projekt Nummer": "30071610", "Kategorie": "SL PA5_Monitoringkonzept Phase 1.2 C2, 4610", "Aufgabenknoten": "PA5 – 30071610\nSL_PA5_AP Monitoring Phase 2.0 Los 3 C2_0623 13010\nSL_PA5_AP Monitoring Phase 2.0 Los 4 C2_0624 14020"}
    ]
    for project in project_data:
        st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'><strong>Projekt Nummer:</strong> {project['Projekt Nummer']}</p>", unsafe_allow_html=True)
        st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'><strong>Kategorie:</strong> {project['Kategorie']}</p>", unsafe_allow_html=True)
        st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'><strong>Aufgabenknoten:</strong> {project['Aufgabenknoten']}</p>", unsafe_allow_html=True)

# Team Contributions Section
elif sections == "Teambeiträge":
    st.header("Teambeiträge")
    team_contributions = st.text_area("Teambeiträge:", "- Zusammenarbeit mit Daniel bei der Datenanalyse\n- Regelmäßige Diskussionen mit Clemens und Volker zur Projektkoordination\n- Unterstützung der Projektassistenz mit Franziska\n- Regelmäßige Updates und Diskussionen mit Michaela während der Mittagspause")

# Trainings Section
elif sections == "Schulungen":
    st.header("Schulungen")
    st.write("Hier sind die Schulungen, an denen Sie teilgenommen haben:")

    # Onboarding Trainings
    st.subheader("Onboarding-Schulungen")
    onboarding_trainings = st.text_area("Onboarding-Schulungen:", "- GeoDin\n- Health & Safety\n- Virtual Onboarding\n- Thema Marketing")

    # Work Project Trainings
    st.subheader("Projektbezogene Schulungen")
    work_project_trainings = st.text_area("Projektbezogene Schulungen:", "- SLPS_PA4_PA5 MA Einführung\n- SLPS_PA4_5 Workshop Ersteller\n- Projekt SuedLink obligatorische Datenschutzschulung")