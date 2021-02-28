import numpy as np
import cv2

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with  open("coco.names", 'r') as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
outputLayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

colors = np.random.uniform(0, 255, size = (len(classes), 3))
cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#outer = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))))
while(True):
    ret, frame = cap.read()
    height, width, channel = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (256,256), (0, 0, 0), True, crop = False)
    net.setInput(blob)
    outs = net.forward(outputLayers)
    classIdArr = []
    confArr = []
    startTupleArr = []
    endTupleArr = []
    boxArr = []

    for out in outs:
        for detection in out:
         scores = detection[5:]
         classId = np.argmax(scores)
         confidence = scores[classId]
         #print(confidence)
         if confidence >= 0.3 :
            classIdArr.append(classId)
            confArr.append(float (confidence))

            centreX = int(detection[0] * width)
            centreY = int(detection[1]* height)

            w = int(detection[2]*width)
            h = int(detection[3]*height)
            # rectangle cordinates
            x = int(centreX - w/2)
            y = int(centreY - h/2)

            startTupleArr.append((x, y))
            endTupleArr.append((x+w, y+ h))
            boxArr.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxArr, confArr, 0.3, 0.3)
    for i in range (len(classIdArr)):
        if i in indices:
            cv2.rectangle(frame, startTupleArr[i], endTupleArr[i], colors[i], 1)
            cv2.putText(frame, classes[classIdArr[i]], startTupleArr[i], cv2.FONT_HERSHEY_PLAIN, 0.5, colors[i], 1)



    #outer.write(frame.astype('uint8'))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()