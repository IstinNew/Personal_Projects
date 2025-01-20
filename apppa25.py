import streamlit as st

# Title and Introduction
st.title("Probezeit-Gespräch nach 3 Monaten")
st.write("Hier ist eine Übersicht Ihrer Leistungen und Fortschritte während der Probezeit.")

# Personal Information
st.header("Persönliche Informationen")
st.write("**Name:** Vorname")
st.write("**Eintrittsdatum:**")
st.write("**Name der Führungskraft:**")

# Tasks and Achievements
st.header("Aufgaben und Erfolge")
st.write("Der/die Mitarbeiter/in hat sich in folgende Aufgaben bereits erfolgreich eingearbeitet:")
tasks = st.text_area("Aufgaben:", "- Erstellung und Verwaltung von GeoDin-Datenbanken\n- Durchführung von GIS-Analysen mit ArcGIS\n- Erstellung von Karten und Berichten für verschiedene Projekte\n- Datenimport aus Monitoring Report, SensorWeb, Excel Tabulation, Sorting, Datenlogger\n- Teamarbeit mit Daniel, Diskussionen mit Clemens und Volker\n- Unterstützung der Projektassistenz mit Franziska, regelmäßige Updates mit Michaela\n- Projektorientierungsrunde mit Daniel für Gabriel Knorr (Halle Team) für GeoDin, GIS, WebGIS, Survey123-App, SENSOweb")

# Project Works
st.header("Projektarbeiten")
st.write("Hier sind die Details zu den Projekten, an denen Sie gearbeitet haben:")

project_data = [
    {"Projekt Nummer": "30071603", "Kategorie": "SL PA4_Monitoring_Phase 1.2 B3, C1 4610", "Aufgabenknoten": "PA4 – 30071603\nSL_PA4_AP Monitoring Phase 2.0 Los 1 B3_0621 13010\nSL_PA4_AP Monitoring Phase 2.0 Los 2 C1_0622 14020"},
    {"Projekt Nummer": "30071610", "Kategorie": "SL PA5_Monitoringkonzept Phase 1.2 C2, 4610", "Aufgabenknoten": "PA5 – 30071610\nSL_PA5_AP Monitoring Phase 2.0 Los 3 C2_0623 13010\nSL_PA5_AP Monitoring Phase 2.0 Los 4 C2_0624 14020"}
]

for project in project_data:
    st.write(f"**Projekt Nummer:** {project['Projekt Nummer']}")
    st.write(f"**Kategorie:** {project['Kategorie']}")
    st.write(f"**Aufgabenknoten:** {project['Aufgabenknoten']}") 

# Team Contributions
st.header("Teambeiträge")
st.write("Hier sind die Beiträge des Mitarbeiters/der Mitarbeiterin zum Team:")
team_contributions = st.text_area("Teambeiträge:", "- Zusammenarbeit mit Daniel bei der Datenanalyse\n- Regelmäßige Diskussionen mit Clemens und Volker zur Projektkoordination\n- Unterstützung der Projektassistenz mit Franziska\n- Regelmäßige Updates und Diskussionen mit Michaela während der Mittagspause")

# Trainings
st.header("Schulungen")
st.write("Hier sind die Schulungen, an denen Sie teilgenommen haben:")

# Onboarding Trainings
st.subheader("Onboarding-Schulungen")
onboarding_trainings = st.text_area("Onboarding-Schulungen:", "- GeoDin\n- Health & Safety\n- Virtual Onboarding\n- Thema Marketing")

# Work Project Trainings
st.subheader("Projektbezogene Schulungen")
work_project_trainings = st.text_area("Projektbezogene Schulungen:", "- SLPS_PA4_PA5 MA Einführung\n- SLPS_PA4_5 Workshop Ersteller\n- Projekt SuedLink obligatorische Datenschutzschulung")
