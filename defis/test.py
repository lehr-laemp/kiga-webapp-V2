# -*- coding: utf-8 -*-

"""
Begonnen am 12.03.2022

@author: HM

test.py

    - Test-Seite 

"""

import datetime
import os
import streamlit as st

def datei_laden():
    
    print(datetime.datetime.now().strftime('%H-%M-%S'), ': Lade Testseite')

    st.title('Kiga-Eingabe')

    # st.download_button(
    #     label="Download data as CSV",
    #     data=,
    #     file_name='Daten/sus.aes',
    #     mime='text/aes',
    #     )

    with open('Daten/sus.aes', 'rb') as file:
        st.download_button(label='Download aes', 
            data=file, file_name='sus.aes')