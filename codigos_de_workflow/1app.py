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
msg.set_content('Olá, tudo bem?!\nJá fez sua verificação de segurança hoje?\n recomendamos fazer uma verificação todos os dias\n Uma falha de segurança é uma grande perigo!\n sempre lembre de anotar as vunerabilidades corrigidas na documentação!\n https://github.com/Lacrei/lacrei-institucional/actions/workflows/owasp_zap.yml\nhttps://www.notion.so/lacrei/f4b829cba43c414cbb8e0e491d20e623?v=40912c3f99ef4e9fb9d4a05b6d8ce98e  \nATENCIOSAMENTE: SCAN_OWASP')

# Usar a porta 587 com STARTTLS
with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    # Iniciar o processo de STARTTLS
    smtp.starttls()

    # Login
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Enviar mensagem
    smtp.send_message(msg)
