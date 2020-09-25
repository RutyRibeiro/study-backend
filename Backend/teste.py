import cv2
import uteis

cam = cv2.VideoCapture('me.mp4')
cap = cv2.VideoCapture(0)
img = cv2.imread('marllon.jpg')

# uteis.captura(cam)
# uteis.treinaAlgoritmo()
resp = uteis.reconheceFoto(img)
# resp = uteis.reconheceVideo(cap)

resp1 = uteis.sit(resp)
print (f'Situação: {resp1}')

