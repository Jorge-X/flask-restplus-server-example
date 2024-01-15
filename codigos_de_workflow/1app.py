import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "scan_lacrei@outlook.com"
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Criando email
msg = EmailMessage()
msg['Subject'] = 'AVISO QUE, VOCE FOI AVISADO!'
msg['From'] = EMAIL_ADDRESS 
msg['To'] = 'teste1brvs@gmail.com'
msg.set_content('Olá foi encontrada uma vunerabilidade pelo owasp verifique no https://github.com/Lacrei/lacrei-institucional/actions/workflows/owasp_zap.yml\n ATENCIOSAMENTE: SCAN_OWASP')

# Usar a porta 587 com STARTTLS
with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    # Iniciar o processo de STARTTLS
    smtp.starttls()

    # Login
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Enviar mensagem
    smtp.send_message(msg)
