from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import cv2

app = QApplication([])
win = QMainWindow()
win.setWindowTitle("Sprout-Tech")
win.resize(500,300)
win.move(100,100)

cam = cv2.VideoCapture(0)

while True:
	ret, image = cam.read()
	cv2.imshow('Imagetest',image)
	k = cv2.waitKey(1)
	if k != -1:
		break
cv2.imwrite('/home/thirteenfour/Desktop/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()

win.show()

sys.exit(app.exec_())