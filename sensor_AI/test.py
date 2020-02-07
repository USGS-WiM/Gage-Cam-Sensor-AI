import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import time
import gage_cam_preprocess as prep
#from keras.models import load_model

def conv(model):
	# Convert the model.
	converter = tf.lite.TFLiteConverter.from_keras_model(model)
	tflite_model = converter.convert()
	return tflite_model

def down_block(x, filters, kernal_size = (3, 3), padding ='same', strides=1):
	c= keras.layers.Conv2D(filters, kernal_size, padding=padding, strides=strides, activation='relu')(x)
	c= keras.layers.Conv2D(filters, kernal_size, padding=padding, strides=strides, activation='relu')(c)
	p = keras.layers.MaxPool2D((2, 2), (2, 2))(c)
	return c, p

def up_block(x, skip, filters, kernal_size =(3, 3), padding='same', strides= 1):
	us = keras.layers.UpSampling2D((2, 2))(x)
	concat = keras.layers.Concatenate()([us, skip])
	c= keras.layers.Conv2D(filters, kernal_size, padding=padding, strides=strides, activation='relu')(concat)
	c= keras.layers.Conv2D(filters, kernal_size, padding=padding, strides=strides, activation='relu')(c)
	return c

def bottleneck(x, filters, kernal_size = (3, 3), padding ='same', strides=1):
	c= keras.layers.Conv2D(filters, kernal_size, padding=padding, strides=strides, activation='relu')(x)
	c= keras.layers.Conv2D(filters, kernal_size, padding=padding, strides=strides, activation='relu')(c)
	return c

def UNet():
	image_size = 256
	f= [16, 32, 64, 128, 256]
	inputs = keras.layers.Input((image_size, image_size, 3))
	p0 = inputs
	c1, p1 = down_block(p0, f[0])
	c2, p2 = down_block(p1, f[1])
	c3, p3 = down_block(p2, f[2])
	c4, p4 = down_block(p3, f[3])
	
	bn = bottleneck(p4, f[4])
	
	u1 = up_block(bn, c4, f[3])
	u2 = up_block(u1, c3, f[2])
	u3 = up_block(u2, c2, f[1])
	u4 = up_block(u3, c1, f[0])
	
	outputs = keras.layers.Conv2D(3, (1, 1), padding='same', activation = 'sigmoid')(u4)
	
	model = keras.models.Model(inputs, outputs)
	
	return model


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
	strt = time.time()
	#model = UNet()
	#model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["acc"])
	#model.summary()
	image = prep.load_on_dek("on_dek/1.jpg")
	print(image.shape)
	img = np.expand_dims(image, axis=0)
	# load model from file
	model = keras.models.load_model("model/UnetM-relu_output.h5") 
	# summarize modelfrom file 
	model.summary()
	#model.load_weights('weights/UnetW-relu_output.h5')
	#model.summary()
	pxH, pxW = run_on_dek(model, img)
	print('Height:', pxH, 'px', 'H(p):', (3.36 - (pxH/pxW) * .333), 'width:', pxW, 'px')  



def run_on_dek(model, img):
	print ('here')
	tflite_model = conv(model)
	# Load TFLite model and allocate tensors. 
	#interpreter = tf.lite.Interpreter(model_content=tflite_model) 
	#interpreter.allocate_tensors()
	# Get input and output tensors. 
	#input_details = interpreter.get_input_details() 
	output_details = interpreter.get_output_details()

	#input_shape = img.shape
	#input_data = img
	#interpreter.set_tensor(img.index, input_data)

	#interpreter.invoke()
	result = tflite_model.run(img)
	#result = model.predict(img)
	print("here")
	result = result >=.995
	print (result)
	px, w = get_exposed(result)
	return px, w

execute()
