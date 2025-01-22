import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Name: Majumder, Shayak</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Eintrittsdatum: 01.01.2025</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Name der Führungskraft: Soldner, Dennis</p>", unsafe_allow_html=True)
    
    # Additional Personal Information
    st.markdown("""
        <style>
        .personal-info {
            margin-top: 20px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            background-color: #f9f9f9;
        }
        .personal-info h2 {
            margin-top: 0;
        }
        .personal-info p {
            margin: 10px 0;
        }
        .personal-info ul {
            list-style-type: none;
            padding: 0;
        }
        .personal-info ul li {
            margin: 10px 0;
        }
        .emoji {
            font-size: 1.2em;
            margin-right: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="personal-info">
            <p>🏛️ When I am off-work, find me at:</p>
            <ul>
                <li>📚 <a href="https://www.terra-mineralia.de/" target="_blank">Terra Mineralia, Freiberg</a>: Mehrsprachiger Reiseleiter - Showcasing minerals, engaging guests 🌐.</li>
                <li>🌿 <a href="https://freiberg.nabu-sachsen.de/" target="_blank">Volunteer Support for NABU-Naturschutzstation Freiberg</a>: Environmental conservation activities.</li>
                <li>👨‍🏫 <a href="https://www.wbscodingschool.com/" target="_blank">Student Mentor & Coach at WBS Coding School Berlin</a>: Mentoring and coaching students.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Tasks Section
elif sections == "Aufgaben":
    st.header("Aufgaben")
    
    # Sample data for tasks and their distribution
    tasks = {
        'Task': [
            'Datenanalyse und -verarbeitung auf GeoDin, ArcGIS usw.',
            'Projektkoordination in-house mit Clemens Neupert, Daniel Kahsay',
            'Projektkoordination extern mit dem Team von UIT',
            'Projektkoordination in-company mit Gabriel Knorr',
            'Projektassistenzarbeit, In-Office Meetings usw.',
            'Mittagspausen-Diskussionen mit Sven Namyslik, Volker Ackermann, Michaela Pohle'
        ],
        'Importance': [5, 4, 3, 3, 2, 1],
        'Hours per Week': [20, 6, 5, 4, 3, 2]
    }

    # Convert the dictionary to a DataFrame
    df_tasks = pd.DataFrame(tasks)

    # Display the table of tasks and their distribution
    st.subheader('Table of Tasks and Their Distribution')
    st.table(df_tasks)

    # Display a heatmap of the task distribution
    st.subheader('Heatmap of Task Distribution')
    plt.figure(figsize=(6, 4))
    heatmap_data = df_tasks.pivot_table(index='Task', columns='Importance', values='Hours per Week')
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm')
    plt.title('Heatmap of Task Distribution')
    st.pyplot(plt)

# Project Works Section
elif sections == "Projektarbeiten":
    st.header("Projektarbeiten")
    
    # Project Work List Data
    project_work_list = [
        {"Projekt Nummer": "30071603", "Kategorie": "SL PA4_Monitoring_Phase 1.2 B3, C1 4610"},
        {"Projekt Nummer": "30071610", "Kategorie": "SL PA5_Monitoringkonzept Phase 1.2 C2, 4610"}
    ]
    
    # Tasks List Data with main section, sub sections and tasks under it
    tasks_list = [
        {"main_section": "GeoDin Arbeiten", 
         "tasks": [
             "Datenimport aus Monitoring Report, Excel Tabulation, Sorting, Datenlogger",
             "Datenimport aus SensorWeb, Excel Tabulation, Sorting, Datenlogger"
         ]},
        {"main_section": "GIS Arbeiten",
         "tasks": [
             "GIS Daten (z. B.: Trasse/Querungen, Baulosgrenzen usw.) bereitstellen"
         ]},
        {"main_section": "Monitoringbericht H2/24",
         "tasks": [
             "Arbeiten an Anlagen (Messpunkte Parameterganglinie, Deckblatten usw.) und Bericht"
         ]}
    ]
    
    # Convert project work list to DataFrame
    df_project_work = pd.DataFrame(project_work_list)
    
    # Display project work list in a table format
    st.subheader('Projektliste')
    st.table(df_project_work)
    
    # Display tasks list in a structured format with main section and sub sections
    st.subheader('Aufgabenliste')
    
    for section in tasks_list:
        st.markdown(f"**{section['main_section']}**")
        for task in section['tasks']:
            st.markdown(f"- {task}")

# Team Contributions Section
elif sections == "Teambeiträge":
    st.header("Teambeiträge")
    
    team_contributions = {
        'Contribution': [
            'Datenanalyse und -verarbeitung auf GeoDin, ArcGIS usw.',
            'Projektkoordination in-house mit Clemens Neupert, Daniel Kahsay',
            'Projektkoordination extern mit dem Team von UIT',
            'Projektkoordination in-company mit Gabriel Knorr',
            'Projektassistenzarbeit, In-Office Meetings usw.',
            'Mittagspausen-Diskussionen mit Sven Namyslik, Volker Ackermann, Michaela Pohle'
        ],
        'Percentage of Hours': [50, 15, 12.5, 10, 7.5, 5]
    }
    
    df_contributions = pd.DataFrame(team_contributions)
    
    # Sort the dataframe by percentage of hours in descending order
    df_contributions = df_contributions.sort_values(by='Percentage of Hours', ascending=False)
    
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.barh(df_contributions['Contribution'], df_contributions['Percentage of Hours'], color=bar_colors)
    ax.set_xlabel('Percentage of Hours')
    ax.set_title('Teambeiträge')
    
    # Add summary info table next to the graph in the same order as the graph
    summary_data = {
        'Contribution': df_contributions['Contribution'],
        'Percentage of Hours': df_contributions['Percentage of Hours']
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