// Importa a API do SendGrid
const sgMail = require('@sendgrid/mail');
// Set the SendGrid API key
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

// Define o email que será enviado
const msg = {
    to: 'teste1brvs@gmail.com',
    from: 'SCAN_LACREI@outlook.com',
    subject: 'Assunto do Email',
    html: `
    <p>FOI ENCONTRADA UMA VULNERABILIDADE NO SITE:</p>
    <p><a href="http://staging.lacreisaude.com.br" target="_blank" rel="noopener noreferrer">staging lacrei saúde</a></p>
    `,
};
// Envia o email e loga o resultado
sgMail.send(msg)
    .then(() => console.log('Email enviado com sucesso'))
    .catch((error) => console.error('Erro ao enviar email:', error));