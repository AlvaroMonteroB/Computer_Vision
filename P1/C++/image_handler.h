#include<vector>
#include<fstream>
#include <memory>
#include<iostream>
#include<string>
using namespace std;

typedef struct{
    char signature[2];
    uint32_t fileSize;
    uint16_t reserved1;
    uint16_t reserved2;
    uint32_t dataOffset;
    uint32_t headerSize;
    int32_t width;
    int32_t height;
    uint16_t planes;
    uint16_t bitsPerPixel;
    uint32_t compression;
    uint32_t imageSize;
    int32_t xPixelsPerMeter;
    int32_t yPixelsPerMeter;
    uint32_t colorsUsed;
    uint32_t importantColors;
}BMP_H;

class Image{
    private:
        BMP_H header;
        vector<uint8_t>img_data;
    public:
        Image(string path){
            ifstream stream(path,ios::binary);
            stream.read(reinterpret_cast<char*>(&header),sizeof(BMP_H));
            img_data.resize(header.imageSize);
            stream.seekg(header.dataOffset);
            stream.read(reinterpret_cast<char*>(img_data.data()),header.imageSize);
        }
        Image(BMP_H _header, vector<uint8_t>data_pixels){
            header=_header;
            img_data=data_pixels;
        }

    vector<uint8_t>get_data(){
        return img_data;
    }

    int32_t get_width(){
        return header.width;
    }
    int32_t get_height(){
        return header.height;
    }

    uint16_t get_channels(){
        return header.bitsPerPixel;
    }

    Image *xor_operation(Image *&input){
        cout<<"xor\n";
        vector<uint8_t> output;
        if(input->get_height()==header.height&&input->get_width()==header.width&&header.bitsPerPixel==input->get_channels()){
        vector<uint8_t>aux=input->get_data();
        for(size_t i=0; i<img_data.size();i++){
            output.push_back(img_data[i]^aux[i]);
            }
        Image *salida=new Image(header,output);
        return salida;
        }
        return nullptr;
    }

    void to_file(){
        cout<<"Escribiendo\n";
        ofstream F("result.bmp",ios::binary);
        F.write(reinterpret_cast<char*>(&header),sizeof(BMP_H));
        F.write(reinterpret_cast<char*>(img_data.data()),img_data.size());

    }

};