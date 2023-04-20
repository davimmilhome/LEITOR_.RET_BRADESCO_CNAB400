# Leitor CNAB 400 BRADESCO

Esse Script é um programa CLI que tem a inteção de ler arquivos de retorno Bradesco (.RET) CNAB 400 para obter um detalhamento das transações contidas. De maneira semelhante ao que acontece nos sites: https://wspf.banco.bradesco/wsValidadorUniversal/validadorgeral https://wspf.bradesco.com.br/wsValidadorTeleBanco/ValidadorRemessa.aspx

Para seu funcionamento adequado, você precisa analisar e adaptar pontos 
específicos do CRM utilizado em sua empresa. 

Feito especificamente para o retorno tipo 1.

"Layout do Arquivo-Retorno - Registro de Transação - Tipo 1"

A intenção é fazer a análise separada do HEADER e do TRAILLER das transações, ou seja, são tratados de forma diferente dentro do script.

As informações vão para dentro da Scripts em dois arquivos, resume[todas as transações] e trailler[resumo das transações.]

O arquivo getfile.py tem que ser adaptado a sua maneira de capturar o arquivo retorno.

Sei que ainda tem  muito a melhorar. Principalmente relacionado ao escopo global utilizado nas variáveis, isso não é indicado em projetos, pois pode causar confusão na hora de enxergar onde uma variável está atuando. Esse módulo é feito para ser utilizado de maneira independente. Porém, pretendo corrigir e melhorar isso no futuro.

Mais detalhes do funcionamento desse programa estão nos comentários do código da aplicação.

Abraços.

## Funcionalidades
 * Realizar leitura dos arquivos CNAB400
 
## Como usar

Clone o repositório
Instale as dependências
Adapte o getfile(se necessário) no leitor_retorno.py
Execute o leitor_retorno.py

## Tecnologias utilizadas
Python, bibliotecas built-in.
Pandas

## Contribuindo
No momento não está aberto a contribuções.

## Autores
Davi Martins Milhome

##Licença
No momento, sem licença.

