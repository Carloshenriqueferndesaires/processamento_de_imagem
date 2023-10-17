from PIL import Image

#image = Image.new("RGB",(500,500),(22,22,231))#string,(altura,largura),cor()
 

def bandeira_franca(height):
    width=3*height//2
    WRITE=(255,255,255)
    BLUE=(0, 85, 164)
    RED=(239, 65, 53)
    image=Image.new("RGB",(width,height),WRITE)
    
    offset=width//3
    for x in range(offset):
      for y in range(height):
            image.putpixel((x,y),BLUE)
            image.putpixel((x+2*offset,y),RED)
    return image

if __name__ == "__main__":
    imagem = bandeira_franca(700)
    imagem.show()