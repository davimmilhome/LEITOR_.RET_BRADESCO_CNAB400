"""Script que principal, lê o arquivo .RET do Bradesco.

Primeiramente, busca o arquivo no móudlo Methods.get_file.
O módulo Methods.get_file deve ser adaptado em uma implementação para captar
o arquivo.
Observe que os métodos para ler os registros está diferente
dos métodos para ler trailler (pode ser replicado para o header).
Basicamente esse módulo funciona captando o arquivo e em seguida
fazendo vários for-loops em cada campo para formatar o CSV de
saída e, por último, lê a útlima linha do arquivo. As funções são
executadas dentro do próprio móudlo utilizando o dundler main.
Para mais informações entre em contato com Davi Milhome.
"""
import pandas as pd

import Methods.get_file as gf
from Methods.get_file import ret_file_path

#GLOBALS
ret_file1 = ''
df_conta = ''
df_nosso_numero = ''
df_valor_titulo = ''
df_dt_vencimento = ''
df_dt_ocorrencia = ''
df_dt_credito = ''
df_valor_pago = ''
df_ocorrencia = ''
df_motivo = ''
df_final = ''
trailler_variables_dict = ''


def file_reader():
    """Pega o arquivo a ser lido."""
    global ret_file1
    ret_file1 = open(gf.getfile(),'r')


#
#Esse grupo de funções tem o objetivo de ler campos específicos do arquivo
# O nome da função corresponde ao campo lido.

def conta():
    """Lê o campo conta, inputa no df_conta."""
    global df_conta
    ls_conta = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:
        # [1:] -> Indica que iremos ignorar  cabeçalho na leitura
            element = i[32:37]
            ls_conta.append(element)

    df_conta = pd.DataFrame(ls_conta, columns=['conta'])

def nosso_numero():
    """Lê o campo nosso numero, inputa no df_nosso_numero."""
    global df_nosso_numero
    ls_nosso_numero = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:
        # [1:] -> Indica que iremos ignorar  cabeçalho na leitura
            element = i[70:82]
            ls_nosso_numero.append(element)

    df_nosso_numero = pd.DataFrame(ls_nosso_numero, columns=['nosso_numero'])

def valor_titulo():
    """Lê o campo valor título, inputa no df_valor_titulo."""
    global df_valor_titulo
    ls_valor_titulo = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]: # IGNORANDO HEADER E TRAILLER

            element = i[153:163]+'.'+i[163:165]
            ls_valor_titulo.append(element)

    df_valor_titulo = pd.DataFrame(ls_valor_titulo,columns = ['valor_pago'])
    df_valor_titulo = df_valor_titulo.apply(pd.to_numeric, errors='coerce')

def dt_vencimento():
    """Lê o campo dt_vencimento,inputa no df_dt_vencimento."""
    global df_dt_vencimento
    ls_dt_vencimento = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:  # IGNORANDO HEADER E TRAILLER

            element = i[146:148]+'/'+i[148:150]+'/'+i[150:152]
            ls_dt_vencimento.append(element)

    df_dt_vencimento = pd.DataFrame(
        ls_dt_vencimento,
        columns=['dt_vencimento'])

def dt_ocorrencia():
    """Lê o campo dt_ocorrencia, inputa no df_dt_ocorrencia."""
    global df_dt_ocorrencia
    ls_dt_ocorrencia = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:  # IGNORANDO HEADER E TRAILLER

            element = i[110:112]+'/'+i[112:114]+'/'+i[114:116]
            ls_dt_ocorrencia.append(element)

    df_dt_ocorrencia = pd.DataFrame(
        ls_dt_ocorrencia, columns=['dt_ocorrencia'])

def dt_credito():
    """Lê o campo dt_credito, inputa no df_dt_credito.

    O input só é feito se valor pago <> 0"""
    global df_dt_credito
    ls_dt_credito = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:  # IGNORANDO HEADER E TRAILLER
            if int(i[254:266]) != 0: #SE O VALOR PAGO FOR DIFERENTE DE ZERO
                element = i[295:297]+'/'+i[297:299]+'/'+i[299:301]
                ls_dt_credito.append(element)
            else: # se não for diferente de zero
                element = ""
                ls_dt_credito.append(element)

    df_dt_credito = pd.DataFrame(ls_dt_credito, columns=['dt_credito'])

def valor_pago():
    """Lê o campo df_valor_pago, inputa no df_valor_pago.

    Faz a separação com ponto dos centavos.
    Transforma o df data em float."""
    global df_valor_pago
    ls_valor_pago = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]: # IGNORANDO HEADER E TRAILLER

            element = i[254:264]+'.'+i[264:266]
            ls_valor_pago.append(element)

    df_valor_pago = pd.DataFrame(ls_valor_pago,columns = ['valor_pago'])
    df_valor_pago = df_valor_pago.apply(pd.to_numeric, errors='coerce')

