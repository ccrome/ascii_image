# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ascii_image.ui'
#
# Created: Tue Jun 30 09:06:01 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(940, 697)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.graphicsView = AsciiGraphicsView(self.splitter)
        self.graphicsView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setObjectName(_fromUtf8("action_New"))
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName(_fromUtf8("actionE_xit"))
        self.actionLine = QtGui.QAction(MainWindow)
        self.actionLine.setCheckable(True)
        self.actionLine.setObjectName(_fromUtf8("actionLine"))
        self.actionCircle = QtGui.QAction(MainWindow)
        self.actionCircle.setCheckable(True)
        self.actionCircle.setObjectName(_fromUtf8("actionCircle"))
        self.actionBox = QtGui.QAction(MainWindow)
        self.actionBox.setCheckable(True)
        self.actionBox.setObjectName(_fromUtf8("actionBox"))
        self.actionArrow = QtGui.QAction(MainWindow)
        self.actionArrow.setCheckable(True)
        self.actionArrow.setChecked(True)
        self.actionArrow.setObjectName(_fromUtf8("actionArrow"))
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.actionText = QtGui.QAction(MainWindow)
        self.actionText.setCheckable(True)
        self.actionText.setObjectName(_fromUtf8("actionText"))
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionE_xit)
        self.menuEdit.addAction(self.actionLine)
        self.menuEdit.addAction(self.actionCircle)
        self.menuEdit.addAction(self.actionBox)
        self.menuEdit.addAction(self.actionText)
        self.menuEdit.addAction(self.actionDelete)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBar.addAction(self.actionArrow)
        self.toolBar.addAction(self.actionLine)
        self.toolBar.addAction(self.actionCircle)
        self.toolBar.addAction(self.actionBox)
        self.toolBar.addAction(self.actionText)
        self.toolBar.addAction(self.actionDelete)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_New.setText(_translate("MainWindow", "&New", None))
        self.action_New.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit", None))
        self.actionE_xit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionLine.setText(_translate("MainWindow", "Line", None))
        self.actionLine.setToolTip(_translate("MainWindow", "Create a line", None))
        self.actionLine.setShortcut(_translate("MainWindow", "L", None))
        self.actionCircle.setText(_translate("MainWindow", "Circle", None))
        self.actionCircle.setShortcut(_translate("MainWindow", "C", None))
        self.actionBox.setText(_translate("MainWindow", "Box", None))
        self.actionBox.setShortcut(_translate("MainWindow", "B", None))
        self.actionArrow.setText(_translate("MainWindow", "Arrow", None))
        self.actionArrow.setToolTip(_translate("MainWindow", "Move items around", None))
        self.actionArrow.setShortcut(_translate("MainWindow", "Esc", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del", None))
        self.action_Save.setText(_translate("MainWindow", "&Save", None))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionText.setText(_translate("MainWindow", "Text", None))
        self.actionText.setShortcut(_translate("MainWindow", "T", None))

from ascii_graphics_view import AsciiGraphicsView

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

