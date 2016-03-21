from PIL.Image import *
from PIL.ImageOps import *
import binascii





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
                    
                
    #temp.show()
    if b:
        return binarypxl
    return pxlarry

def binaryDetect(binarypxl, opt='0'):
    arr=[]
    for i in range(len(binarypxl)):
        for j in range(3):
            string=""
            if binarypxl[i][0][j]!=binarypxl[i][1][j]:
                if opt in ('0','1'):
                    for k,t in zip(binarypxl[i][0][j][2:] , binarypxl[i][1][j][2:]):
                        if k==t:
                            string+=opt
                        else:
                            string+=t
                elif opt in ('-','+'):
                    if opt=='-':
                        string = bin(abs(int(binarypxl[i][0][j],2)-int(binarypxl[i][1][j],2)))
                    #if opt=='+':
                    #    string = bin(abs(int(binarypxl[i][0][j],2)+int(binarypxl[i][1][j],2)))        
            if string!="":            
                arr.append(string) 
    print "                         binaryDetect - output:" 
    s1,s2="",""           
    for c in arr:
        s1+=str(int(c,2))+'/'
        s2+=chr(int(c,2))
    print "int:  " ,s1
    print "ascii:  " ,s2            
    return arr                               
    



def binaryDetect2(binarypxl):
    arr=[]
    for i in range(len(binarypxl)):
        for j in range(3):
            if binarypxl[i][0][j][2:]!=binarypxl[i][1][j][2:]:
                arr.append(binarypxl[i][1][j])
                
                
    print "                             binaryDetect2 - output:" 
    s1,s2="",""           
    for c in arr:
        s1+=str(int(c,2))+'/'
        s2+=chr(int(c,2))
    print "int:  " ,s1
    print "ascii:  " ,s2            
    return arr            



def binaryDetect3(binarypxl,opt='0'):
    arr=[]
    arr2=[]
    for i in range(len(binarypxl)):
        x,y= "",""
        for j in range(3):
            x,y=x+binarypxl[i][0][j][2:],y+binarypxl[i][1][j][2:]
            
        arr.append((x,y))
    for i in range(len(arr)):
        string="" 
        if arr[i][0]!=arr[i][1]:
            for k,t in zip(arr[i][0][2:] , arr[i][1][2:]):
                if k==t:
                    string+=opt
                else:
                    string+=t
            arr2.append(string)   
        
                
                
    print "                            binaryDetect3 - output:" 
    s1,s2="",""           
    for c in arr2:
        s1+=str(int(c,2))+'/'
        #s2+=chr(int(c,2))
    print "int:  " ,s1
    print "ascii:  " ,s2            
    return arr2            


def Main():
    img=open("d1.png")
    img2=open("d2.png")
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    arr=ViewChange(img2,img,0,1)
    #print arr
    binaryDetect(arr,'1')
    #binaryDetect2(arr)
    #print arrA
    binaryDetect3(arr,'1')
    
    #print arrB
    
    
 
Main()                