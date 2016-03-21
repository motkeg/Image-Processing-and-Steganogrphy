
from PIL.Image import *
from PIL import ImageFilter 
import matplotlib
import matplotlib.pyplot as plt 
from numpy import *



"------------------------------------------------------------"
def Histogram(img):
    R,G,B=[0]*256,[0]*256,[0]*256
    pxls=img.load()
    if(img.mode=="RGB"):
        for x in range (img.size[0]):
            for y in range(img.size[1]):
                R[pxls[x,y][0]]+=1
                G[pxls[x,y][1]]+=1
                B[pxls[x,y][2]]+=1
                #print(pxls[x,y])
        plt.title('Histogram of Img')
        plt.plot(R)
        plt.plot(G) 
        plt.plot(B)
        plt.xlim()  
        plt.grid(True)
        plt.show()
         
        plt.hist(R, 40, normed=3, facecolor='r', alpha=1)
        plt.hist(G, 40, normed=3, facecolor='g', alpha=1)
        plt.hist(B, 40, normed=3, facecolor='b', alpha=1)
        plt.grid(True)
        plt.show()
        #print(R,G,B)
        
    if(img.mode!="RGB"):
        h=[0]*256     
        for x in range (img.size[0]):
            for y in range(img.size[1]): 
                h[pxls[x,y]]+=1
                plt.hist(h, 40, normed=3, facecolor='r', alpha=0.75)
                plt.show()
                
                
                
"---------------------------------------------------"                
                
                
def HistogramNoPlot(img):
    R,G,B=[0]*256,[0]*256,[0]*256
    pxls=img.load()
    if(img.mode=="RGB"):
        for x in range (img.size[0]):
            for y in range(img.size[1]):
                R[pxls[x,y][0]]+=1
                G[pxls[x,y][1]]+=1
                B[pxls[x,y][2]]+=1
        return(R,G,B)         
    if(img.mode!="RGB"):
        h=[0]*256     
        for x in range (img.size[0]):
            for y in range(img.size[1]): 
                h[pxls[x,y]]+=1
                
        return h    
    
"--------------------------------------------------"   
    
def normalize(arr):
        arr = arr.astype('float')
        for i in xrange(0,1):
            minval = arr[..., i].min()
            maxval = arr[..., i].max()
            if maxval != minval:
                arr[..., i] -= minval
                arr[..., i] *= (255.0 / (maxval - minval))
        return arr
    
                   
"------------------------------------------------------"
def Equalization(img):  
    pxls=img.load()
    N=(img.size)[0]*(img.size)[1]
    
    """--------------------------------"""
    def H(hist):
        histSize = len(hist)
        H = [0]*histSize
       
        for i in range(1,histSize):
            H[i]= hist[i]+H[i-1]
        return H
    '''''----------------------------------------'''
    if(img.mode=="RGB"):
        out_im =new("RGB", img.size, color = 1 )
        R,G,B=HistogramNoPlot(img)
        R,G,B=H(R),H(G),H(B)
        for x in range (img.size[0]):
            for y in range(img.size[1]):
                tup=((R[pxls[x,y][0]]*255)/N,
                     (G[pxls[x,y][1]]*255)/N,
                     (B[pxls[x,y][2]]*255)/N)
               
                out_im.putpixel((x,y),tup)
    if(img.mode!="RGB"):
        out_im =new("L", img.size, color = 1 )
        h=H(HistogramNoPlot(img))
        
        for x in range (img.size[0]):
            for y in range(img.size[1]):
                out_im.putpixel((x,y),h[pxls[x,y]]*255/N)
               
    #img.show()
    out_im.save('C:\Users\USER\workspace\Final Project\src\outputImage\OUTAVG.png')
    out_im.show() 
'''---------------------------------------------------------------------'''        
def Color_Quantization(img):
    '''Color quantization is the process 
    that drastically reduces the number of colors used in a digital color image 
    by approximating the original pixels with their nearest representative colors'''
    img=img.filter(ImageFilter.SMOOTH)
    result = img.convert('P', palette=ADAPTIVE, colors=4)
    result.save('C:\Users\USER\workspace\Final Project\src\outputImage\OUTEqualization.png')
    result.show()
'''---------------------------------------------------------------------'''        
def ImgMax(img):
    img=img.filter(ImageFilter.SMOOTH)
    img=img.filter(ImageFilter.MedianFilter(5))
    img.show() 
'''---------------------------------------------------------------------'''            
def Avg(img):
    R,G,B=0,0,0
    img=img.filter(ImageFilter.SMOOTH)
    pxls=img.load()
    
    N=img.size[0]*img.size[1]
    out_im =new("RGB", img.size, color = 1 )
    out_im2 =new("RGB", img.size, color = 1 )
    #img=cv2.bilateralFilter(np.array(pxls),9,75,75)


    print ("Calculate Avg..")
    for x in xrange (img.size[0]):
        for y in xrange(img.size[1]):
            R,G,B=R+pxls[x,y][0],G+pxls[x,y][1],B+pxls[x,y][2]
                
    R,G,B=R/N,G/N,B/N 
    for x in xrange (img.size[0]):
        for y in xrange(img.size[1]):
            tup=((pxls[x,y][0])/img.size[0],
                     (pxls[x,y][1])/img.size[0],
                     (pxls[x,y][2])/img.size[0])
            out_im.putpixel((x,y),tup)
            if((pxls[x,y][0]>R and  pxls[x,y][1]>G and pxls[x,y][2]>B)
                or (pxls[x,y][0]<R and  pxls[x,y][1]<G and pxls[x,y][2]<B)):
                out_im.putpixel((x,y),pxls[x,y])
                
    out_im.save('C:\Users\USER\workspace\Final Project\src\outputImage\OUTAVG.png')
    print ("Output Saved") 
    out_im.show()
                       

"------------------------------------------------"
