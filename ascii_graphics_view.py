from PyQt4 import QtGui, QtCore
import StringIO
import json
import zlib
import binascii
import traceback
import textedit
import font2
import pickle
import sys
class AsciiGraphicsView(QtGui.QGraphicsView):
    def __init__(self, parent):
        super(AsciiGraphicsView, self).__init__(parent)
        scene = QtGui.QGraphicsScene()
        self.setScene(scene)
        
        redbrush   = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        dotbrush   = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        dotpen     = QtGui.QPen(QtGui.QColor(0, 0, 0, 0))
        greenbrush = QtGui.QBrush(QtCore.Qt.green)
        self.blackpen   = QtGui.QPen(QtCore.Qt.black)
        self.blackpen.setWidth(4)
        self.setMouseTracking(True)
        
        bigx = 300
        bigy = 100
        stepx = 5
        stepy = 7
        self.stepx = stepx
        self.stepy = stepy
        
        for x in range(bigx):
            for y in range(bigy):
                x1, y1 = x*stepx, y*stepy
                scene.addRect(x1, y1, 2, 2, brush=dotbrush, pen=dotpen)

        self.drawingState = None
        self.drawingCoordinates = list()
        self.drawingCurrentObject = None
        self.scene = scene
        self.currentObjects = list()
        self.font = QtGui.QFont("courier", 6)
        self.lineStart = "// "
        self.lineEnd = "\n"
        self.commentStart = ""
        self.commentEnd = ""

    def selectedToolChanged(self, action):
        self.drawingState = action.text() # Stop doing whatever we were doing ... the tool changed.
        self.drawingCoordinates = list()
        if (self.drawingCurrentObject):
            self.scene.removeItem(self.drawingCurrentObject)
            self.drawingCurrentObject = None

    def snapCoordinates(self, pos):
        return pos.x(), pos.y()
        x = float(pos.x())
        y = float(pos.y())
        x = int(round(x / self.stepx))*self.stepx
        y = int(round(y / self.stepy))*self.stepy
        return [x, y]
    
    def actionDelete(self):
        # Find any currently selected objects in the scene and delete them
        for item in self.scene.selectedItems():
            self.currentObjects.remove(item)
            self.scene.removeItem(item)
            
    def loadSaveableStruct(self, js):
        """convert what was returned by 'getSaveableStruct' back to a list of graphicsItems"""
        currentObjects = list()
        for item in js:
            t = item[0]
            coords = item[1:]
            text = None
            if (t == 'ellipse'):
                posx, posy, width, height = coords
                obj = QtGui.QGraphicsEllipseItem(0, 0, width, height)
            elif (t == 'rect'):
                posx, posy, width, height = coords
                obj = QtGui.QGraphicsRectItem(0, 0, width, height)
            elif (t == 'line'):
                posx, posy, width, height = coords
                obj = QtGui.QGraphicsLineItem(0, 0, width, height)
            elif (t == 'text'):
                text, posx, posy = coords
                obj = QtGui.QGraphicsTextItem(text)
                obj.setFont(self.font)
            else:
                raise Exception("Unrecognized graphics item")
            if text == None:
                obj.setPen(self.blackpen)
            obj.setPos(posx, posy)
            obj.setFlag(obj.ItemIsSelectable)
            obj.setFlag(obj.ItemIsMovable)
            
            currentObjects.append(obj)
            
        return currentObjects
        
    def getSaveableStruct(self):
        """return the currentObjects in a form that's easy to save.  i.e. with no class, just a dict"""
        object_list = list()
        for obj in self.currentObjects:
            d = None
            if isinstance(obj, QtGui.QGraphicsEllipseItem):
                d = ["ellipse",
                     int(obj.pos().x()), int(obj.pos().y()),
                     int(obj.rect().width()), int(obj.rect().height())]
            if isinstance(obj, QtGui.QGraphicsRectItem):
                d = ["rect",
                     int(obj.pos().x()), int(obj.pos().y()),
                     int(obj.rect().width()), int(obj.rect().height())]
            if isinstance(obj, QtGui.QGraphicsLineItem):
                d = ["line",
                     int(obj.pos().x()), int(obj.pos().y()),
                     int(obj.line().x2()),
                     int(obj.line().y2())]
            if isinstance(obj, QtGui.QGraphicsTextItem):
                d = ["text",
                     str(obj.toPlainText()),
                     int(obj.pos().x()), int(obj.pos().y())]
            if d:
                object_list.append(d)
        return object_list
    
    def _extract_json(self, lines):
        # extract the AGV= ... json from f
        for line in lines:
            magic = "%sAGV=" % self.lineStart
            try:
                # Check to see if the line parses by itself.
                return json.loads(line)
            except ValueError:
                pass
                
            if line.startswith(magic):
                # This is it.  just extract the rest of the line and be done.
                txt = line[len(magic):]
                return json.loads(txt)

        
    def asciiToGraphics(self, text):
        """convert whatever is in the asciiTextEdit field into the graphics view.  i.e. equivalent of load file"""
        lines = text.split("\n")
        d = self._extract_json(lines)
        self._to_graphics(d)
    
    def load(self):
        filename = QtGui.QFileDialog.getOpenFileName(filter = "*.agv")
        if filename:
            f = open(filename, "r")
            d = self._extract_json(f.readlines())
            self._to_graphics(d)

    def _to_graphics(self, d):
        try:
            currentObjects = self.loadSaveableStruct(d)
        except Exception as e:
            mb = QtGui.QMessageBox()
            traceback.print_exc()
            mb.setText("Couldn't read %s.  Error returned is %s" % (filename, e))
            mb.exec_()
            return

        self.new()
        for obj in currentObjects:
            self.currentObjects.append(obj)
            self.scene.addItem(obj)
        
    def new(self):
        """remove all items from the current scene"""
        for obj in self.currentObjects:
            self.scene.removeItem(obj)
        self.currentObjects = list()


    def convertToAsciiImage(self):
        objs = self.getSaveableStruct()
        asc = font2.create_image(objs)
        return asc
        
    def graphicsToAscii(self):
        """Convert what is in the graphics view into a text string and return it"""
        ascii_text = self._to_ascii()
        return ascii_text

    def _to_ascii(self):
        objs = self.getSaveableStruct()
        js = json.dumps(objs) # , indent=4, separators=(',', ': '))
        zjs = binascii.b2a_hex(zlib.compress(js, 9))
        ascii_image = self.convertToAsciiImage()
        f = StringIO.StringIO()
        f.write(self.commentStart)
        for line in ascii_image:
            f.write(self.lineStart)
            f.write(line)
            f.write(self.lineEnd)
        f.write(self.lineStart)
        f.write("AGV=")
        f.write(js)
        f.write(self.lineEnd)
        txt = f.getvalue()
        f.close()
        return txt
    
    def save(self):
        # save the current items.
        filename = QtGui.QFileDialog.getSaveFileName(filter = "*.agv")
        if filename:
            ascii_text = self._to_ascii()
            f = open(filename, "w")
            f.write(ascii_text)
            f.close()
            
            
    def mousePressEvent(self, mouseEvent):
        pos = self.mapToScene(mouseEvent.pos())
        x, y = pos.x(), pos.y()
        self.drawingCoordinates.append(self.snapCoordinates(pos))
        object_created = False
        if ( (self.drawingState == 'Line' or
              self.drawingState == 'Circle' or
              self.drawingState == 'Box')
             and len(self.drawingCoordinates) == 2):
            self.currentObjects.append(self.drawingCurrentObject)
            object_created = True
            
        if (self.drawingState == 'Text'):
            Dialog = QtGui.QDialog()
            mb = textedit.Ui_Dialog()
            mb.setupUi(Dialog)
            Dialog.exec_()
            self.drawingCurrentObject = self.scene.addText(mb.textEdit.toPlainText(), self.font)
            self.drawingCurrentObject.setPos(x, y)
            self.currentObjects.append(self.drawingCurrentObject)
            object_created=True
            
        if (object_created):
            self.drawingCurrentObject.setFlag(self.drawingCurrentObject.ItemIsSelectable)
            self.drawingCurrentObject.setFlag(self.drawingCurrentObject.ItemIsMovable)
            self.drawingCurrentObject = None
            self.drawingCoordinates = list()
            return
        
        super(AsciiGraphicsView, self).mousePressEvent(mouseEvent)
        
    def mouseMoveEvent(self, mouseEvent):
        pos = self.mapToScene(mouseEvent.pos())
        if len(self.drawingCoordinates):
            x1, y1 = self.drawingCoordinates[0][0], self.drawingCoordinates[0][1]
        x2, y2 = self.snapCoordinates(pos)
        if (self.drawingState == 'Line' and len(self.drawingCoordinates) == 1):
            if self.drawingCurrentObject:
                self.scene.removeItem(self.drawingCurrentObject)
            self.drawingCurrentObject = self.scene.addLine(0, 
                                                           0,
                                                           x2 - x1, y2- y1,
                                                           pen = self.blackpen)
            self.drawingCurrentObject.setPos(x1, y1)
            
        if (self.drawingState == 'Circle' and len(self.drawingCoordinates) == 1):
            if self.drawingCurrentObject:
                self.scene.removeItem(self.drawingCurrentObject)
            self.drawingCurrentObject = self.scene.addEllipse(0, 0, x2-x1, y2-y1, pen = self.blackpen)
            self.drawingCurrentObject.setPos(x1, y1)
            
        if (self.drawingState == 'Box' and len(self.drawingCoordinates) == 1):
            if self.drawingCurrentObject:
                self.scene.removeItem(self.drawingCurrentObject)
            self.drawingCurrentObject = self.scene.addRect(0, 0, x2-x1, y2-y1, pen = self.blackpen)
            self.drawingCurrentObject.setPos(x1, y1)
            
        super(AsciiGraphicsView, self).mouseMoveEvent(mouseEvent)
            
       
#        ellipse = self.scene.addEllipse(10, 10, 100, 100, blackpen, redbrush)
#        rect    = self.scene.addRect   (-100, -100, 200, 200, blackpen, redbrush)
#        for i in [ellipse, rect]:
#            i.setFlag(i.ItemIsMovable)
#            i.setFlag(i.ItemIsSelectable)
        
