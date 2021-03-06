import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.setGeometry(300, 300, 600, 300)
		self.setWindowTitle('MenuBar&StatusBar')
		self.setWindowIcon(QIcon('1.png'))
		self.show()


	def contextMenuEvent(self, event):
		cmenu = QMenu(self)
		
		newAct = cmenu.addAction('New')
		openAct = cmenu.addAction('Open')
		quitAct = cmenu.addAction('Quit')
		action = cmenu.exec_(self.mapToGlobal(event.pos()))

		if action == quitAct:
			qApp.quit()

if __name__ == '__main__':
	app = QApplication(sys.argv)

	w = Example()

	sys.exit(app.exec_())