# -*- coding: utf-8 -*-

"""
Begonnen am 4.06.2021

@author: HM

Mails sollen automatisch versendet werden.

Für Benachrichtigungen und Termine

"""

import keyring      # um das Passwort nicht im Script zu speichern
import smtplib
import ssl
from email.message import EmailMessage

# -------------------------------------------------------------------
# Passwort auf dem System speichern mit keyring
# im Terminal: keyring set 'system' 'mail.gmx.net'

# -------------------------------------------------------------------
# Angaben für den Server
gmx_smpt = 'mail.gmx.net'
gmx_passwort = keyring.get_password('system', gmx_smpt)
gmx_port = 587

# -------------------------------------------------------------------
# Angaben zum Mail
mail_von = 'satipati@gmx.ch'
mail_fuer = 'klameflu@gmail.com'
mail_betreff = 'Testmail mit python'
mail_text = """\
Hallo
Wie geht es dir?
Mir geht es gut.
Liebe Gruesse 
Hansruedi"""

# übersetzen in Email-Format
nachricht = EmailMessage()
nachricht.set_content(mail_text)

nachricht['Subject'] = mail_betreff
nachricht['From'] = mail_von 
nachricht['To'] = mail_fuer

# Verbindung mit Server
context = ssl.create_default_context()
try:
    server = smtplib.SMTP(gmx_smpt, gmx_port)
    server.set_debuglevel(2)
    server.starttls(context=context)
    server.login(mail_von, gmx_passwort)
    server.send_message(nachricht)
except Exception as e:
    print(e)
finally:
    server.quit()
