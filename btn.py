import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon, QFont

class Myshow(QWidget):
	"""docstring for Myshow"""
	def __init__(self):
		super(Myshow, self).__init__()
		
		self.initUI()

	def initUI(self):

		# QToolTip.setFont(QFont('SansSerif', 10))
		qbtn = QPushButton('Quit', self)
		qbtn.setToolTip('click to <b>exit</b>')
		qbtn.setGeometry(220, 260, 60, 20)
		qbtn.clicked.connect(QApplication.instance().quit)
		# qbtn.clicked.connect(self.closeEvent)

		self.setGeometry(300, 300, 300, 300)
		self.setWindowIcon(QIcon("1.png"))
		self.setWindowTitle("April")


		self.show()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Massage', 'Are you sure to exit?', 
			QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()

		else:
			event.ignore()

if __name__ == '__main__':
	app = QApplication(sys.argv)

	w = Myshow()
	print(1)

	sys.exit(app.exec_())

