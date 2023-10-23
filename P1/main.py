import image_handler as ih


img1=ih.Image("IMG_6697.bmp")
img2=ih.Image("IMG_6700.bmp")
img3=img1.and_operation(img2)
img3.to_file()
print("bien")
