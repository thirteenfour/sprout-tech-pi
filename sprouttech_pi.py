from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication([])
win = QMainWindow()
win.setWindowTitle("Sprout-Tech")
win.resize(500,300)
win.move(100,100)

win.show()

sys.exit(app.exec_())