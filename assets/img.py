from PIL import Image
import sys, os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def ImgFormat():
    print("aviso: el programa convierte imagenes a RGBA de png, pesan mas\nuse en el directorio de la imagen")
    print("ingrese nombre de la imagen (con extension):")
    name=input()
    print("ingrese nombre de salida (sin extension):")
    salida=input()
    thisFilePath = os.path.abspath(__file__)
    thisFolderPath = os.path.dirname(thisFilePath)
    sprite= os.path.join(thisFolderPath,str(name))
    image = Image.open(sprite)
    image2=image.convert('RGBA')
    image2.save(os.path.join(thisFolderPath,str(salida)+".png"),'PNG')    
ImgFormat()