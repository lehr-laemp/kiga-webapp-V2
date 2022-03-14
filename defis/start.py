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


# ---------------------------------------------------------
def start_seite():

    print('Lade Startseite:', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

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
        
        else:
            st.warning('Falsches Passwort.')
            st.session_state['angemeldet'] = 'nein'
    
    else:
        st.info('Gehe zu **Eingabe** oder zu **Abmelden**.')