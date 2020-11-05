import inspect
from werkzeug.utils import secure_filename
import cv2
import tratamentoDeErros
import reco_Modulos

def cadastro(body):
    response={}
    if 'nome' not in body or 'video' not in body:
        response['erro'] = 'Você esta passano a propriedade errada é apenas aceito NOME e VIDEO'
        return  response
    elif body['nome'] == ''or body['nome'] is None:

        response['erro'] = 'Nome obrigatório!'
        return response
    elif body['video'] == '' or body['video'] is None:

        response['erro'] = 'Video obrigatório!'
        return response
    else:
        response = reco_Modulos.captura(body['video'], body['nome'])
        return response

def login(img):
    response={}
    
    if img == '' or img is None:
        
        response['erro'] = 'Você esta passando a propriedade nula ou vazia'
        
        return  response
    
    else:
        img=cv2.imread(img)
        user = uteis.reconheceFoto(img)
        
        if 'nome' not in user:
            response = user
        
        else:
            response['nome']=user['nome']
            response['conteudo'] = reco_Modulos.buscaConteudoUser(user['id'])

        return response

def download(file):
     try:
         filename = secure_filename(file.filename)
         file.save(os.path.join('./',secure_filename(filename)))
         return filename
     except Exception as e:
        tratamentoDeErros.printErro(os.path.basename(__file__),inspect.getframeinfo(inspect.currentframe())[2],e)
        return 'Ocorreu um erro no download'

