import image_handler as ih
import os
from copy import deepcopy


class weight_vector:
    def __init__(self,name,vector) -> None:
        self.name=name
        self.vector=vector




root_path="Weight\\"
filenames=os.listdir(root_path)
while True:
    pesos=list()
    for file in filenames:#Iteramos entre los nombres de  archivos de pesos
            print("Archivo "+file+'\n')
            file=os.path.join(root_path, file)
            with open(file, 'r') as f: #leemos cada archivo y dividimos todo
                line = f.read()
                numbers = line.split()
                weight = [int(num) for num in numbers]#Calculamos el arreglo de pesos
            
            aux=weight_vector(os.path.basename(file),weight)
            pesos.append(deepcopy(aux))
    print(str(len(pesos))+" Pesos guardados")
    image=ih.Image()
    input_image=input("Introduce la ruta de la imagen a analizar")
    image.read_img(input_image,0,48,36)
    Image_filtered=image.canny(100,300)
    sums=[]
    for struct in pesos:
        name,vector=struct.name,struct.vector
        sum=0
        for i in range(len(vector)):
            if Image_filtered.byte[i]==255:
                sum+=vector[i]
        sums.append((sum,name))
    Image_filtered.show_image()
    for result in sums:
        print(result[1]+ " con resultado "+str(result[0]))
    inip=input()
    if inip==1:
        exit
            
            
        
            
            
    
            