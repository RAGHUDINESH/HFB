from imageai.Detection import ObjectDetection
import os
import cv2
import numpy as np

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
while(True):
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
	box=detections[0]['box_points']
	pos_human_L=(box[0]+box[2])*0.4
	pos_human=(box[0]+box[2])*0.5
	pos_human_R=(box[0]+box[2])*0.6
	frame_centre=480
	if pos_human_L>frame_centre:
		clock()
	elif pos_human_R<=frame_centre:
		anti_clock()
	else:
		x=distance()
		if x>150:
			forward()
		else:
			stop()
	image=cv2.imread("imagenew.jpg")
	image[int(point[1]+2),int(point[0])+2]=red
	cv2.imwrite("result.png",image)