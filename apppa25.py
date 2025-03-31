import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import plotly.express as px 

# Define Colors based on Arcadis Marketing Theme
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
sections = st.sidebar.radio("Sections", ["Persönliche Informationen", "Aufgaben", "Projektarbeiten", "Nutzung von Data Science", "Teambeiträge", "Schulungen"])

# Personal Information Section
if sections == "Persönliche Informationen":
    st.header("Persönliche Informationen")
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Name: Majumder, Shayak</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Eintrittsdatum: 01.01.2025</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Name der Führungskraft: Soldner, Dennis</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Arbeitsort: Freiberg (Sachs)</p>", unsafe_allow_html=True) 
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Business Unit: Resilience</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> Affinity Group: Ethinicity & Heritage</p>", unsafe_allow_html=True)
    st.write(f"<p style='color: {arcadis_colors['text']}; font-size: 18px;'> freiwillige Unterstützer: Wintercup 2025</p>", unsafe_allow_html=True)
    
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
if sections == "Aufgaben":
    st.header("Aufgaben")
    
    # Sample data for tasks and their distribution
    tasks = {
        'Task': [
            'Datenanalyse und -verarbeitung auf GeoDin, ArcGIS usw.',
            'Projektkoordination in-house mit Clemens Neupert, Daniel Kahsay',
            'Projektkoordination extern mit dem Team von UIT, Eurofins ',
            'Projektkoordination in-company mit Gabriel Knorr',
            'Projektassistenzarbeit, In-Office Meetings usw.',
            'Mittagspausen-Diskussionen mit Sven Namyslik, Volker Ackermann, Michaela Pohle'
        ],
        'Importance': [5, 4, 3, 3, 2, 1],
        'Hours per Week': [20, 6, 5, 4, 3, 2]
    }

    # Convert the dictionary to a DataFrame
    df_tasks = pd.DataFrame(tasks)
    
    # Adjust the index to start from 1 instead of 0
    df_tasks.index = df_tasks.index + 1

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
    
    # Convert project work list to DataFrame
    df_project_work = pd.DataFrame(project_work_list)
    
    # Adjust the index to start from 1 instead of 0
    df_project_work.index = df_project_work.index + 1

    # Display project work list in a table format
    st.subheader('Projektliste')
    st.table(df_project_work)
    
    # Tasks List Data with main section, short list of tasks, and full list of tasks
    tasks_list = [
        {"main_section": "GeoDin Arbeiten", 
         "short_list": [
             "Datenimport und Verarbeitung von Monitoring-Daten",
             "Erstellung, Archivierung und Pflege von Datenbanken"
         ],
         "full_list": [
             "Datenimport und Verarbeitung von Monitoring-Daten",
             "Erstellung und Pflege von Datenbanken",
             "Analyse von Wasserstandsdaten",
             "Erstellung von Berichten und Visualisierungen"
         ]},
        {"main_section": "GIS Arbeiten",
         "short_list": [
             "GIS Daten bereitstellen",
             "Arbeiten mit Feature Classes"
         ],
         "full_list": [
             "GIS Daten bereitstellen",
             "Arbeiten mit Feature Classes",
             "Verwendung von Shapefiles",
             "Erstellung und Bearbeitung von Karten",
             "Analyse und Visualisierung von GIS-Daten"
         ]},
        {"main_section": "Projektbezogene Aufgaben Jan - Mar 2025",
         "short_list": [
             "Project Calendar Coordination (SuedLink Grundwassermonitoring Baulose 3 bis 4)"
             "Arbeiten an Anlagen",
             "Vorbereitung von Ortsterminen",
             "Mitwirkung an Konzepten, Stellungnahmen",             
             "Monitoringbericht erstellen",
             "Einsatz von Data-Science-Techniken zur Sortierung, Filterung und Automatisierung der Verwaltung einer komplexen GeoDin-Datenbank, um die Datengenauigkeit und Effizienz zu verbessern."
         ],
         "full_list": [
             "Projektkalenderkoordination (SuedLink Grundwassermonitoring Baulose 3 bis 4), einschließlich der Planung und Überwachung von Terminen, Ressourcen und Meilensteinen",             
             "Arbeiten an Anlagen (Messpunkte Parameterganglinie, Deckblatten usw.) und Bericht",
             "Vorbereitung von Ortsterminen",
             "Mitwirkung an Konzepten, Stellungnahmen",
             "Zusammenstellung von verfügbaren Informationen",
             "Entwicklung von Monitoringkonzepten",
             "Koordination mit Drittanbietern",
             "Monitoringbericht erstellen und analysieren",
             "Anwendung fortschrittlicher Data-Science-Methoden zur Optimierung von GeoDin- und MS-Office-Workflows, um eine nahtlose Datenintegration und -verarbeitung zu gewährleisten.",
             "Unterstützung bei der Analyse von Berichten durch automatisierte Datenverarbeitung und Visualisierung.",
             "Verbesserung der Berichtsgenauigkeit durch detaillierte Datenanalyse und Mustererkennung."
            ]}
    ]
    
    # Display tasks list in a structured format with main section and short list of tasks
    st.subheader('Aufgabenliste')
    
    for section in tasks_list:
        st.markdown(f"**{section['main_section']}**")
        
        # Display short list of tasks
        for task in section['short_list']:
            st.markdown(f"- {task}") 
        
        # Add a dropdown filter to show the full list of tasks
        if st.checkbox(f"Show all tasks for {section['main_section']}"):
            for task in section['full_list']:
                st.markdown(f"  - {task}")


