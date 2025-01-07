# from PyQt5.QtWidgets import QApplication, QMainWindow
# import sys
import cv2
import requests
import json
import serial
import time

# app = QApplication([])
# win = QMainWindow()
# win.setWindowTitle("Sprout-Tech")
# win.resize(500,300)
# win.move(100,100)

cam = cv2.VideoCapture(0)
mega = serial.Serial('/dev/ttyUSB0',9600)
mega.reset_input_buffer()
initserial = False

while True:
    # communication with mega
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip() # receive status information from mega
        status = line.split('_')
        status[6] = status[6][0:4] # remove trailing '#' from euwf
        # send sensor information to server
        r1 = requests.post('https://alyssagollena.com/updatesensors.php', data={'temperature':float(status[1]), 'humidity':float(status[2]), 'soilmoisture1':float(status[3]), 'soilmoisture2':float(status[4]), 'waterlevel':int(status[5])})
        # send initial command status to server (only on initial)
        if initserial == False:
            r2 = requests.post('https://alyssagollena.com/updatecommands.php', data={'fanstate':status[6][0], 'uvstate':status[6][1], 'wateringstate':status[6][2], 'fertilizerstate':status[6][3]})
            initserial = True
    # communication with server
    r3 = requests.post('https://alyssagollena.com/getcommands.php')
    r3cmd = r3.json()
    # send new commands to mega
    megacmd = '@St_' + r3cmd['fanstate'] + r3cmd['uvstate'] + r3cmd['wateringstate'] + r3cmd['fertilizerstate'] + '\n'
    mega.write(megacmd.encode('ascii'))
    # images
	ret, image = cam.read()
	cv2.imshow('Imagetest',image)
	k = cv2.waitKey(1)
	if k != -1:
		break
	# delay
	time.sleep(1)
cv2.imwrite('/home/thirteenfour/Desktop/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()

# win.show()

# sys.exit(app.exec_())