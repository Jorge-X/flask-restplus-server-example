import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "scan_lacrei@outlook.com"
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Criando email
msg = EmailMessage()
msg['Subject'] = 'DAST LACREI'
msg['From'] = EMAIL_ADDRESS 
msg['To'] = 'teste1brvs@gmail.com'
msg.set_content('Olá, tudo bem?!\nJá fez sua verificação de segurança hoje?\n recomendamos fazer uma verificação todos os dias\n Uma falha de segurança é uma grande perigo!\n sempre lembre de anotar as vunerabilidades corrigidas na documentação!\n https://github.com/Lacrei/lacrei-institucional/actions/workflows/owasp_zap.yml\nhttps://www.notion.so/lacrei/anota-es-Vulnerabilidades-e-falso-positivo-9168a0cd41644f4e8e7acba0fc3c8f90  \nATENCIOSAMENTE: SCAN_OWASP')

# Usar a porta 587 com STARTTLS
with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    # Iniciar o processo de STARTTLS
    smtp.starttls()

    # Login
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Enviar mensagem
    smtp.send_message(msg)
