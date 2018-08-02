import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Ready')
		'''
		等价于
		self.statusBar().showMessage('Ready')
		'''
		
		menubar = self.menuBar()
		filemenu = menubar.addMenu('&File')

		exitAct = QAction(QIcon('1.png'), '&Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit Application')
		exitAct.triggered.connect(qApp.quit) # 另一种退出程序方式

		submenu = QMenu('Import', self)
		# submenu.setStatusTip('Import something') # QAction对象才能显示StatusTip
		submenu_act = QAction('import mail', self)
		submenu_act.setStatusTip('Import a mail')
		submenu_act1 = QAction('nothing',self)
		submenu.addAction(submenu_act1)
		submenu.addAction(submenu_act)

		viewAct = QAction('view statusbar', self, checkable = True)
		viewAct.setStatusTip('view statusbar')
		viewAct.setChecked(True) # initial status
		viewAct.triggered.connect(self.toggleMenu)


		filemenu.addAction(exitAct)
		filemenu.addMenu(submenu)
		filemenu.addAction(viewAct)

		self.toolbar = self.addToolBar('exit')
		self.toolbar.addAction(exitAct)

		self.setGeometry(300, 300, 600, 300)
		self.setWindowTitle('MenuBar&StatusBar')
		self.setWindowIcon(QIcon('1.png'))
		self.show()

	def toggleMenu(self, state):
		if state:
			self.statusbar.show()
		else:
			self.statusbar.hide()

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