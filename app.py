# -*- coding: utf-8 -*-

"""
Begonnen am 12.03.2022

@author: HM

app.py

    - Hauptprogramm
    - lädt alle nötigen Funktionen aus dem Ordner def
    - Programm soll eine Oberfläche erstellen, damit Schülerdaten eingegeben werden können
        - geschützt - verschlüsselt
        - übers Internet

"""

# ---------------------------------------------------------
import os
import datetime

import streamlit as st
from defis import start
from defis import abmelden
from defis import eingabe
from defis import admin
from defis import helper



# ---------------------------------------------------------
def main():
    """
    Hauptprogamm
    """

    print('\n')
    print(datetime.datetime.now().strftime('%H-%M-%S'), ': Hauptprogramm')

    # allgemeine Angabe zur Seite
    st.set_page_config(
        page_title='Kiga-Eingabe',
        layout='centered',
        initial_sidebar_state='auto')

    # Menu an der Seite
    menu_item = st.sidebar.radio(
        'Navigation', index=0, options=('Start', 'Eingabe', 'Abmelden', 'Admin'))

    st.sidebar.warning('Abmelden nicht vergessen!')
    # st.sidebar.info(os.getcwd())

    # Verzweigung bei der Auswahl
    if menu_item == 'Start':
        start.start_seite()
    
    if menu_item == 'Eingabe':
        eingabe.eingabe_seite()

    if menu_item == 'Abmelden':
        abmelden.abmelde_seite()

    if menu_item == 'Admin':
        admin.datei_laden()


    return True


# ---------------------------------------------------------
if __name__ == "__main__":

    # # Timer starten oder stoppen
    # if 'timer' not in st.session_state:
    #     st.session_state['timer'] = 'start'
    #     helper.start_timer()
    #
    # if st.session_state['timer'] == 'start':
    #     helper.stop_timer()
    #     helper.start_timer()
            
    # Status: angemeldet oder nicht?
    if 'angemeldet' not in st.session_state:
        st.session_state['angemeldet'] = 'nein'
    
    # Abfrage ob sus.tmp vorhanden ist >> jemand ist am Arbeiten
    if not os.path.exists('Daten/sus.tmp'):
        main()
    
    # ist jemand angemeldet
    elif st.session_state['angemeldet'] == 'ja':
        main()

    else:
        st.title('Kiga-Abfrage')
        st.write('')
        st.info('Jemand gibt gerade etwas ein.')
        st.info('Versuche es später nochmals.')
        admin.datei_laden()