# Data Science Usage Section
elif sections == "Nutzung von Data Science":
    st.header("Nutzung von Data Science")

    # Display data protection message and checkbox
    agree = st.checkbox("**Note:** Zum Schutz der Daten wurden die genauen Stationsnamen, Standorte und Koordinaten in der Excel-Tabelle geändert. Ich stimme zu.")

    if agree:
        # File Upload
        uploaded_file = st.file_uploader("Laden Sie Ihre GeoDin Excel-Datei hoch", type=["xlsx"])

        if uploaded_file is not None:
            # Load Excel sheets into DataFrames
            s3stamm = pd.read_excel(uploaded_file, sheet_name='GEODIN_LOC_S3STAMM', engine='openpyxl')
            gwatab01 = pd.read_excel(uploaded_file, sheet_name='GEODIN_MES_GWATAB01', engine='openpyxl')
            
            # Convert date columns to datetime format
            s3stamm['DATUM'] = pd.to_datetime(s3stamm['DATUM'], format='%d.%m.%Y %H:%M:%S', errors='coerce')
            gwatab01['SMPDATE'] = pd.to_datetime(gwatab01['SMPDATE'], format='%d.%m.%Y %H:%M:%S', errors='coerce')
            
            # Filter and merge DataFrames
            s3stamm_filtered = s3stamm[s3stamm['LONGNAME'].str.contains(r'PA[345]-GWM-.*', regex=True) & 
                                       s3stamm['SHORTNAME'].str.contains(r'GWM-.*', regex=True)].copy()
            gwatab01_filtered = gwatab01[gwatab01['SMPNAME'].str.contains(r'PA[345]-GWM-.*', regex=True)].copy()
            
            s3stamm_filtered['Identifier Name'] = s3stamm_filtered['LONGNAME'].str.replace('PA', 'SX')
            gwatab01_filtered['Identifier Name'] = gwatab01_filtered['SMPNAME'].str.replace('PA', 'SX')
            
            merged_df = s3stamm_filtered.merge(gwatab01_filtered, left_on='Identifier Name', right_on='Identifier Name', how='left')
            
            merged_df['DATUM'] = pd.to_datetime(merged_df['DATUM'], errors='coerce')
            merged_df['SMPDATE'] = pd.to_datetime(merged_df['SMPDATE'], errors='coerce')
            
            # Handle missing dates
            if 'SMPDATE' in merged_df.columns:
                merged_df.dropna(subset=['SMPDATE'], inplace=True)
            
            # Split ORTSBEZ into Baulos, Kabelsectionen, and Ort
            merged_df[['Baulos', 'Kabelsectionen', 'Ort']] = merged_df['ORTSBEZ'].str.split('; ', expand=True)
            
            # Display the data range for the entire dataset
            min_date = merged_df['DATUM'].min()
            max_date = merged_df['DATUM'].max()
            st.write(f"**Data Range:** Start Date: {min_date} End Date: {max_date}")
            
            # Date range filter
            start_date = st.date_input("Startdatum", value=min_date)
            end_date = st.date_input("Enddatum", value=max_date)
            
            filtered_df = merged_df[(merged_df['DATUM'] >= pd.to_datetime(start_date)) & (merged_df['DATUM'] <= pd.to_datetime(end_date))]
            
            # Remove duplicate entries
            filtered_df = filtered_df.drop_duplicates()
            
            # Display filtered DataFrame
            st.subheader("Gefiltertes DataFrame")
            st.write(filtered_df[['Identifier Name', 'ORTSBEZ', 'Baulos', 'Kabelsectionen', 'Ort', 'DATUM', 'XCOORD', 'YCOORD', 'ZCOORDB', 'ZCOORDE', 'COLOUR', 'PH_FIELD', 'EC', 'TURB_LAB']])
            
            # Save the filtered DataFrame to an Excel file
            output_file_path = 'Gefilterte_GeoDin_Daten.xlsx'
            filtered_df.to_excel(output_file_path, index=False)
            
            # Provide download link for the saved file
            st.download_button(label="Gefilterte Daten herunterladen", data=open(output_file_path, 'rb').read(), file_name=output_file_path)
            
            # Create a 3-axis data chart with date, pH, Station Name (Identifier Name), and legend for ORTSBEZ
            fig = px.scatter(filtered_df, x='DATUM', y='PH_FIELD', color='ORTSBEZ',
                             hover_data=['Identifier Name', 'Baulos', 'Kabelsectionen', 'Ort'],
                             labels={'PH_FIELD': 'pH Value'},
                             title="3-Axis Data Chart with Date, pH, Station Name (Identifier Name), and Ortsbez")
            
            st.plotly_chart(fig)

