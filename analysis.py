import cv2
import numpy as np
from skimage.exposure import is_low_contrast
import matplotlib.pyplot as plt

def check_contrast(path, method='rms'):
    '''
    Check contrast of given images using 
    RMS or Michelson method
    
    path : str
        path of given image
    method : str
        method 'rms' or 'mich'

    Returns 
        None 
    '''
    img = cv2.imread(path)
    plt.figure()

    if method == 'rms':
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        contrast = img_grey.std()

        print(contrast, end = ' ')
        if(contrast > 45):
            print('Normal')
            plt.title('Normal')
        else:
            print('Low')
            plt.title('Low')

    elif method == 'mich': #michelson
        Y = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)[:,:,0]

        # compute min and max of Y
        min = int(np.min(Y))
        max = int(np.max(Y))

        # compute contrast
        contrast = (max-min)/(max+min)

        print(contrast, end = ' ')
        if(contrast > 0.8):
            print('Normal')
            plt.title('Normal')
        else:
            print('Low')
            plt.title('Low')
        

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB) )
    plt.show()

def variance_of_laplacian(image):
    '''
    Compute the Laplacian of the image and return its variance
    '''
    return cv2.Laplacian(image, cv2.CV_64F).var()

def check_blur(path):

    img = cv2.imread(path)
    img_gray = cv2.imread(path,0)
    var = variance_of_laplacian(img_gray)

    plt.figure()

    if var<100:
        print('Blurry')
        plt.title('Blurry')
    else:
        print('Normal')
        plt.title('Normal')

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB) )
    plt.show()



if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='FcarScan Task - Blur and Contrast check')

  parser.add_argument('--image', default='view1.jpeg', type=str, help='Path of the image file')
  parser.add_argument('--folder', default='False', type=str, help='True if path is a directory')
  parser.add_argument('--method', default='rms', type=str, help='RMS (rms) or Michelson (mich)')
  parser.add_argument('--choice', default='blur', type=str, help='Blur (blur) or Contrast (con) Analysis')

  args = parser.parse_args()

  if args.choice == 'blur':
    print('Blur Analysis')

    if args.folder == 'True':
      import os
      files = os.listdir(args.image)
      files = [os.path.join(args.image, file) for file in files]
      for file in files:
        print('Image name :', file, end=' ')
        check_blur(file)

    else:
      print('Image name :', args.image, end=' ')
      check_blur(args.image)


  else:
    if args.folder == 'True':
      import os
      files = os.listdir(args.image)
      files = [os.path.join(args.image, file) for file in files]
      for file in files:
        print('Image name :', file, end=' ')
        check_contrast(file, args.method)

    else:
      print('Image name :', args.image, end=' ')
      check_contrast(args.image,args.method)
