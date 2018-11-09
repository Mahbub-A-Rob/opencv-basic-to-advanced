# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 05:15:29 2018

@author: Mahbub
"""
import cv2

def main():
    print('This is inside the main function')
    
    img_path = 'peppers_color.tif'
    img = cv2.imread(img_path) # Load image to img variable
    
    cv2.imshow('Peppers', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()