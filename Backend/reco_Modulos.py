# from Database import connection
import tratamentoDeErros
import cv2
import inspect
import os
import numpy as np
import math
import face_recognition
from os.path import isfile, join

path = './dataSet'


nomeArq = os.path.basename(__file__)

glass_cas = cv2.CascadeClassifier('Haar/haarcascade_eye_tree_eyeglasses.xml') # Classifierde "eye" Haar Cascade
face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')  # algoritmo detector de faces, a função classifier carrega o arquivo xml


def procuraNome(ID):
    if ID>=1 and ID<=last_string:
        NameString=connection.select(ID)
    else:
        NameString = "Face não reconhecida" 

    return NameString

def AddNome(nome):
    Name=nome
    Info = open("Names.txt", "r+")
    ID = ((sum(1 for line in Info))+1)
    insereDb=connection.insert({'nome':Name,'id':ID})
    print(insereDb)
    Info.write("\n" + str(ID) + " " + "," + " " + Name )
    print ("Name Stored in " + str(ID))
    Info.close()
    return ID

def DetectaOlhos(Image):
    Theta = 0
    rows, cols = Image.shape
    glass = glass_cas.detectMultiScale(Image)                                               # This ditects the eyes
    for (sx, sy, sw, sh) in glass:
        if glass.shape[0] == 2:                                                             # The Image should have 2 eyes
            if glass[1][0] > glass[0][0]:
                DY = ((glass[1][1] + glass[1][3] / 2) - (glass[0][1] + glass[0][3] / 2))    # Height diffrence between the glass
                DX = ((glass[1][0] + glass[1][2] / 2) - glass[0][0] + (glass[0][2] / 2))    # Width diffrance between the glass
            else:
                DY = (-(glass[1][1] + glass[1][3] / 2) + (glass[0][1] + glass[0][3] / 2))   # Height diffrence between the glass
                DX = (-(glass[1][0] + glass[1][2] / 2) + glass[0][0] + (glass[0][2] / 2))   # Width diffrance between the glass

            if (DX != 0.0) and (DY != 0.0):                                                 # Make sure the the change happens only if there is an angle
                Theta = math.degrees(math.atan(round(float(DY) / float(DX), 2)))            # Find the Angle
                print ("Theta  " + str(Theta))

                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), Theta, 1)                 # Find the Rotation Matrix
                Image = cv2.warpAffine(Image, M, (cols, rows))
                # cv2.imshow('ROTATED', Image)                                              # UNCOMMENT IF YOU WANT TO SEE THE

                Face2 = face_cascade.detectMultiScale(Image, 1.3, 5)                                # This detects a face in the image
                for (FaceX, FaceY, FaceWidth, FaceHeight) in Face2:
                    CroppedFace = Image[FaceY: FaceY + FaceHeight, FaceX: FaceX + FaceWidth]
                    return CroppedFace

def captura (video,nome): 
    # cam = cv2.VideoCapture(video)  # carrega a camera a ser usada, 0 significa que usava a camera embutida, webcam
    
    cam=video
    
    Count=0
    mensagem={}
    ID = connection.consultaID() + 1   
    
    try:
        while Count < 3:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 # converte a imagem para a escala cinza, isso ajuda no reconhecimento
            
            if np.average(gray) > 110:                                   # testa se o brilho da imagem é satisfatorio
                faces = face_cascade.detectMultiScale(gray, 1.3,5)       # detecta as faces na imagem, guarda lista com as coordenadas da face(x,y,largura,altura)
                for (x, y, w, h) in faces:
                    
                    FaceImage = gray[y - int(h / 2): y + int(h * 1.5),x - int(x / 2): x + int(w * 1.5)]  # a imagem é cortada de forma a capturar apenas a face
                    
                    Img = (DetectaOlhos(FaceImage))
                    
                    if Img is not None:
                        frame = Img  # Show the detected faces
                    else:
                        frame = gray[y: y + h, x: x + w]
                    
                    cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", frame)
                    cv2.waitKey(300)
                    
                    Count = Count + 1

        AddNome(nome)
        mensagem['status']='usuário cadastrado'
        mensagem['id'] = ID
        return mensagem
    
    except Exception as e:
        tratamentoDeErros.printErro(nomeArq,inspect.getframeinfo(inspect.currentframe())[2],e)

        mensagem['status']='Ocorreu um erro durante a captura facial, tente novamente'
        return mensagem

def reconhece (img):
    files = [f for f in os.listdir(path) if isfile(join(path, f))]

    imagem= face_recognition.load_image_file(img)
    imagem_encoding = face_recognition.face_encodings(imagem)[0]

    for pessoa in files:

        try:
            img_desconhecida = face_recognition.load_image_file(f'./dataSet/{pessoa}')
            img_desconhecida_encoding = face_recognition.face_encodings(img_desconhecida)[0]

            # Compara as faces
            results = face_recognition.compare_faces([imagem_encoding], img_desconhecida_encoding)
            
            if results[0]:
                print (pessoa)
        except IndexError as ie:
            print('Não consegui encontrar uma face!')
        except Exception as e:
            print('Houve algum erro!')

                
