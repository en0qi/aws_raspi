import boto3
import cv2
import datetime

client = boto3.client('rekognition')
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
ret, data = cv2.imencode('.png', frame)

#save capture image
dt_now = datetime.datetime.now()
dt_str= dt_now.strftime('%y%m%d_%H%M%S')
cv2.imwrite('/cap/reko_{}.png'.format(dt_str),frame)

#change data format
byte_data = bytearray(data)

#call Amazon rekognition
response = client.detect_labels(
	Image={
		'Bytes': byte_data
	},
	MaxLabels=50
)

#console log
for i, value in enumerate(response['Labels']): 
	print("{1:05.2f} % - {0}".format(response['Labels'][i]['Name'],response['Labels'][i]['Confidence']))

