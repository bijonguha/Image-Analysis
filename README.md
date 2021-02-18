# Image-Analysis
Blur and Contrast Analysis of images

Task - Blur and Contrast check

optional arguments:
  -h, --help       show this help message and exit
  --image IMAGE    Path of the image file
  --folder FOLDER  True if path is a directory
  --method METHOD  RMS (rms) or Michelson (mich)
  --choice CHOICE  Blur (blur) or Contrast (con) Analysis
  
  
Example
>> python analysis.py --image blur_img --folder True --choice blur
 
>> python analysis.py --image testing --folder True --method mich

>> python analysis.py --image testing --folder True --method rms
