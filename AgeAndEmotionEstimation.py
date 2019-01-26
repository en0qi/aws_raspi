import boto3
import cv2
import datetime
import pprint
import json

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
response = client.index_faces(
    CollectionId='sample',
    Image={
        'Bytes': byte_data,
    },
    DetectionAttributes=['ALL']
)

resd = json.loads(response)

# #console log
# for i, value in enumerate(response['FaceRecords']): 
# 	print("{1:05.2f} % - {0}".format(response['FaceRecords']['FaceDetail'][i]['Name'],response['Labels'][i]['Confidence']))

print("この人の性別は *{0}* で、".format(resd['FaceRecords']['FaceDetail']['Gender']['Value']))

	# ,response['FaceRecords']['FaceDetail']['AgeRange']['Low'],response['FaceRecords']['FaceDetail']['AgeRange']['High'],response['FaceRecords']['FaceDetail']['Emotions'][0]['Type']))年齢は *{1}~{2}歳* だね。{3}そうだね。#

