#Space to specify a getfile method, in here you want to specify how getting the file
#The functions here need to be change in acord with the necessity
import os

ret_file_path = ''

def getfile():
    global ret_file, ret_file_path


    ret_file = input("Digite o caminho do arquivo: \n")
    ret_file_path =  os.path.join(ret_file)

    return ret_file_path

if __name__ == '__main__':
    getfile()