# Team Contributions Section
elif sections == "Teambeiträge":
    st.header("Teambeiträge")
    
    team_contributions = {
        'Contribution': [
            'Datenanalyse und -verarbeitung auf GeoDin, ArcGIS usw.',
            'Projektkoordination in-house mit Clemens Neupert, Daniel Kahsay',
            'Projektkoordination extern mit dem Team von UIT, Eurofins',
            'Projektkoordination in-company mit Gabriel Knorr',
            'Projektassistenzarbeit, In-Office Meetings usw.',
            'Mittagspausen-Diskussionen mit Sven Namyslik, Volker Ackermann, Michaela Pohle'
        ],
        'Percentage of Hours': [50, 15, 12.5, 10, 7.5, 5]
    }
    
    df_contributions = pd.DataFrame(team_contributions)
    
    # Adjust the index to start from 1 instead of 0
    df_contributions.index = df_contributions.index + 1
    
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
if sections == "Schulungen":
    st.header("Schulungen")
    
    # Onboarding Trainings
    onboarding_trainings = {
        'Schulung': ['GeoDin', 'Gesundheit & Sicherheit', 'Virtuelles Onboarding', 'Thema Marketing'],
        'Status': ['Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen']
    }
    
    df_onboarding = pd.DataFrame(onboarding_trainings)
    
    # Adjust the index to start from 1 instead of 0
    df_onboarding.index = df_onboarding.index + 1

    # Work Project Trainings
    work_project_trainings = {
        'Schulung': ['SLPS_PA4_PA5 MA Einführung', 'SLPS_PA4_5 Workshop Ersteller', 'Projekt SuedLink obligatorische Datenschutzschulung'],
        'Status': ['Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen']
    }
    
    df_work_project = pd.DataFrame(work_project_trainings)
    
    # Adjust the index to start from 1 instead of 0
    df_work_project.index = df_work_project.index + 1

    # On-boarding Certifications
    onboarding_certifications = {
        'Schulung': ['Health & Safety Induction E- Learning', 'Bystander Intervention Training', 'Arcadis Global Onboarding & Mandatory', 'Code of Practice', 'Certified Mentoring Program 2025'],
        'Status': ['Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen']
    }

    df_onboarding_certifications = pd.DataFrame(onboarding_certifications)

    # Adjust the index to start from 1 instead of 0
    df_onboarding_certifications.index = df_onboarding_certifications.index + 1

    st.subheader("Onboarding-Schulungen")
    st.table(df_onboarding)
    
    st.subheader("Projektbezogene Schulungen")
    st.table(df_work_project)
    
    st.subheader("On-boarding Certifications")
    st.table(df_onboarding_certifications)