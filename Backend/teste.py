import cv2
import uteis,os
 
# print(os.listdir())
# cam = cv2.VideoCapture('Marllon.mp4')
cap = cv2.VideoCapture('preto.mp4')
# img = cv2.imread('l.jpg')

resp = uteis.captura(cap,'preto')
# uteis.treinaAlgoritmo()
# resp = uteis.reconheceFoto(img)
# resp = uteis.reconheceVideo(cap)

print (resp)

