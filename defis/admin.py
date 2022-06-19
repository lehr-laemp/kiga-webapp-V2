# -*- coding: utf-8 -*-

"""
Begonnen am 12.03.2022

@author: HM

admin.py

    - Admin-Seite 

"""

# ---------------------------------------------------------
import datetime
import os
import streamlit as st
from defis import helper


# ---------------------------------------------------------
def datei_laden():
    
    print(datetime.datetime.now().strftime('%H-%M-%S'), ': Lade Adminseite')

    st.write('**Administrator**')

    # Passwort-Eingabe
    
    # Container, um Passwort-Eingabe bei erfolgreicher Eingabe zu löschen
    leeres_feld = st.empty()

    passwort_antwort = ''
    passwort_antwort = leeres_feld.text_input(
        label='Bitte das Passwort eingeben:', type='password')

    if passwort_antwort == '':
        # zeige noch nichts an
        pass
    
    elif passwort_antwort == st.secrets['admin_passwort']:
        
        leeres_feld.empty()
        # Button für Datei-Download 
        with open('Daten/sus.aes', 'rb') as file:
            st.download_button(label='Download aes', 
                data=file, file_name='sus.aes')

 #######       # Button für Backup-Download
        with open('Daten/sus.aes', 'rb') as file:
            st.download_button(label='Download Backup-Datei', 
                data=file, file_name='sus.aes')

        # Button für reguläre Abmeldung
        abmelde_antwort = st.button('Abmelden')
        if abmelde_antwort:
            helper.pickle_in_excel_speichern()
            # helper.mail_senden('Abmeldung')

    else:
        st.warning('Falsches Passwort.')