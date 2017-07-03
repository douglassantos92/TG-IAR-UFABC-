
import time
import serial

import socket
import io
import sys

import cv2
import time
import urllib
import numpy as np
import urllib.request
from PIL import Image
import piexif


def main(args):
     
    nFrames = 48

    i = 0

    while(i != 48):
        url = 'http://172.31.33.132:8080/shot.jpg'
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        print ("/data/imagenTeste",int(i),".png")
        file = str("/data/imagenTeste"+str(i)+".jpg")
        img=cv2.imdecode(imgNp,-1)
        cv2.imshow('Foto',img)
        k = cv2.waitKey(100)
        cv2.imwrite(file,img)
        dir="/data/"
        image=str("imagenTeste"+str(i)+".jpg")
        image_dir=dir+image
        dir2="/home/pi/Pictures/"
        image2="Imagem1.jpg"
        image_dir2=dir2+image2
        piexif.transplant(image_dir2,image_dir)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # Iniciando conexao serial
        comport = serial.Serial('/dev/ttyACM0', 9600)
    #comport = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # Setando timeout 1s para a conexao
 
        PARAM_CARACTER='t'
        PARAM_ASCII=str(chr(116))       # Equivalente 116 = t
 
    # Time entre a conexao serial e o tempo para escrever (enviar algo)
        time.sleep(1.8) 
 
        comport.write(PARAM_ASCII)
 
        VALUE_SERIAL=comport.readline()
 
        print '\nRetorno da serial: %s' % (VALUE_SERIAL)
 
    # Fechando conexao serial
        comport.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        i=i+1
        imgResp.close()
            
            
     
    cv2.destroyAllWindows()
    return 0
 
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Conectado por', cliente   
##### # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

##### # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    print 'Finalizando conexao do cliente', cliente
    con.close()

