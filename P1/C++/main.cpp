#include "image_handler.h"


int main(){
    cout<<"Empezando operaciones\n";
    string path="D:/Repositorios/Computer_Vision/P1/C++/IMG_6697.bmp";
    string path2="D:/Repositorios/Computer_Vision/P1/C++/IMG_6700.bmp";
    Image *img1=new Image(path);
    Image *img2=new Image(path2);
    Image *img3=img1->xor_operation(img2);
    img3->to_file();
    delete img3;
    cout<<"Bien\n";

    return 0;
}