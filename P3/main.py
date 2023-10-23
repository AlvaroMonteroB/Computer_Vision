import image_handler as ih
import numpy as np

img=ih.Image()
img.read_img(r'C:\Users\diavl\OneDrive\Escritorio\Repositorios\Computer_Vision\anorlondo.jpg',1,500,500)


kernel_suavizado=np.array([[-1,-1,-1],
                           [-1,9,-1],
                           [-1,-1,-1]])

kernel=np.array([[0,1,0],#Deteccion de bordes
                 [1,-4,1],
                 [0,1,0]])
sobel_vert=np.array([[1,0,-1],
                     [1,0,-1],
                     [1,0,-1]])

kernel2=np.array([[-2,-1,0],#Repujado
                  [-1,1,1],
                  [0,1,2]])
newimg=img.convolution(kernel_suavizado)
newimg.show_image()
img2=newimg.convolution(kernel)
img2.show_image()