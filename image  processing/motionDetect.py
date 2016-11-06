import numpy as np
import cv2
import math ,time




'''-----------------------------------------------'''


def normalize(arr):
	
        ''' The normalization proccess is to clear 'noise' that captured  by the camera
            in duration of the algorithm.  '''
		   
        arr = arr.astype('float')
        for i in xrange(0,1):
            minval = arr[..., i].min()
            maxval = arr[..., i].max()
            if maxval != minval:
                arr[..., i] -= minval
                arr[..., i] *= (255.0 / (maxval - minval))
        return arr
'''------------------------------------------------'''  
def FrameSmoth(frame):

    ''' In this stage of algorithm we impliment the 'bluring' procces -
        the function clculate the score of each frame of the interval (0.25 s) by execute the gaussian.
        The goal of this proccess is to avoid 'False Positive'	of ths frames hat we recognized as diffrent. ''' 

    gaussian =cv2.getGaussianKernel(5,10)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.filter2D(gray,-1,gaussian)
    #gray=signal.convolve2d(gray, gaussian,mode='same')
    gray=normalize(gray)
    return gray

'''---------------------------------------------------'''       

def AVGframe( frms):
        ''' Here we clculate the avg frame of the inteval due to the formula:
       	   avg = (sum(N)*W(i)*I(i))/N
           where: N = size of frames
             	  W = weight of each frame (we can give same weight for all frames)
                  I = frame.			
           finally we subtract the final frame from the avarege.				  '''

        N=len(frms)
        w=1/1.2
        lastFrame=frms[N-1]
        for i in range(N):
            frms[i]=frms[i]*(float(w)/N)
        res = sum(frms)-lastFrame
        return res 
                 

def Main():
    cap = cv2.VideoCapture(0)  
    while(cap.isOpened()):
        frams=[]
        ret = cap.set(3,320)
        ret = cap.set(4,240)
        t1=time.time()
                                  
        while(1): #take frames in 0.25 sec in loop
            ret, frame = cap.read()
            
            if ret==True:
                gray=FrameSmoth(frame)
                frams.append(gray)
                if (time.time()-t1>0.25):
                    break
            else:
                break     
            
        avg = AVGframe(frams)
        cv2.imshow('frames after Averaging',avg)
       
        if cv2.waitKey(1) & 0xFF == ord(' '): # exit if the user choose to stop
            break
# Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()        
            
          



    
def Q2():
    cap = cv2.VideoCapture(0)
   
    while(cap.isOpened() ):
        ret = cap.set(3,320)
        ret = cap.set(4,240)
        ret, frame = cap.read()
            
        if ret==True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            x,thresh = cv2.threshold(gray,137,255,1)
            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame, contours,-1, (0,255,0), 3)
            cv2.imshow('Image with contours',frame)    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ =="__main__":
    Main()       

