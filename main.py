import ascii_image
from PyQt4 import QtCore, QtGui
import sys

class UiMainWindow(ascii_image.Ui_MainWindow):
    def __init__(self, MainWindow):
        super(UiMainWindow, self).__init__()
        self.setupUi(MainWindow)
        self.graphicsView.addAction(self.actionLine)
        self.graphicsView.addAction(self.actionCircle)
        self.graphicsView.addAction(self.actionBox)
        self.actionE_xit .triggered.connect(QtGui.qApp.quit)

        self.objectActionGroup = QtGui.QActionGroup(MainWindow)
        self.objectActionGroup.addAction(self.actionArrow)
        self.objectActionGroup.addAction(self.actionText)
        self.objectActionGroup.addAction(self.actionLine)
        self.objectActionGroup.addAction(self.actionBox)
        self.objectActionGroup.addAction(self.actionCircle)


        self.graphicsView.selectedToolChanged(self.actionArrow)
        self.graphicsView.scale(3, 3)
        self.objectActionGroup.triggered.connect(self.graphicsView.selectedToolChanged)
        self.actionDelete.triggered.connect(self.graphicsView.actionDelete)

        self.action_Save.triggered.connect(self.graphicsView.save)
        self.action_Open.triggered.connect(self.graphicsView.load)
        
        self.buttonToAscii.clicked.connect(self.graphicsToAscii)
        self.buttonToGraphics.clicked.connect(self.asciiToGraphics)
        

    def graphicsToAscii(self):
        text = self.graphicsView.graphicsToAscii()
        self.asciiTextEdit.setText(text)
        
    def asciiToGraphics(self):
        """convert whatever is in the asciiTextEdit field into the graphics view.  i.e. equivalent of load file"""
        text = str(self.asciiTextEdit.toPlainText())
        self.graphicsView.asciiToGraphics(text)

        
    def getSelectedTool(self):
        return self.objectActionGroup
        
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = UiMainWindow(MainWindow)
#ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
