import cv2
import numpy as np
import NameFind             # importa módulo NameFind
import os                                               # importing the OS for path
from PIL import Image                                   # importing Image library

def captura (video,nome):

    face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')  # algoritmo detector de faces, a função classifier carrega o arquivo xml
    eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')  # algoritmo detector de olhos

    ID = NameFind.AddName(nome)
    cam = cv2.VideoCapture(video)  # carrega a camera a ser usada, 0 significa que usava a camera embutida, webcam
    Count = 0

    try:
        while Count < 50:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 # converte a imagem para a escala cinza, isso ajuda no reconhecimento
            if np.average(gray) > 110:                                   # testa se o brilho da imagem é satisfatorio
                faces = face_cascade.detectMultiScale(gray, 1.3,5)       # detecta as faces na imagem, guarda lista com as coordenadas da face(x,y,largura,altura)
                for (x, y, w, h) in faces:
                    FaceImage = gray[y - int(h / 2): y + int(h * 1.5),x - int(x / 2): x + int(w * 1.5)]  # a imagem é cortada de forma a capturar apenas a face
                    Img = (NameFind.DetectEyes(FaceImage))
                    cv2.putText(gray, "FACE DETECTED", (x + int((w / 2)), y - 5), cv2.FONT_HERSHEY_DUPLEX, .4, [255, 255, 255])  # texto plotado caso detecte rosto
                    if Img is not None:
                        frame = Img  # Show the detected faces
                    else:
                        frame = gray[y: y + h, x: x + w]
                    cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", frame)
                    cv2.waitKey(300)
                    cv2.imshow("CAPTURED PHOTO", frame)  # show the captured image
                    Count = Count + 1
            cv2.imshow('Face Recognition System Capture Faces', gray)  # Show the video
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        print('FACE CAPTURE FOR THE SUBJECT IS COMPLETE')
        cam.release()
        cv2.destroyAllWindows()
        mensagem={}
        mensagem['status']='usuário cadastrado'
        mensagem['id'] = ID
        return mensagem
    except:
        mensagem={}
        mensagem['status']='Ocorreu um erro durante a captura facial, tente novamente'
        return mensagem


def treinaAlgoritmo():
    EigenFace = cv2.face.EigenFaceRecognizer_create(15)  # creating EIGEN FACE RECOGNISER
    FisherFace = cv2.face.FisherFaceRecognizer_create(2)  # Create FISHER FACE RECOGNISER
    LBPHFace = cv2.face.LBPHFaceRecognizer_create(1, 1, 7, 7)  # Create LBPH FACE RECOGNISER

    path = 'dataSet'  # path to the photos

    def getImageWithID(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        FaceList = []
        IDs = []
        for imagePath in imagePaths:
            faceImage = Image.open(imagePath).convert('L')  # Open image and convert to gray
            faceImage = faceImage.resize((110, 110))  # resize the image so the EIGEN recogniser can be trained
            faceNP = np.array(faceImage, 'uint8')  # convert the image to Numpy array
            ID = int(os.path.split(imagePath)[-1].split('.')[1])  # Retreave the ID of the array
            FaceList.append(faceNP)  # Append the Numpy Array to the list
            IDs.append(ID)  # Append the ID to the IDs list
            cv2.imshow('Training Set', faceNP)  # Show the images in the list
            cv2.waitKey(1)
        return np.array(IDs), FaceList  # The IDs are converted in to a Numpy array

    IDs, FaceList = getImageWithID(path)

    # ------------------------------------ TRAING THE RECOGNISER ----------------------------------------
    print('TRAINING......')
    EigenFace.train(FaceList, IDs)  # The recongniser is trained using the images
    print('EIGEN FACE RECOGNISER COMPLETE...')
    EigenFace.save('Recogniser/trainingDataEigan.xml')
    print('FILE SAVED..')
    FisherFace.train(FaceList, IDs)
    print('FISHER FACE RECOGNISER COMPLETE...')
    FisherFace.save('Recogniser/trainingDataFisher.xml')
    print('Fisher Face XML saved... ')
    LBPHFace.train(FaceList, IDs)
    print('LBPH FACE RECOGNISER COMPLETE...')
    LBPHFace.save('Recogniser/trainingDataLBPH.xml')
    print('ALL XML FILES SAVED...')

    cv2.destroyAllWindows()
def reconheceFoto(img):
    face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
    eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')
    spec_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye_tree_eyeglasses.xml')

    # FACE RECOGNISER OBJECT
    LBPH = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 20)
    EIGEN = cv2.face.EigenFaceRecognizer_create(10, 5000)
    FISHER = cv2.face.FisherFaceRecognizer_create(5, 500)

    # Load the training data from the trainer to recognise the faces
    LBPH.read("Recogniser/trainingDataLBPH.xml")
    EIGEN.read("Recogniser/trainingDataEigan.xml")
    FISHER.read("Recogniser/trainingDataFisher.xml")

    # ------------------------------------  PHOTO INPUT  -----------------------------------------------------
    NAME=''
    img= cv2.imread(img)
    # gray = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the Camera to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)  # Detect the faces and store the positions
    print(faces)
    try:
        for (x, y, w, h) in faces:  # Frames  LOCATION X, Y  WIDTH, HEIGHT

            Face = cv2.resize((gray[y: y + h, x: x + w]), (110, 110))  # The Face is isolated and cropped

            ID, conf = LBPH.predict(Face)  # LBPH RECOGNITION
            print(ID)
            NAME = NameFind.ID2Name(ID, conf)
            NameFind.DispID(x, y, w, h, NAME, gray)

        # cv2.imshow('LBPH Face Recognition System', gray)  # IMAGE DISPLAY
        # cv2.destroyAllWindows()

        return {'nome':NAME, 'id':ID}
    except Exception as e:
       print(e)
       return{'erro':'Face não reconhecida'}

#
# def reconheceVideo(cap):
#
#     face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')  # Classifier "frontal-face" Haar Cascade
#     eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')  # Classifier "eye" Haar Cascade
#
#     recognise = cv2.face.EigenFaceRecognizer_create(15, 4000)  # creating EIGEN FACE RECOGNISER
#     recognise.read("Recogniser/trainingDataEigan.xml")  # Load the training data
#     NAME=''
#     ID = 0
#     while True:
#         ret, img = cap.read()  # Read the camera object
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the Camera to gray
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect the faces and store the positions
#         for (x, y, w, h) in faces:  # Frames  LOCATION X, Y  WIDTH, HEIGHT
#             # ------------ BY CONFIRMING THE EYES ARE INSIDE THE FACE BETTER FACE RECOGNITION IS GAINED ------------------
#             gray_face = cv2.resize((gray[y: y + h, x: x + w]), (110, 110))  # The Face is isolated and cropped
#             eyes = eye_cascade.detectMultiScale(gray_face)
#             for (ex, ey, ew, eh) in eyes:
#                 ID, conf = recognise.predict(gray_face)  # Determine the ID of the photo
#                 NAME = NameFind.ID2Name(ID, conf)
#                 NameFind.DispID(x, y, w, h, NAME, gray)
#         cv2.imshow('EigenFace Face Recognition System', gray)  # Show the video
#         if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit if the key is Q
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#
#     return NAME

def sit(resp):

    if resp == "Face Not Recognised":
        return 'Pessoa não cadastrada!'
    elif resp == "":
        return 'Face não reconhecida'
    else:
        return 'Pessoa cadastrada!'

