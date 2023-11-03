# Desafio para o Voluntariado de DevSecOps da Lacrei!
## Garantindo a Segurança do Projeto com Bandit e Safety Check

Como desenvolvedor, é fundamental garantir a segurança do nosso código. Para isso, integramos duas ferramentas muito importantes: o Bandit e o Safety Check. Eles são como guardiões, ajudando a identificar possíveis problemas de segurança e manter nossas aplicações mais seguras.

## Bandit: O Detetive do Código Python

O Bandit é como um detetive que analisa nosso código Python em busca de problemas de segurança. Ele olha atentamente para o código, procurando por práticas inseguras e possíveis vulnerabilidades. Com o Bandit, podemos descobrir erros de segurança como injeção de código ou uso inadequado de segredos. Sua presença no nosso processo de desenvolvimento nos ajuda a corrigir esses problemas desde o início.

### Um exemplo de uma falha de segurança simples presente aqui: 
As linhas que começam com Issue são alertas ou problemas detectados pela ferramenta Bandit. Neste caso, há vários alertas do tipo B105:hardcoded_password_string, que indica a presença de senhas codificadas diretamente no código, o que é uma prática de segurança ruim. Além disso, há alertas do tipo B101:assert_used, que adverte sobre o uso de afirmações assert. Esses alertas sugerem que o código possui declarações assert, que são tipicamente usadas para verificar condições e podem ser removidas quando o código é compilado para otimização.

## Safety Check: O Guardião das Dependências

O Safety Check atua como um guardião das dependências do nosso projeto. Ele verifica se as bibliotecas que usamos têm vulnerabilidades conhecidas. Isso é importante, já que versões desatualizadas podem representar riscos de segurança. O Safety Check nos ajuda a evitar problemas, garantindo que as dependências que utilizamos não tragam riscos inesperados.

Unindo o Bandit e o Safety Check, garantimos uma segurança extra ao nosso projeto. Eles nos ajudam não apenas a identificar possíveis problemas, mas também a adotar práticas de programação mais seguras desde o começo do desenvolvimento. Essas ferramentas são nossas aliadas, fortalecendo a segurança do nosso código e nos ajudando a construir aplicações mais confiáveis.

Ter essas verificações de segurança é como ter um escudo extra, protegendo nosso código e garantindo que nossas aplicações sejam mais robustas e seguras. É um passo importante para criar um ambiente de desenvolvimento mais seguro e confiável.

### exemplo de output utilizando o safety e o erro reportado:
```output
+=======================================================================================================================================================================+

                               /$$$$$$            /$$
                              /$$__  $$          | $$
           /$$$$$$$  /$$$$$$ | $$  \__//$$$$$$  /$$$$$$   /$$   /$$
          /$$_____/ |____  $$| $$$$   /$$__  $$|_  $$_/  | $$  | $$
         |  $$$$$$   /$$$$$$$| $$_/  | $$$$$$$$  | $$    | $$  | $$
          \____  $$ /$$__  $$| $$    | $$_____/  | $$ /$$| $$  | $$
          /$$$$$$$/|  $$$$$$$| $$    |  $$$$$$$  |  $$$$/|  $$$$$$$
         |_______/  \_______/|__/     \_______/   \___/   \____  $$
                                                          /$$  | $$
                                                         |  $$$$$$/
  by pyup.io                                              \______/

+=======================================================================================================================================================================+

 REPORT

  Safety is using PyUp's free open-source vulnerability database. This data is 30 days old and limited.
  For real-time enhanced vulnerability data, fix recommendations, severity reporting, cybersecurity support, team and project policy management and more sign up at
https://pyup.io or email sales@pyup.io

  Safety v2.3.5 is scanning for Vulnerabilities...
  Scanning dependencies in your environment:

 -> /LACREI/syssegurit/lib/python3.12/site-packages

  Using non-commercial database
  Found and scanned 67 packages
  Timestamp 2023-11-02 18:03:56
  7 vulnerabilities found
  0 vulnerabilities ignored

+=======================================================================================================================================================================+
 VULNERABILITIES FOUND
+=======================================================================================================================================================================+

-> Vulnerability found in flask version 1.1.4
   Vulnerability ID: 55261
   Affected spec: <2.2.5
   ADVISORY: Flask 2.2.5 and 2.3.2 include a fix for CVE-2023-30861: When all of the following conditions are met, a response containing data intended for one
   client may be cached and subsequently sent by the proxy to other clients. If the proxy also caches 'Set-Cookie' headers, it may send one client's 'session' cookie...
   CVE-2023-30861
   For more information, please visit https://pyup.io/v/55261/f17


-> Vulnerability found in sqlalchemy version 1.4.50
   Vulnerability ID: 51668
   Affected spec: <2.0.0b1
   ADVISORY: Sqlalchemy 2.0.0b1 avoids leaking cleartext passwords to the open for careless uses of str(engine.URL()) in logs and
   prints.https://github.com/sqlalchemy/sqlalchemy/pull/8563
   PVE-2022-51668
   For more information, please visit https://pyup.io/v/51668/f17


-> Vulnerability found in sqlalchemy-utils version 0.34.2
   Vulnerability ID: 42194
   Affected spec: >=0.27.0
   ADVISORY: Sqlalchemy-utils from version 0.27.0 'EncryptedType' uses by default AES with CBC mode. The IV that it uses is not random
   though.https://github.com/kvesteri/sqlalchemy-utils/issues/166https://github.com/kvesteri/sqlalchemy-utils/pull/499
   PVE-2021-42194
   For more information, please visit https://pyup.io/v/42194/f17


-> Vulnerability found in werkzeug version 0.15.6
   Vulnerability ID: 53325
   Affected spec: <2.2.3
   ADVISORY: Werkzeug 2.2.3 includes a fix for CVE-2023-25577: Prior to version 2.2.3, Werkzeug's multipart form data parser will parse an unlimited number of
   parts, including file parts. Parts can be a small amount of bytes, but each requires CPU time to parse and may use more memory as Python data. If a request can be...
   CVE-2023-25577
   For more information, please visit https://pyup.io/v/53325/f17


-> Vulnerability found in werkzeug version 0.15.6
   Vulnerability ID: 53326
   Affected spec: <2.2.3
   ADVISORY: Werkzeug 2.2.3 includes a fix for CVE-2023-23934: Browsers may allow "nameless" cookies that look like '=value' instead of 'key=value'. A vulnerable
   browser may allow a compromised application on an adjacent subdomain to exploit this to set a cookie like '=__Host-test=bad' for another subdomain. Werkzeug prior...
   CVE-2023-23934
   For more information, please visit https://pyup.io/v/53326/f17


-> Vulnerability found in apispec version 0.38.0
   Vulnerability ID: 42246
   Affected spec: <1.0.0b2
   ADVISORY: In PyYAML before 5.1, the yaml.load() API could execute arbitrary code if used with untrusted data. The load() function has been deprecated in
   version 5.1 and the 'UnsafeLoader' has been introduced for backward compatibility with the function.
   CVE-2017-18342
   For more information, please visit https://pyup.io/v/42246/f17


-> Vulnerability found in webargs version 1.10.0
   Vulnerability ID: 36963
   Affected spec: <5.1.3
   ADVISORY: webargs 5.1.3 fixes race condition between parallel requests when the cache is used. See: CVE-2019-9710.
   CVE-2019-9710
   For more information, please visit https://pyup.io/v/36963/f17

 Scan was completed. 7 vulnerabilities were found.

+=======================================================================================================================================================================+
```

