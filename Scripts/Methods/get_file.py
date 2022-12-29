"""Especifíca o método que será utilizado para captar o arquivo a ser lido.

Contém um método genérico para captação local desse arquivo.
Pode ser reescrito de acordo com a impementação.
"""
import os

ret_file_path = ''

def getfile():
    """Médoto genérico para captação do arquivo.

    Input -- path do arquivo
    retorna o próprio path"""
    global ret_file, ret_file_path
    ret_file = input("Digite o caminho do arquivo: \n")
    ret_file_path =  os.path.join(ret_file)

    return ret_file_path

if __name__ == '__main__':
    getfile()
