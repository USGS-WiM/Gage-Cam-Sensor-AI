import numpy as np 
import cv2


def load_on_dek(path):
	img = cv2.imread(path, 1)
	rdy_img = prep(img, 256, False)
	return rdy_img

def prep(image, image_size, darken):
	#image = image     
	#image_size = image_size     
	#cropped_img = get_crop(image)     
	resized_img = cv2.resize(image, (image_size, image_size))     
	if darken == False:         
		return resized_img/255.0     
	else:         
		return  (resized_img/255.0) - darken
