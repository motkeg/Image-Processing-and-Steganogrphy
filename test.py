from PIL.Image import *
from PIL.ImageOps import *
import binascii


img=open("d1.png")
img2=open("d2.png")




def getByts(ch):
    num =ord(ch)
    res=[0]*8
    for i in xrange(8):
        if(num % 2 ) !=0:
            res[i]=1
        num/=2
    return res        


def Combine(pxl,bits):
    assert len(pxl)==len(bits) ,"length mismach"
    pxl=list(pxl)
    for i in xrange(len(pxl)): 
        even= 2*(pxl[i]/2)
        if bits[i]:
            even+=1
        pxl[1]=even
    return tuple(pxl)


def MassegeEncode2(img,msg):
    #img.show()
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
    img.save('C:\Users\USER\Desktop\OUTStringHide.png')    
    #img.show()
    #return img


        
def MassegeDecode2(img):
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
    #data.save('C:\Users\USER\Desktop\OUTImageHide.png')        
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
    return data                  



def HideString_img(img,msg):
    if len(msg)%3 !=0:
        res=len(msg)%3
        for i in range((len(msg)%3)+1):
            msg += "X"
    temp=new('RGBA',(1,len(msg)/3),(255, 0, 0, 0))
    temp.putpixel((0,0), (255,res,len(msg)/3))
    for i in range(1,(len(msg)/3),3):
        r,g,b=ord(msg[i]),ord(msg[i+1]),ord(msg[i+2])
        temp.putpixel((0,i),(r,g,b))
    temp.show()    



def ViewChange(source,tar,s=1,b=0):
    assert source.size==tar.size ,"Size missmach!"
    temp=source
    pxlarry=[]
    binarypxl=[]
    for x in range(temp.size[0]):
        for y in range(temp.size[1]):
            p = source.getpixel((x, y))
            q = tar.getpixel((x, y))
            if p!=q:
                pxlarry.append((p,q))
                temp.putpixel((x,y),(255,255,255))
                #P,Q=map(bin,p),map(bin,q)
                #binarypxl.append( (P[0][2:]+P[1][2:]+P[2][2:],Q[0][2:]+Q[1][2:]+Q[2][2:] ) )
                binarypxl.append((map(bin,p),map(bin,q)))
                if s==1:
                    if(p[0]!=q[0]):
                        print "index({0},{1}) has change in RED".format(x,y)
               
                    if(p[1]!=q[1]):
                        print "index({0},{1}) has change in GREEN".format(x,y)
               
                    if(p[2]!=q[2]):
                        print "index({0},{1}) has change in BLUE".format(x,y)
                    
                
    temp.show()
    if b:
        return binarypxl
    return pxlarry

def binaryDetect(binarypxl, opt='0'):
    arr=[]
    for i in range(len(binarypxl)):
        for j in range(3):
            string=""
            if binarypxl[i][0]!=binarypxl[i][1]:
                if opt in ('0','1'):
                    for k,t in zip(binarypxl[i][0][j][2:] , binarypxl[i][1][j][2:]):
                    
                        if k==t:
                            string+=opt
                        else:
                            string+=t
                elif opt in ('-','+'):
                    if opt=='-':
                        print ""
                    #    string = bin(abs(int(binarypxl[i][0][j],2)-int(binarypxl[i][1][j],2)))
                    #if opt=='+':
                    #    string = bin(abs(int(binarypxl[i][0][j],2)+int(binarypxl[i][1][j],2)))        
            if string!="":            
                arr.append(string) 
    print "Done!"                     
    return arr                
        
'''-----------------------------------------------------------------------------------------'''
def Main():
    arr=ViewChange(img2,img,0,1)
    print arr
    arrB= binaryDetect(arr,'0')
    print arrB
    s1=""
    s2=""
    for c in arrB:
        s1+=str(int(c,2))+'/'
        #s2+=chr(int(c,2))
    print "int:  " ,s1
    print "ascii:  " ,s2
 
Main()   

#HideString_img(img,"Motiii Gadiannn SCE")

'''MassegeEncode2(img,"Moti Gadiannnnnnnnnn SCE_ASHDOD")
print(MassegeDecode2(img)) 
Hideimage(img2,img) 
#Extractimage(img3)'''
'''MassegeEncode2(img,"234/255/122")
print(MassegeDecode2(img))               
print(MassegeDecode2(img))'''                    