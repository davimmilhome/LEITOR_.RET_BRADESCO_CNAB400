
Esse Script tem a inteção de ler arquivos de retorno  Bradesco (.RET) CNAB 400 
para obter um detalhamento das transações contidas. De maneira semelhante ao 
que acontece nos sites: 
https://wspf.banco.bradesco/wsValidadorUniversal/validadorgeral
https://wspf.bradesco.com.br/wsValidadorTeleBanco/ValidadorRemessa.aspx

Feito especificamente para o retorno tipo 1.

"Layout do Arquivo-Retorno - Registro de Transação - Tipo 1"

A intenção é fazer a análise separada do HEADER e do TRAILLER das transações, ou seja, são tratados de forma diferente dentro do script.

As informações vão para dentro da Scripts em dois arquivos, resume[todas as transações] e trailler[resumo das transações.] 

O arquivo getfile.py tem que ser adaptado a sua maneira de capturar o arquivo retorno.

Sei que ainda tenho muito a melhorar. Principalmente relacionado ao escopo global utilizado nas variáveis, aprendi que isso não é indicado pois pode causar confusão na hora de enxergar onde uma variável está atuando. Esse módulo é feito para ser utilizado de maneira independente. Porém, pretendo corrigir e melhorar isso no futuro. 

Abraços.



