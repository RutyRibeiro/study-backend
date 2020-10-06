import cv2
import uteis
 

cam = cv2.VideoCapture('Marllon.mp4')
cap = cv2.VideoCapture(0)
img = cv2.imread('marllon.jpg')

#resp= uteis.captura(nome='Marllon')
# uteis.treinaAlgoritmo()
# resp = uteis.reconheceFoto(img)
resp = uteis.reconheceVideo(cap)

print (resp)

