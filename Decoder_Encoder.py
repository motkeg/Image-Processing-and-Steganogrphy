from PIL.Image import *
from PIL.ImageOps import *
import binascii
import optparse



img=open("pic1.jpg")
img2=open("trafico_11.jpg")



def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)



def MassegeHide2(img, message):
   
    assert img.mode== 'RGBA' ,"Incorrect Image Mode, Couldn't Hide"
    def encode(hexcode, digit):
        if hexcode[-1] in ('0','1', '2', '3', '4', '5'):
            hexcode = hexcode[:-1] + digit
            return hexcode
        else:
            return None
    def hex2rgb(hexcode):
        return tuple(map(ord, hexcode[1:].decode('hex')))
    def str2bin(message):
        binary = bin(int(binascii.hexlify(message), 16))
        return binary[2:]
    binary = str2bin(message) + '1111111111111110'
    
    img = img.convert('RGBA')
    datas = img.getdata()
    newData,digit,temp = [],0,''
    for item in datas:
        if (digit < len(binary)):
            newpix = encode(rgb2hex(item[0],item[1],item[2]),binary[digit])
            if newpix == None:
                newData.append(item)
            else:
                r, g, b = hex2rgb(newpix)
                newData.append((r,g,b,255))
                digit += 1
        else:
            newData.append(item)    
        img.putdata(newData)
        img.save('C:\Users\USER\workspace\Final Project\src\outputImage\OUTStringHidebinary.png')
        
        return " Hiding Completed!"
  
  
def decode(hexcode):
    if hexcode[-1] in ('0', '1'):
        #print hexcode[-1]
        return hexcode[-1]
    else:
        return None          
                    

def MassegeDecode2(img):
    binary = ''
    assert img.mode== 'RGBA' ,"Incorrect Image Mode, Couldn't Hide"
    
    def bin2str(binary):
        message = binascii.unhexlify('%x' % (int('0b'+binary,2)))
        return message
    img = img.convert('RGBA')
    datas = img.getdata()
        
    for item in datas:
        digit = decode(rgb2hex(item[0],item[1],item[2]))
        if digit == None:
            pass
        else:
            binary = binary + digit
            if (binary[-16:] == '1111111111111110'):
                print "Success"
                return bin2str(binary[:-16])

    return bin2str(binary[:-16])
 
 
 
def MassegeHide1(img,msg):
    #img.show()
    if type(msg) in (int,long):
        msg=str(msg)

    def red(img,x,y,val):
        R,G,B =img.getpixel((x,y))
        img.putpixel((x,y),(val,G,B))
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    assert len(msg)< 256 , "massege is too long!!"
    red(img,0,0,len(msg))
    i=1
    for c in msg:
        red(img,0, i,ord(c))
        i+=1
    img.save('C:\Users\USER\workspace\Final Project\src\outputImage\OUTStringHide.png')    
    #img.show()
    #return img


        
def MassegeDecode1(img):
    def getRed(img,x,y):
        R,G, B =img.getpixel((x,y))
        return R
    '''''''''''''''''''''''''''''''''''''''''' 
    numChar=getRed(img,0,0)
    msg= ""
    for i in xrange(1,numChar+1):
        msg += chr(getRed(img,0,i))
    return str(msg)              
 
 
def Hideimage(public, secret, s=4):
    assert public.size <= secret.size ,"Secret image size Missmach"
    data =public
    key = autocontrast(secret)
    for x in range(data.size[0]):
        for y in range(data.size[1]):
            p = data.getpixel((x, y))
            q = key.getpixel((x, y))
            red   = p[0] - (p[0] % s) + (s * q[0] / 255)
            green = p[1] - (p[1] % s) + (s * q[1] / 255)
            blue  = p[2] - (p[2] % s) + (s * q[2] / 255)
            data.putpixel((x, y), (red, green, blue))
    data.show()
    data.save('C:\Users\USER\workspace\Final Project\src\outputImage\OUTImageHide.png')        
    return data          
 
 
def Extractimage(from_image, s=4):
    data = from_image 
    for x in range(data.size[0]):
        for y in range(data.size[1]):
            p = data.getpixel((x, y))
            red   = (p[0] % s) * 255 / s
            green = (p[1] % s) * 255 / s
            blue  = (p[2] % s) * 255 / s
            data.putpixel((x, y), (red, green, blue))
    data.show() 
    data.save('C:\Users\USER\workspace\Final Project\src\outputImage\OUTImageHideExtract.png')       
    return data                  



#MassegeHide1(img,555)
#print(MassegeDecode1(img))
#MassegeHide2(img,"Moti Gadiannnnnnnnnn SCE_ASHDOD")
#MassegeDecode2(img)
img3=Hideimage(img2,img)
#Extractimage(img3)

