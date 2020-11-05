import os, sys

sys.path.append('../Database')

def printErro(nomeArq,nomeFunc,err):
    print(f'Arquivo {nomeArq} - Função: {nomeFunc} - Erro: {err} - linha: {err.__traceback__.tb_lineno}')