import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define Colors based on Arcadis rebranding
arcadis_colors = {
    "primary": "#F05A28",       # Bold Orange
    "accent": "#000000",        # Black
    "background": "#F5F5F5",    # Light Gray
    "text": "#333333"           # Dark Gray
}

# Define varying colors for the bar chart
bar_colors = ["#6A5ACD", "#4682B4", "#9ACD32", "#32CD32", "#FFD700", "#FF69B4"]

# Title and Introduction
st.set_page_config(page_title="Probezeit-Gespräch", page_icon=":clipboard:", layout="wide", initial_sidebar_state="expanded")
st.title("Probezeit-Gespräch nach 3 Monaten")
st.write("Übersicht : Leistungen und Fortschritte")

# Navigation Sidebar for Clickable Sections
st.sidebar.title("Navigation")
sections = st.sidebar.radio("Sections", ["Persönliche Informationen", "Aufgaben", "Projektarbeiten", "Teambeiträge", "Schulungen"])

# Personal Information Section
if sections == "Persönliche Informationen":
    st.header("Persönliche Informationen")
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'>Majumder, Shayak</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'>Eintrittsdatum: 01.01.2025</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'>Soldner, Dennis</p>", unsafe_allow_html=True)

# Tasks Section
elif sections == "Aufgaben":
    st.header("Aufgaben")
    tasks = st.text_area("Aufgaben:", "- Erstellung und Verwaltung von GeoDin-Datenbanken\n- Durchführung von GIS-Analysen mit ArcGIS\n- Erstellung von Karten und Berichten für verschiedene Projekte\n- Datenimport aus Monitoring Report, SensorWeb, Excel Tabulation, Sorting, Datenlogger\n- Teamarbeit mit Daniel, Diskussionen mit Clemens und Volker\n- Unterstützung der Projektassistenz mit Franziska, regelmäßige Updates mit Michaela\n- Projektorientierungsrunde mit Daniel für Gabriel Knorr (Halle Team) für GeoDin, GIS, WebGIS, Survey123-App, SENSOweb")

# Project Works Section
elif sections == "Projektarbeiten":
    st.header("Projektarbeiten")
    project_data = {
        "Projekt Nummer": ["30071603", "30071610"],
        "Kategorie": ["SL PA4_Monitoring_Phase 1.2 B3, C1 4610", "SL PA5_Monitoringkonzept Phase 1.2 C2, 4610"],
        "Aufgabenknoten": ["PA4 – 30071603\nSL_PA4_AP Monitoring Phase 2.0 Los 1 B3_0621 13010\nSL_PA4_AP Monitoring Phase 2.0 Los 2 C1_0622 14020",
                           "PA5 – 30071610\nSL_PA5_AP Monitoring Phase 2.0 Los 3 C2_0623 13010\nSL_PA5_AP Monitoring Phase 2.0 Los 4 C2_0624 14020"]
    }
    df = pd.DataFrame(project_data)
    st.table(df)

# Team Contributions Section
elif sections == "Teambeiträge":
    st.header("Teambeiträge")
    team_contributions = {
        'Contribution': [
            'Datenanalyse und -verarbeitung auf GeoDin, ArcGIS usw.',
            'Projektkoordination in-house mit Clemens Neupert, Daniel Kahsay',
            'Projektkoordination in-company mit Gabriel Knorr',
            'Projektkoordination extern mit dem Team von UIT',
            'Projektassistenzarbeit, In-Office Meetings usw.',
            'Mittagspausen-Diskussionen mit Sven Namyslik, Volker Ackermann, Michaela Pohle'
        ],
        'Frequency': [15, 12, 10, 8, 6, 4]
    }
    df_contributions = pd.DataFrame(team_contributions)
    
    # Sort the dataframe by frequency in descending order
    df_contributions = df_contributions.sort_values(by='Frequency', ascending=False)
    
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.barh(df_contributions['Contribution'], df_contributions['Frequency'], color=bar_colors)
    ax.set_xlabel('Häufigkeit')
    ax.set_title('Teambeiträge')
    
    # Add summary info table next to the graph
    summary_data = {
        'Contribution': df_contributions['Contribution'],
        'Frequency': df_contributions['Frequency']
    }
    df_summary = pd.DataFrame(summary_data)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.pyplot(fig)
    
    with col2:
        st.table(df_summary)

# Trainings Section
elif sections == "Schulungen":
    st.header("Schulungen")
    
    # Onboarding Trainings
    onboarding_trainings = {
        'Schulung': ['GeoDin', 'Gesundheit & Sicherheit', 'Virtuelles Onboarding', 'Thema Marketing'],
        'Status': ['Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen']
    }
    df_onboarding = pd.DataFrame(onboarding_trainings)
    
    # Work Project Trainings
    work_project_trainings = {
        'Schulung': ['SLPS_PA4_PA5 MA Einführung', 'SLPS_PA4_5 Workshop Ersteller', 'Projekt SuedLink obligatorische Datenschutzschulung'],
        'Status': ['Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen']
    }
    df_work_project = pd.DataFrame(work_project_trainings)
    
    st.subheader("Onboarding-Schulungen")
    st.table(df_onboarding)
    
    st.subheader("Projektbezogene Schulungen")
    st.table(df_work_project)