"""Script que lê efetivamento o .RET
Observe que os métodos para ler os registros está dif
dos métodos para ler trailler (pode ser replicado para o header.
"""
import pandas as pd

import Methods.get_file as gf
from Methods.get_file import ret_file_path

def file_reader():
    global ret_file1


    ret_file1 = open(gf.getfile(),'r')

def nosso_numero():
    global df_nosso_numero


    ls_nosso_numero = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:
        # [1:] -> Indica que iremos ignorar  cabeçalho na leitura
            element = i[70:82]
            ls_nosso_numero.append(element)

    df_nosso_numero = pd.DataFrame(ls_nosso_numero, columns=['nosso_numero'])

def valor_titulo():
    global df_valor_titulo


    ls_valor_titulo = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]: # IGNORANDO HEADER E TRAILLER

            element = i[153:163]+'.'+i[163:165]
            ls_valor_titulo.append(element)

    df_valor_titulo = pd.DataFrame(ls_valor_titulo,columns = ['valor_pago'])
    df_valor_titulo = df_valor_titulo.apply(pd.to_numeric, errors='coerce')

def dt_vencimento():
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
    global df_dt_ocorrencia


    ls_dt_ocorrencia = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:  # IGNORANDO HEADER E TRAILLER

            element = i[110:112]+'/'+i[112:114]+'/'+i[114:116]
            ls_dt_ocorrencia.append(element)

    df_dt_ocorrencia = pd.DataFrame(
        ls_dt_ocorrencia, columns=['dt_ocorrencia'])

def valor_pago():
    global df_valor_pago


    ls_valor_pago = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]: # IGNORANDO HEADER E TRAILLER

            element = i[254:264]+'.'+i[264:266]
            ls_valor_pago.append(element)

    df_valor_pago = pd.DataFrame(ls_valor_pago,columns = ['valor_pago'])
    df_valor_pago = df_valor_pago.apply(pd.to_numeric, errors='coerce')

def ocorrencia():
    global df_ocorrencia


    ls_ocorrencia = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:  # IGNORANDO HEADER E TRAILLER

            element = i[108:110]
            ls_ocorrencia.append(element)

    df_ocorrencia = pd.DataFrame(ls_ocorrencia, columns=['ocorrencia'])

def motivo():
    global df_motivo


    ls_motivo = []
    with open(gf.ret_file_path, 'r') as ret_file1:

        for i in ret_file1.readlines()[1:-1]:  # IGNORANDO HEADER E TRAILLER

            element = i[318:328]
            ls_motivo.append(element)

    df_motivo = pd.DataFrame(ls_motivo, columns=['motivo'])

def file_fitter():
    global df_final


    file_reader()
    nosso_numero()
    # seu_numero()
    dt_vencimento()
    valor_titulo()
    dt_ocorrencia()
    valor_pago()
    ocorrencia()
    motivo()

    df_final = df_nosso_numero
    # df_final["seu_numero"] = df_seu_numero
    df_final["dt_vencimento"] = df_dt_vencimento
    df_final["valor_titulo"] = df_valor_titulo
    df_final["dt_ocorrencia"] = df_dt_ocorrencia
    df_final["valor_pago"] = df_valor_pago
    df_final["ocorrencia"] = df_ocorrencia
    df_final["motivo"] = df_motivo

    print(df_final)

def out_resume():

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

    global trailler_variables_dict

    with open(gf.ret_file_path, 'r') as ret_file1:

        if money == 'on':

            for i in ret_file1.readlines()[-1:]:

                value = i[y:z-2]+"."+i[z-2:z]
                trailler_variables_dict.update({x:value})
        else:

            for i in ret_file1.readlines()[-1:]:

                value = i[y:z]
                trailler_variables_dict.update({x:value})

#depende da fille_fitter(), fille_fitter() deve ser invocada antes
#Isso acontece pois fille_fitter invoca file_reader

def trailler_fitter():

    trailler_reader('qtde_registros_(02)', 57, 62, money='off')
    trailler_reader('valor_registrado_(02)', 62, 74, money='on')
    trailler_reader('qtde_liquidado_(06)', 86, 91, money='off')
    trailler_reader('valor_liquidado_(06)', 74, 86, money='on')
    #NECESSÁRIO SOMAR VALOR LIQUIDADO TOTAL DE OUTRAS OCORRENCIAS ex:17
    trailler_reader('qtde_baixa_(09e10)', 103, 108, money='off')
    trailler_reader('valor_baixado_(09e10)', 108, 120, money='on')

def out_trailler():


    trailler_file = open("./trailler.txt",'w')
    trailler_file.write("Leitura do Trailler, ultima linha do arquivo:\n")

    for k,v in trailler_variables_dict.items():

        trailler_file.write(f'{k} : {v}\n')

    trailler_file.close()

if __name__ == '__main__':

    file_fitter()
    out_resume()
    trailler_fitter()
    out_trailler()


