# -*- coding: utf-8 -*-

"""
Begonnen am 12.03.2022

@author: HM

start.py

    - Startseite

"""

# ---------------------------------------------------------
import datetime
import streamlit as st
from defis import helper


# ---------------------------------------------------------
def start_seite():

    print(datetime.datetime.now().strftime('%H-%M-%S'), ': Lade Startseite')

    st.title('Kiga-Eingabe')

    st.write('')
    # st.info(st.secrets['tabelle_passwort'])

    # Container, um Passwort-Eingabe bei erfolgreicher Eingabe zu löschen
    leeres_feld = st.empty()

    # Passwortabfrage nur wenn noch nicht angemeldet
    if st.session_state['angemeldet'] == 'nein':
        passwort_antwort = ''
        passwort_antwort = leeres_feld.text_input(
            label='Bitte das Passwort eingeben:', type='password')
        # OK st.write(passwort_antwort)

        if passwort_antwort == '':
            # zeige noch nichts an
            pass
        
        elif passwort_antwort == st.secrets['app_passwort']:
            st.info('Prima!')
            st.info('Gehe zu **Eingabe**.')
            st.session_state['angemeldet'] = 'ja'
            leeres_feld.empty()
            
            # Daten entschlüsseln >> Excel-Tabelle
            helper.excel_tabelle_entschluesseln()
            
            # Daten der SuS in eine Liste speichern
            sus_liste = helper.excel_tabelle_in_liste_speichern()
            
            # SuS-Liste in einem pickle-Dump speichern
            if not helper.liste_in_pickle_speichern(sus_liste):
                st.warning('Konnte Dump nicht erstellen')

            # Excel-Tabelle löschen
            helper.excel_tabelle_loeschen()

            # Mail senden
            helper.mail_senden('Anmeldung')

        else:
            st.warning('Falsches Passwort.')
            st.session_state['angemeldet'] = 'nein'

    
    else:
        st.info('Gehe zu **Eingabe** oder zu **Abmelden**.')