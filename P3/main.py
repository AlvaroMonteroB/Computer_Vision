import image_handler as ih
import numpy as np

img=ih.Image()
img.read_img(r'C:\Users\diavl\OneDrive\Escritorio\Repositorios\Computer_Vision\5image.jpg',0,100,100)


kernel_suavizado=np.array([[]])

kernel=np.array([[0,1,0],
                 [1,-4,1],
                 [0,1,0]])
kernel2=np.array([[-2,-1,0],
                  [-1,1,1],
                  [0,1,2]])
newimg=img.convolution(kernel2)
newimg.show_image()
img2=newimg.convolution(kernel)
img2.show_image()