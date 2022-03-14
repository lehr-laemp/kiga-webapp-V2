# -*- coding: utf-8 -*-

"""
Begonnen am 12.03.2022

@author: HM

eingabe.py

    - Seite für die Eingabe

"""

# ---------------------------------------------------------
import datetime
import os
import streamlit as st
from defis import helper


# ---------------------------------------------------------
def eingabe_seite():

    print('Lade Eingabe-Seite:', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    st.title('Kiga-Eingabe')

    # nicht angemeldet
    if st.session_state['angemeldet'] == 'nein':
        st.warning('Gehe zu **Start** und melde dich an.')

    # Angemeldet   
    else:
        st.info('Toll, jetzt kann es losgehen.')

        if not os.path.exists('Daten/sus.tmp'):

            # Daten entschlüsseln
            helper.excel_tabelle_entschluesseln()
            
            # Daten der SuS in eine Liste speichern
            sus_liste = helper.excel_tabelle_in_liste_speichern()

            # SuS-Liste in einem pickle-Dump speichern
            if not helper.liste_in_pickle_speichern(sus_liste):
                st.warning('Konnte Dump nicht erstellen')

            # Excel-Tabelle löschen
            helper.excel_tabelle_loeschen()

        else:
            sus_liste = helper.liste_aus_pickle_holen()

        # Kiga wählen
        kiga_gewaehlt = st.selectbox(
            label='Wähle einen Kindergarten.', 
            options=helper.kiga_standorte_lesen(sus_liste), 
            )

        # Kinder aus gewähltem Kiga
        schueler_gewaehlt_liste = []
        sus_name = ''
        for i in range(len(sus_liste)):
            if sus_liste[i][4] == kiga_gewaehlt:
                sus_name = str(sus_liste[i][0]) + '  ' \
                    + sus_liste[i][1] + '  ' + sus_liste[i][2] + '  ' + sus_liste[i][3] 
                schueler_gewaehlt_liste.append(sus_name)
                sus_name = ''
        
        # OK st.info('Kinder aus gewähltem Kiga')
        # OK st.info(schueler_gewaehlt_liste)

        kind_gewaehlt = st.selectbox(
            label='Wähle ein Kind.',
            options=schueler_gewaehlt_liste,
            )

        # Index des gewählten Kindes bestimmen
        kind_gewaehlt_id = kind_gewaehlt[0:6]
        # OK print(kind_gewaehlt_id, type(kind_gewaehlt_id))
        # OK st.info(kind_gewaehlt_id)

        for i in range(len(sus_liste)):
            if int(kind_gewaehlt_id) in sus_liste[i]:
                # OK print(schueler_liste[i])
                kind_gewaehlt_index = i
                break
    
        # OK st.info('Index des gewählten Kindes.')
        # OK st.info(kind_gewaehlt_index)

        ############################
        # Werte auslesen für Anzeige
        
        # DaZ
        print('DaZ', sus_liste[kind_gewaehlt_index][1], sus_liste[kind_gewaehlt_index][5])
        if sus_liste[kind_gewaehlt_index][5] == 'x':
            daz_wert = True
        else:
            daz_wert = False

        # Logo
        print('Logo', sus_liste[kind_gewaehlt_index][1], sus_liste[kind_gewaehlt_index][6])
        if sus_liste[kind_gewaehlt_index][6] == 'x':
            logo_wert = True
        else:
            logo_wert = False

        # Hort
        print('Hort', sus_liste[kind_gewaehlt_index][1], sus_liste[kind_gewaehlt_index][7])
        if sus_liste[kind_gewaehlt_index][7] == 'x':
            hort_wert = True
        else:
            hort_wert = False

        # andere Therapien
        print('andere Therapien', sus_liste[kind_gewaehlt_index][1], 
            sus_liste[kind_gewaehlt_index][8])
        if sus_liste[kind_gewaehlt_index][8] == None:
            andere_wert = '-'
        else:
            andere_wert = sus_liste[kind_gewaehlt_index][8]
        
        # SAB
        print('SAB', sus_liste[kind_gewaehlt_index][1], sus_liste[kind_gewaehlt_index][9])
        if sus_liste[kind_gewaehlt_index][9] == 'x':
            sab_wert = True
        else:
            sab_wert = False

        # gegen SAB
        print('gegen SAB', sus_liste[kind_gewaehlt_index][1], sus_liste[kind_gewaehlt_index][10])
        if sus_liste[kind_gewaehlt_index][10] == 'x':
            gegen_sab_wert = True
        else:
            gegen_sab_wert = False

        # EK
        print('EK', sus_liste[kind_gewaehlt_index][1], sus_liste[kind_gewaehlt_index][11])
        if sus_liste[kind_gewaehlt_index][11] == 'x':
            ek_wert = True
        else:
            ek_wert = False

        # Geschwister
        print('Geschwister', sus_liste[kind_gewaehlt_index][1], 
            sus_liste[kind_gewaehlt_index][12])
        if sus_liste[kind_gewaehlt_index][12] == None:
            geschwister_wert = '-'
        else:
            geschwister_wert = sus_liste[kind_gewaehlt_index][12]

        # Aufwand mit SuS
        print('Aufwand mit SuS', sus_liste[kind_gewaehlt_index][1], 
            sus_liste[kind_gewaehlt_index][13])
        if sus_liste[kind_gewaehlt_index][13] == None:
            aufwand_sus_wert = 'wenig'
        else:
            aufwand_sus_wert = sus_liste[kind_gewaehlt_index][13]

        # Aufwand mit Eltern
        print('Aufwand mit Eltern', sus_liste[kind_gewaehlt_index][1], 
            sus_liste[kind_gewaehlt_index][14])
        if sus_liste[kind_gewaehlt_index][14] == None:
            aufwand_eltern_wert = 'wenig'
        else:
            aufwand_eltern_wert = sus_liste[kind_gewaehlt_index][14]

        # Bemerkungen
        print('Bemerkungen', sus_liste[kind_gewaehlt_index][1], 
            sus_liste[kind_gewaehlt_index][15])
        if sus_liste[kind_gewaehlt_index][15] == None:
            bemerkungen_wert = '-'
        else:
            bemerkungen_wert = sus_liste[kind_gewaehlt_index][15]

        
        ###########################
        # Formular für alle Eingaben
        with st.form('Formular', clear_on_submit=True):

            # Therapien
            # 3 Spalten für Checkboxen
            col1, col2, col3 = st.columns(3)

            # DaZ
            daz_antwort = col1.checkbox(label='DaZ?', value=daz_wert)
            
            # Logo
            logo_antwort = col2.checkbox(label='Logo?', value=logo_wert)
            
            # Hort
            hort_antwort = col3.checkbox(label='Hort?', value=hort_wert)
        
            # andere Therapien
            andere_antwort = st.text_input(label='andere Therapien?',
                value=andere_wert)
            
            # SAB
            sab_antwort = col1.checkbox(label='SAB?', value=sab_wert)
            
            # gegen SAB
            gegen_sab_antwort = col2.checkbox(label='gegen SAB?', value=gegen_sab_wert)
            
            # EK
            ek_antwort = col3.checkbox(label='EK?', value=ek_wert)
            
            # Geschwister
            geschwister_antwort = st.text_input(label='Geschwister?', value=geschwister_wert)
            
            # Aufwand SuS
            aufwand_sus_antwort = st.select_slider(
                'Aufwand mit SuS', value= aufwand_sus_wert,
                options=['wenig', 'mittel', 'gross'])
            
            # Aufwand mit Eltern
            aufwand_eltern_antwort = st.select_slider(
                'Aufwand mit Eltern', value= aufwand_eltern_wert,
                options=['wenig', 'mittel', 'gross'])

            # Bemerkungen
            bemerkungen_antwort = st.text_area(label='Bemerkungen',
                value=bemerkungen_wert, height=80)

            #########################
            # Abschluss mit Speichern
            gespeichert = st.form_submit_button('Speichern')
            if gespeichert:

                # Daz-Antwort speichern
                if daz_antwort == True:
                    sus_liste[kind_gewaehlt_index][5] = 'x'
                else:
                    sus_liste[kind_gewaehlt_index][5] = '-'                

                # Logo-Antwort speichern
                if logo_antwort == True:
                    sus_liste[kind_gewaehlt_index][6] = 'x'
                else:
                    sus_liste[kind_gewaehlt_index][6] = '-'

                # Hort-Antwort speichern
                if hort_antwort == True:
                    sus_liste[kind_gewaehlt_index][7] = 'x'
                else:
                    sus_liste[kind_gewaehlt_index][7] = '-'

                # andere Therapien Antwort speichern
                sus_liste[kind_gewaehlt_index][8] = andere_antwort

                # SAB-Antwort speichern
                if sab_antwort == True:
                    sus_liste[kind_gewaehlt_index][9] = 'x'
                else:
                    sus_liste[kind_gewaehlt_index][9] = '-'

                # gegen SAB-Antwort speichern
                if gegen_sab_antwort == True:
                    sus_liste[kind_gewaehlt_index][10] = 'x'
                else:
                    sus_liste[kind_gewaehlt_index][10] = '-'
                
                # EK-Antwort speichern
                if ek_antwort == True:
                    sus_liste[kind_gewaehlt_index][11] = 'x'
                else:
                    sus_liste[kind_gewaehlt_index][11] = '-'

                # Geschwister-Antwort speichern
                sus_liste[kind_gewaehlt_index][12] = geschwister_antwort

                # SuS-Aufwand-Antwort speichern
                sus_liste[kind_gewaehlt_index][13] = aufwand_sus_antwort

                # Eltern-Aufwand-Antwort speichern
                sus_liste[kind_gewaehlt_index][14] = aufwand_eltern_antwort

                # Bemerkungen-Antwort speichern
                sus_liste[kind_gewaehlt_index][15] = bemerkungen_antwort

                
                
                # Liste in Pickle speichern
                helper.liste_in_pickle_speichern(sus_liste)
                # sus_liste = helper.liste_aus_pickle_holen()



        
        # die ganze Liste
        #st.write('')
        #st.info(sus_liste)