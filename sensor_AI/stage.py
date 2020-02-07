import numpy as np
import cv2
import gage_cam_preprocess as prep


def execute(): #on_dek, meta, id):
	image = prep.load_on_dek("on_dek/1.jpg")
	img = np.expand_dims(image, axis=0)
	np.save("on_dek/rdy.npy", img)


execute()
