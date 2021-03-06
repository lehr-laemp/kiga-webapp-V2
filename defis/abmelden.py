# -*- coding: utf-8 -*-

"""
Begonnen am 12.03.2022

@author: HM

abmelden.py

    - Seite für die Abmeldung

"""
# ---------------------------------------------------------
import datetime
import streamlit as st
from defis import helper


# ---------------------------------------------------------
def abmelde_seite():

    print(datetime.datetime.now().strftime('%H-%M-%S'), ': Lade Abmelde-Seite')

    st.title('Kiga-Eingabe')

    st.write('')
    st.write('Hier kannst du dich abmelden.')

    platzhalter = st.empty()

    if st.session_state['angemeldet'] == 'ja':
        
        abmelde_antwort = platzhalter.button('Abmelden')
        if abmelde_antwort:
            st.session_state['angemeldet'] = 'nein'
            platzhalter.empty()
            st.info('Herzlichen Dank für deine Mitarbeit.')
            helper.pickle_in_excel_speichern()
            helper.mail_senden('Abmeldung')
        
    else:
        st.warning('Gehe zu **Start** und melde dich an.')
