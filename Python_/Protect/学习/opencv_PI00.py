import cv2
import numpy as np
import matplotlib.pyplot as plt
#Creat color line image
def color_hist(img):
    #Creat YanMo
    mask = np.zeros(img.shape[:2],np.uint8)
    mask[70:170,100:220] = 255

    hsv = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    hist_mask = cv2.calcHist([hsv],[0],mask,[180],[0,180])
    object_H = np.where(hist_mask==np.max(hist_mask))

    print (object_H[0])
    return object_H[0]
    plt.plot(hist_mask)
    plt.xlim(0, 100)
    plt.imshow(hist_mask, interpllatioin='nearest')




def color_distinguish(object_H):
    try:
        if object_H>26 and object_H<34: color = 'yellow'
        elif object_H>156 and object_H<180: color = 'red'
        elif object_H>100 and object_H<124: color='blue'
        elif object_H>35 and object_H<77 : color='green'
        elif object_H>78 and object_H<99 : color='cyan-blue'
        elif object_H>6 and object_H<15 : color='orange'
        else : color = 'None'
        print (color)
        return color
    except : pass

if __name__ == '__main__':
    img = np.ones((240,320,3),dtype=np.uint8) * 128
    img [60:180,80:240] = [255,0,255]
    object_H = color_hist(img)
    color_distinguish(object_H)
    cv2.imshow('image',img)
    cv2.waitKey(0)





