import cv2, sys
import reco_Modulos,os
 
# print(os.listdir())
# cam = cv2.VideoCapture('Marllon.mp4')
# cap = cv2.VideoCapture('./videosClara.mp4')
# img = cv2.imread('l.jpg')

# resp = reco_Modulos.captura(cap,'Clara')
resp= reco_Modulos.reconhece('./Fotos/Ruty.jpg')

print (resp)

