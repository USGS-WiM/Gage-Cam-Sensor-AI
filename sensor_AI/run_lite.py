from tensorflow import keras
import numpy as np
import pidash
#import gc



# This is a prototype implementation of the sensor AI deployment. 
#This is not final code and should not be reguarded as a best practices.



# get_exposed() is a simple pixel count routine. It established the pixel count on the x and the y axis using simple n^2 logic loops

def get_exposed(y_hat):
	img = y_hat.ravel()
	img = img[2::3]
	img = np.resize(img, (256, 256))
	h = []
	for i, obj in enumerate(img):
		for j in obj:
			if j:
				h.append(i)
				break
	w=[]
	for i, obj in enumerate(img.T):
		for j in obj:				
			if j:
				w.append(i)
				break
	h = len(h)
	w = len(w)
	
	return h, w


def execute(): #on_dek, meta, id):
	#gc.collect()
	#Load keras pretrained model from .h5 file
	model = keras.models.load_model("model/UnetM-relu_output.h5") 
	# summarize model 
	model.summary()
	pidash.dashboard()
	#get px height and px width from image
	pxH, pxW = run_on_dek(model)
	outputtxt = 'Height: '+ str(pxH) + ' px '+ ' H(p): ' + str((3.36 - (pxH/pxW) * .333)) + ' width: '+ str(pxW) + ' px'
	text_file = open("complete.txt", "w") 
	n = text_file.write(outputtxt) 
	text_file.close()
	print (outputtxt)


def run_on_dek(model):
	# Load img
	img = np.load("on_dek/rdy.npy")
	print("Image loaded..." + '\n\n' + "Running model...")
	pidash.dashboard()
	result = model.predict(img)
	print("\n\nModel ran successfully...")
	result = result >=.995
	#print (result)
	px, w = get_exposed(result)
	return px, w

execute()
