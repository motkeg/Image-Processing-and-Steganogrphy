from Tkinter import *
import tkFileDialog as fd
#from ttk import *
from Decoder_Encoder  import *
from image_func import *
from PIL.Image import *



root2 = Tk()
root2.title("Select image to detact")
root2.withdraw()
file_path = fd.askopenfilename()
img=open(file_path)
def loadhidegui():
    hidegui=HideGUI()
def loaddetectgui():    
    detectgui=DetectGUI()
    
def f1():
    temp=img
    Histogram(temp)
def f2():
    temp=img
    Avg(temp)
def f3():
    temp=img
    Equalization(temp)
def f4():
    temp=img
    Color_Quantization(temp)
def f5():
    temp=img
    ImgMax(temp)
def f6():
    temp=img
    MassegeDecode1(temp)
def f7():
    temp=img
    MassegeDecode2(temp)
def f8():
    temp=img
    Extractimage(temp)
def f9():
    img.show() 

def fstr():
    num=raw_input("Enter string:")
    MassegeHide1(img,num)                                
def fimage():
    root2 = Tk()
    root2.title("Select image to detact")
    root2.withdraw()
    file_path = fd.askopenfilename()
    img2=open(file_path)
    Hideimage(img, img2)

def getPath():
            root = Tk()
            root.withdraw()
            file_path = fd.askopenfilename()
            img=open(file_path)
            img.show()

class MainGUI():
    def __init__(self):
        
        root = Tk()
        root.title("Main Menu")
        root.geometry("400x100")
      
        self.lbl= Label(root,text="Hello and Wellcom!" ,fg="red").pack()
        self.btn1=Button(root,text="Detect data Steganography",bg="red",fg="white",command=loaddetectgui).pack(side=LEFT)
        self.btn2=Button(root,text="Hide data Steganography",bg="black",fg="white",command=loadhidegui).pack(side=RIGHT)
        
        root.mainloop()
        

            
class HideGUI():
    def __init__(self):
        
        root = Tk()
        root.title("Hide Menu")
        root.geometry("250x130")
        self.btn1=Button(root,text="Hide number",bg="blue",fg="white",padx = 20,command=fstr).pack()
        self.btn2=Button(root,text="Hide string",bg="blue",fg="white",padx = 20,command=fstr).pack()
        self.btn3=Button(root,text="Hide image",bg="blue",fg="white",padx = 20,command=fimage).pack()
        
        root.mainloop()
        




class DetectGUI():      
    def __init__(self):  
        root = Tk()
        root.title("Detect Menu")
        root.geometry("250x250")
    
        self.rd1=Radiobutton(root, text="Histogram",padx = 20, value=1 ,command=f1).pack(anchor=W)
        self.rd2=Radiobutton(root, text="AVG",padx = 20,value=2,command=f2).pack(anchor=W)
        self.rd3=Radiobutton(root, text="Equalization",padx = 20,value=3,command=f3).pack(anchor=W)
        self.rd4=Radiobutton(root, text="Color_Quantization",padx = 20, value=4,command=f4).pack(anchor=W)
        self.rd5=Radiobutton(root, text="ImgMax",padx = 20,value=5,command=f5).pack(anchor=W)
        self.rd6=Radiobutton(root, text="MassegeDecode1",padx = 20,value=6,command=f6).pack(anchor=W)
        self.rd7=Radiobutton(root, text="MassegeDecode2",padx = 20, value=7,command=f7).pack(anchor=W)
        self.rd8=Radiobutton(root, text="Extractimage",padx = 20,value=8,command=f8).pack(anchor=W)
        self.btn=Button(root,text="see the orginal",bg="blue",fg="white",padx = 20,command=f9).pack()
        root.mainloop()
 



#img.show()                    

        

       