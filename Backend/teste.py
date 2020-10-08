import cv2
import uteis
 

cam = cv2.VideoCapture('Marllon.mp4')
cap = cv2.VideoCapture('Ruty.mp4')
img = cv2.imread('imagemUsuario.png')

# resp= uteis.captura('Ruty.mp4','Ruty')
# uteis.treinaAlgoritmo()
resp = uteis.reconheceFoto(img)
# resp = uteis.reconheceVideo(cap)

print (resp)

