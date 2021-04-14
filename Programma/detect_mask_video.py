# USAGE
# python detect_mask_video.py

# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import winsound

#lees groene plaatje in
img_goed = cv2.imread('groen.png')
#lees rode plaatje in
img_fout = cv2.imread('rood.png')
#lees het grijze plaatje in
img_geen = cv2.imread('grijs.png')
masker = False
last_mask = False
l_img = img_geen
sound = None

face_detected = False


def detect_and_predict_mask(frame, faceNet, maskNet):

	# grab the dimensions of the frame and then construct a blob
	# from it
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
		(104.0, 177.0, 123.0))

	# pass the blob through the network and obtain the face detections
	faceNet.setInput(blob)
	detections = faceNet.forward()

	# initialize our list of faces, their corresponding locations,
	# and the list of predictions from our face mask network

	faces = []
	locs = []
	preds = []

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the detection
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the confidence is

		if confidence > args["confidence"]:
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
		#framw
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)
			face = np.expand_dims(face, axis=0)
			# add the face and bounding boxes to their respective
			# lists
			faces.append(face)
			locs.append((startX, startY, endX, endY))
	# only make a predictions if at least one face was detected
	if len(faces) > 0:
		# for faster inference we'll make batch predictions on *all*
		# faces at the same time rather than one-by-one predictions
		# in the above `for` loop
		preds = maskNet.predict(faces)
	return locs, preds


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", type=str,
	default="face_detector",
	help="path to face detector model directory")
ap.add_argument("-m", "--model", type=str,
	default="mask_detector.model",
	help="path to trained face mask detector model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# load our serialized face detector model from disk
print("[INFO] loading face detector model...")
prototxtPath = ".\deploy.prototxt"
weightsPath = "res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
print("[INFO] loading face mask detector model...")
maskNet = load_model(args["model"])

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = cv2.VideoCapture(1,cv2.CAP_DSHOW)
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	ret, frame = vs.read()
	if not ret:
		print("failed to grab frame")
		break

	frame = imutils.resize(frame, width=400)

	# detect faces in the frame and determine if they are wearing a
	# face mask or not
	(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

	# loop over the detected face locations and their corresponding
	# locations
	for (box, pred) in zip(locs, preds):
		# unpack the bounding box and predictions
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred

		# determine the class label and color we'll use to draw
		# the bounding box and text
		last_mask = masker
		if mask > withoutMask:
			color = (0, 255, 0)
			l_img = img_goed
			masker = True
			#hieronder een string met de locatie van het bestand dat afgespeeld moet worden als iemand een masker op heeft
			sound = 'C:/Users/joeyp/Desktop/IKPHBV_Project/IKPHBV_Draag_Je_Masker_Detectie_Tycho_van_Veen-Joey_Peschier/Programma/applause.wav'
		elif withoutMask > mask:
			l_img = img_fout
			color = (0, 0, 255)
			masker = False
			# hieronder een string met de locatie van het bestand dat afgespeeld moet worden als iemand geen masker op heeft
			sound = 'C:/Users/joeyp/Desktop/IKPHBV_Project/IKPHBV_Draag_Je_Masker_Detectie_Tycho_van_Veen-Joey_Peschier/Programma/beep.wav'
		#als de laatste keer dat er werd gecheckt de 'masker-status' anders is dan nu, speel geluid af.
		if last_mask != masker:
			winsound.PlaySound(sound,  winsound.SND_ASYNC)


		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

	# show the output frame
	s_img = frame
	x_offset = 50
	y_offset = 50
	l_img[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img
	cv2.imshow("Frame", l_img)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.release()