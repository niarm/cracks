import os, os.path
import cv2
import math
import matplotlib.pyplot as plt


#TAKES AN IMAGE AND RETURNS A LIST WITH CROPPED SLICES
def createImageSlices(img, tile_size=(512,512), offset=(512,512)):
    cropped_images = []
    img_shape = img.shape

    for i in range(int(math.floor(img_shape[0]/(offset[1] * 1.0)))):
        for j in range(int(math.floor(img_shape[1]/(offset[0] * 1.0)))):
            cropped_img = img[offset[1]*i:min(offset[1]*i+tile_size[1], img_shape[0]), offset[0]*j:min(offset[0]*j+tile_size[0], img_shape[1])]
            cropped_images.append(cropped_img)
    
    return cropped_images


def plotImageTiles(croppedImageList, columns = 7, rows = 10, imageSize=(10,10)):
    fig=plt.figure(figsize=imageSize)
    
    for i in range(1, columns*rows +1):
        img = croppedImageList[i-1]
        plt.subplots_adjust(wspace=0.05, hspace=0.005)
        fig.add_subplot(columns, rows, i)
        plt.axis('off')
        plt.imshow(img)
    plt.show()



##TAKES A DIRECTORY-PATH AND RETURNS A LIST OF IMAGES FOUND.
##(NO RECURSIVE DIR-STRUCTURES SUPPORTED)
def getImageListFromDir(targetDir, validFormats=['.jpg']):
    images = []
    for f in os.listdir(targetDir):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in validFormats:
            print("skip:",f)
        else:
            images.append(cv2.imread(os.path.join(targetDir,f)))
    return images

