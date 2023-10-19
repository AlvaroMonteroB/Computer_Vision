import cv2 as cv
import os
import numpy as np


class Image:
    def __init__(self):
        self.imagen=None#Matriz de la imagen
        self.mode:int=None#Modo de lectura
        self.byte=None#Bytes de la imagen
        self.width=None
        self.height=None
    def read_img(self,name,mode:int):#Leer imagen en modo estandar, si resize=true hay que reeescalarla
        self.imagen=cv.imread(name,mode)
        self.height,self.width=self.imagen.shape
        if mode==0:
            self.mode=1
        elif mode==1:
            self.mode=3
        self.byte=self.imagen.tobytes()

    def read_img(self,name,mode,scale_factor):#Leer con un factor de escala 
        self.imagen=cv.imread(name,mode)
        height,width=self.imagen.shape
        self.imagen=cv.resize(self.imagen,(int(width/scale_factor),int(height/scale_factor)))
        self.height,self.width=self.imagen.shape
        if mode==0:
            self.mode=1
        elif mode==1:
            self.mode=3
        self.byte=self.imagen.tobytes()

    def read_img(self,name,mode,height,width):#leer escalando a valores definidos
        self.imagen=cv.imread(name,mode)
        self.imagen=cv.resize(self.imagen,(width,height))
        self.height,self.width=self.imagen.shape
        if mode==0:
            self.mode=1
        elif mode==1:
            self.mode=3
        self.byte=self.imagen.tobytes()

    def assign_img(self,input):#Asignamos una nueva imagen
        self.imagen=input
        self.byte=self.imagen.tobytes()
        self.height,self.width=self.imagen.shape

    def show_image(self):
        cv.imshow("imagen",self.imagen)
        cv.waitKey(0)
        cv.destroyAllWindows()


    def assign_vector(self,width,height,input,mode,img:bool):#Asignamos vector calculando la imagen
        self.mode=mode
        self.byte=input 
        self.width=width
        self.height=height
        if img:
            self.imagen=np.frombuffer(self.byte, dtype=np.uint8)
            self.imagen=np.reshape(self.imagen, (self.height,self.width, 1))


    
    
    def convolution(self,kernel):
        new_matrix=np.zeros((self.height,self.width))
        kernel_size=kernel.shape[0]
        
        for j in range(self.height):
            for i in range(self.width):
                sum=0
                for y in range(kernel_size):
                    for x in range(kernel_size):
                        imagen_y=j-kernel_size//2+y
                        imagen_x=i-kernel_size//2+x
                        if 0 <= imagen_y < self.height and 0 <= imagen_x < self.width:
                            sum+=self.imagen[imagen_y,imagen_x]*kernel[y,x]
                            
                new_matrix[j,i]=(sum//((kernel_size)**2))
             
        output=Image()
        output.assign_img(new_matrix)
        return output
           
    
    
    

    def canny(self,thr1,thr2):#Algoritmo de canny
        output=Image()
        borde=cv.Canny(self.imagen,thr1,thr2)
        output.assign_img(borde)
        return output
        

        