def ocorrencia():
    """Lê o campo ocorrencia, inputa no df_ocorrencia."""
    global df_ocorrencia
    ls_ocorrencia = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:  # IGNORANDO HEADER E TRAILLER

            element = i[108:110]
            ls_ocorrencia.append(element)

    df_ocorrencia = pd.DataFrame(ls_ocorrencia, columns=['ocorrencia'])

def motivo():
    """Lê o campo motivo, inputa no df_motivo."""
    global df_motivo
    ls_motivo = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:  # IGNORANDO HEADER E TRAILLER

            element = i[318:328]
            ls_motivo.append(element)

    df_motivo = pd.DataFrame(ls_motivo, columns=['motivo'])

def file_fitter():
    """Invoca as funções para ciração dos dfs e formata o arquivo resume_csv.

    Invoca as funções para a criação dos DFS.
    Utiliza os dfs definidos acima para juntar em um único csv.
    É possível desativar alguma leitura específica caso seja necessario
    Caso você adicione um campo a mais de leitura, será necessário
    adiconar o novo método aos que seguem abaixo"""
    global df_final

    file_reader()
    conta()
    nosso_numero()
    dt_vencimento()
    valor_titulo()
    dt_ocorrencia()
    dt_credito()
    valor_pago()
    ocorrencia()
    motivo()

    #formatando DF
    df_final = pd.DataFrame()
    df_final["conta"] = df_conta
    df_final["nosso_numero"] = df_nosso_numero
    df_final["dt_vencimento"] = df_dt_vencimento
    df_final["valor_titulo"] = df_valor_titulo
    df_final["dt_ocorrencia"] = df_dt_ocorrencia
    df_final["dt_credito"] = df_dt_credito
    df_final["valor_pago"] = df_valor_pago
    df_final["ocorrencia"] = df_ocorrencia
    df_final["motivo"] = df_motivo
    print(df_final)
def out_resume():
    """Saída do aruqivo csv do"""
    df_final.to_csv(
        './resume_csv.csv',
        header = True ,
        index = False,
        decimal = ',',
        sep = ';')

##################################HEADER###############################
#ESPAÇO PARA Extair informações do HEADER



##################################Trailler###############################
#ESPAÇO PARA Extair informações do TRAILLER

trailler_variables_dict = {}
def trailler_reader(x, y,z, money):
    """Lê a última linha do arquivo, inputa no dict trailler_variables_dict

    Argumentos:
    x -- Nome do campo inserido no dicionário
    y -- campo de ínicio da leitura
    z --  campo de termino da leitura
    money -- verifica se campo monetário para adicionar a separação(money=on).
    Depende da fille_fitter(), fille_fitter() deve ser invocada antes
    Isso acontece pois fille_fitter invoca file_reader.
    """
    global trailler_variables_dict
    with open(gf.ret_file_path, 'r') as ret_file1:

        if money == 'on':
            #Adiciona o separador as casas decimais
            for i in ret_file1.readlines()[-1:]:

                value = i[y:z-2]+"."+i[z-2:z]
                trailler_variables_dict.update({x:value})
        else:

            for i in ret_file1.readlines()[-1:]:

                value = i[y:z]
                trailler_variables_dict.update({x:value})

def trailler_fitter():
    """Utiliza trailler_reader especificandoos campos que se deseja."""
    trailler_reader('qtde_registros_(02)', 57, 62, money='off')
    trailler_reader('valor_registrado_(02)', 62, 74, money='on')
    trailler_reader('qtde_liquidado_(06)', 86, 91, money='off')
    trailler_reader('valor_liquidado_(06)', 74, 86, money='on')
    #NECESSÁRIO SOMAR VALOR LIQUIDADO TOTAL DE OUTRAS OCORRENCIAS ex:17
    trailler_reader('qtde_baixa_(09e10)', 103, 108, money='off')
    trailler_reader('valor_baixado_(09e10)', 108, 120, money='on')

def out_trailler():
    """Escrita do trailler_dict no trailler.txt, saida do txt.

    Escreve as infomações contidas no dicionário do trailler num arquivo txt.
    """
    trailler_file = open("./trailler.txt",'w')
    trailler_file.write("Leitura do Trailler, ultima linha do arquivo:\n")

    for k,v in trailler_variables_dict.items():

        trailler_file.write(f'{k} : {v}\n')

    trailler_file.close()

if __name__ == '__main__':
    """Executa as funções em ordem quando o script é inicializado.
    
    A ordem é importante.
    """
    file_fitter()
    out_resume()
    trailler_fitter()
    out_trailler()