## Workflow
#### !!!SEMPRE QUE ACONTECER UMA ATUALIAÇÂO NO REPOSITORIO O WORKFLOW VAI BUSCAR FALHAS DE SEGURANÇA!!!
![Captura de tela de 2023-11-02 21-23-41](https://github.com/Jorge-X/ELT-with-Power-BI/assets/140755201/88f654fa-f846-4229-a3fb-8e41c3d2093f)

Agora, os passos de upload dos artefatos estão dentro do bloco security_scan e devem ser executados após a execução do Bandit e do Safety Check. Esses artefatos estarão disponíveis para download após a conclusão bem-sucedida do workflow.
Para visualizar os resultados e entender melhor quais foram as questões de segurança identificadas, você pode abrir o arquivo bandit_results.txt (gerado pelo comando bandit -r . > bandit_results.txt) para examinar as descobertas específicas feitas pelo Bandit.
#### !!!RELATORIOS GERADOS PELO WORKFLOW!!!
![Captura de tela de 2023-11-02 21-26-42](https://github.com/Jorge-X/ELT-with-Power-BI/assets/140755201/1d506c22-5f1f-449c-87c9-b795c0fd0127)

O conteúdo do arquivo bandit_results.txt conterá detalhes sobre os problemas encontrados, como possíveis vulnerabilidades, práticas inseguras ou falhas conhecidas no código Python analisado. Abra esse arquivo para obter mais informações sobre as questões específicas identificadas pelo Bandit e trabalhe para corrigir esses problemas de segurança no código.

### Codigo utilizado no workflow:
```yml

name: Security Checks

on: [push]

jobs:
  security_scan:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.12

      - name: Install dependencies
        run: |
          pip install bandit safety
      - name: Run Bandit
        run: bandit -r . --format txt -o bandit_results.txt || true  # Este comando pode ignorar os erros e continuar a execução

      - name: Run Safety Check
        run: safety check --json > safety_results.json  # Executa o Safety Check e armazena os resultados em um arquivo JSON

      - name: Upload Bandit results
        if: always()  # Isso garante que os resultados sejam carregados mesmo se houver erros no Bandit
        uses: actions/upload-artifact@v2
        with:
          name: bandit-results
          path: bandit_results.txt

      - name: Upload Safety results
        uses: actions/upload-artifact@v2
        with:
          name: safety-results
          path: safety_results.json


```

Acho que com isso provo minha utilidade para o projeto.
Espero que gostem...
# END
# ( ≖.≖)
