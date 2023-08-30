import numpy as np



class Image:
    def __init__(self,path=None,image_n_data=None) -> None:
        if not path and image_n_data:
            self.constructor_output(image_n_data)
        if path:
            with open(path,'rb') as img_buffer:
                raw_img=img_buffer.read()
                file_array=np.frombuffer(raw_img,dtype=np.uint8)
                header=file_array[:14]
                header_info=file_array[14:54]
                self.header=file_array[:54]
                self.img_data=np.frombuffer(file_array[54:],dtype=np.uint8)#Datos de los pixeles
                self.width=np.frombuffer(header_info[4:8],dtype=np.uint32)# 4 , 5 , 6 , 7
                self.height=np.frombuffer(header_info[8:12],dtype=np.uint32)# 8 , 9, 10 , 11
                self.bitspp=np.frombuffer(header_info[14:16],dtype=np.uint16)#14 , 15
            
    def constructor_output(self,image_n_data):
        self.img_data,self.width,self.height,self.bitspp,self.header=image_n_data
        
        
    def and_operation(self, input):
        if(input.bitspp==self.bitspp and input.width==self.width and input.height==self.height):
            buffer=input.img_data & self.img_data
        return Image(None, (buffer,self.width,self.height,self.bitspp,self.header))
    
    def to_file(self):
        with open ("Result.bmp",'wb') as archivo:
            file=(self.header.tobytes()+self.img_data.tobytes())
            archivo.write(file)
            
        
        
        
        


