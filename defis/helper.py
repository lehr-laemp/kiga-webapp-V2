# -*- coding: utf-8 -*-

"""
Begonnen am 12.03.2022

@author: HM

helper.py

    - alle nötigen Funktionen

"""
# ---------------------------------------------------------
import datetime
import os
import pickle
import pyAesCrypt
import streamlit as st
import openpyxl

# ---------------------------------------------------------
def excel_tabelle_entschluesseln():

    print('Datenbank entschlüsseln', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    pyAesCrypt.decryptFile('Daten/sus.aes', 'Daten/sus.xlsx', st.secrets['tabelle_passwort'])

    
    
# ---------------------------------------------------------
def excel_tabelle_in_liste_speichern():

    print('Excel-Tabelle in SuS-Liste speichern', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    # öffne und aktiviere Excel-Tabelle
    kiga_datei = openpyxl.load_workbook('Daten/sus.xlsx')
    kiga_tabelle = kiga_datei.active

    sus_liste = []
    sus_einzel = []

    for reihe in range(2, kiga_tabelle.max_row + 1):
        for spalte in range(1, 17):
            sus_einzel.append(
                kiga_tabelle.cell(row=reihe, column=spalte).value)
                
            if spalte == 16:
                sus_liste.append(sus_einzel)
                sus_einzel = []

    # OK print(sus_liste)
    return sus_liste

# ---------------------------------------------------------
def liste_in_pickle_speichern(sus_liste):

    print('Liste in Pickle speichern', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    with open('Daten/sus.tmp', 'wb') as datei_handler:
        pickle.dump(sus_liste, datei_handler)

    return True

# ---------------------------------------------------------
def excel_tabelle_loeschen():
    
    print('Excel-Tabelle löschen', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    os.remove('Daten/sus.xlsx')

    return True


# ---------------------------------------------------------
def pickle_in_excel_speichern():
    """
    Speichert Pickle-Dump in Excel-Tabelle
        Öffnet dazu die verschlüsselte Tabelle
        Schreibt die Daten in die Tabelle
        Verschlüsselt die Tabelle wieder
        Löscht die entschlüsselte Tabelle
        Löscht den Pickle-Dump
    """

    
    print('Pickle in Excel-Tabelle speichern', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    # Pickle-Dump auslesen
    with open('Daten/sus.tmp', 'rb') as datei_handler:
            sus_liste = pickle.load(datei_handler)

    # Tabelle entschlüsseln
    excel_tabelle_entschluesseln()

    # öffne und aktiviere Excel-Tabelle
    kiga_datei = openpyxl.load_workbook('Daten/sus.xlsx')
    kiga_tabelle = kiga_datei.active

    # Schreibe die SuS-Liste in der Excel-Tabelle
    for reihe in range(len(sus_liste)):
        # OK print(liste[reihe])
        for spalte in range(0, 16):
            kiga_tabelle.cell(row=reihe+2, column=spalte+1).value = sus_liste[reihe][spalte]

    # Speichere die Excel-Tabelle
    kiga_datei.save('Daten/sus.xlsx')

    excel_tabelle_verschluesseln() # und löschen

    # Pickle-Dump löschen
    os.remove('Daten/sus.tmp')

    return True


# ---------------------------------------------------------
def excel_tabelle_verschluesseln():
    
    print('Excel-Tabelle verschlüsseln', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    # Excel-Tabelle verschlüsseln
    pyAesCrypt.encryptFile('Daten/sus.xlsx', 'Daten/sus.aes', st.secrets['tabelle_passwort'])

    # Excel-Tabelle löschen
    os.remove('Daten/sus.xlsx')
    
    return True


# ---------------------------------------------------------
def liste_aus_pickle_holen():
    
    print('Liste aus Pickle-Dump holen', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    # Pickle-Dump auslesen
    with open('Daten/sus.tmp', 'rb') as datei_handler:
            sus_liste = pickle.load(datei_handler) 

    return sus_liste
    

# ---------------------------------------------------------
def kiga_standorte_lesen(sus_liste):
    """
    Lies aus der Liste der SuS die möglichen Kiga-Standorte
    return: Liste der Kiga, sortiert
    """

    print('Kiga-Standorte einlesen', datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S'))

    kiga_liste = []
    for i in range(len(sus_liste)):
        # OK print(sus_liste[i][4])
        kiga_liste.append(sus_liste[i][4])

    return sorted(set(kiga_liste))
