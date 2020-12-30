import sys
import functools
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel

class GUILogic(QMainWindow):
    
    imagenes = ["mario", "luigi", "yoshi", "dk", "peach", "wario", "daisy", "waluigi"]
    
    offset1 = 0
    offset2 = 4
    offset3 = 2
    offset4 = 1

    def __init__(self):
        super().__init__()
        uic.loadUi("qtui.ui", self)
        self.setimages()
        self.right1.mousePressEvent = functools.partial(self.changeimg1Right)
        self.right2.mousePressEvent = functools.partial(self.changeimg2Right)
        self.right3.mousePressEvent = functools.partial(self.changeimg3Right)
        self.right4.mousePressEvent = functools.partial(self.changeimg4Right)

        self.left1.mousePressEvent = functools.partial(self.changeimg1)
        self.left2.mousePressEvent = functools.partial(self.changeimg2)
        self.left3.mousePressEvent = functools.partial(self.changeimg3)
        self.left4.mousePressEvent = functools.partial(self.changeimg4)

        self.mas1.mousePressEvent = functools.partial(self.add, so=self.mas1)
        self.menos1.mousePressEvent = functools.partial(self.sub, so=self.menos1)
        self.mas2.mousePressEvent = functools.partial(self.add, so=self.mas2)
        self.menos2.mousePressEvent = functools.partial(self.sub, so=self.menos2)
        self.mas3.mousePressEvent = functools.partial(self.add, so=self.mas3)
        self.menos3.mousePressEvent = functools.partial(self.sub, so=self.menos3)
        self.mas4.mousePressEvent = functools.partial(self.add, so=self.mas4)
        self.menos4.mousePressEvent = functools.partial(self.sub, so=self.menos4)

        self.menos1.setVisible(False)
        self.menos2.setVisible(False)
        self.menos3.setVisible(False)
        self.menos4.setVisible(False)

        self.reset.mousePressEvent = functools.partial(self.resetvalues)

    def add(self, event, so):
        if "1" in so.objectName():
            x = int(self.val1.text()) + 1
            self.val1.setText(str(x))
            self.menos1.setVisible(True)
        elif "2" in so.objectName():
            x = int(self.val2.text()) + 1
            self.val2.setText(str(x))
            self.menos2.setVisible(True)
        elif "3" in so.objectName():
            x = int(self.val3.text()) + 1
            self.val3.setText(str(x))
            self.menos3.setVisible(True)
        elif "4" in so.objectName():
            x = int(self.val4.text()) + 1
            self.val4.setText(str(x))
            self.menos4.setVisible(True)
    
    def sub(self, event, so):
        if "1" in so.objectName():
            x = int(self.val1.text()) - 1
            self.val1.setText(str(x))
            if x == 0:
                self.menos1.setVisible(False)
        elif "2" in so.objectName():
            x = int(self.val2.text()) - 1
            self.val2.setText(str(x))
            if x == 0:
                self.menos2.setVisible(False)
        elif "3" in so.objectName():
            x = int(self.val3.text()) - 1
            self.val3.setText(str(x))
            if x == 0:
                self.menos3.setVisible(False)
        elif "4" in so.objectName():
            x = int(self.val4.text()) - 1
            self.val4.setText(str(x))
            if x == 0:
                self.menos4.setVisible(False)
    
    def resetvalues(self, event):
        self.img1.setStyleSheet("border-image: url(mario.png);")
        self.img2.setStyleSheet("border-image: url(peach.png);")
        self.img3.setStyleSheet("border-image: url(yoshi.png);")
        self.img4.setStyleSheet("border-image: url(luigi.png);")
        self.val1.setText("0")
        self.val2.setText("0")
        self.val3.setText("0")
        self.val4.setText("0")
        self.menos1.setVisible(False)
        self.menos2.setVisible(False)
        self.menos3.setVisible(False)
        self.menos4.setVisible(False)

    def setimages(self):
        self.img1.setStyleSheet("border-image: url(mario.png);")
        self.img2.setStyleSheet("border-image: url(peach.png);")
        self.img3.setStyleSheet("border-image: url(yoshi.png);")
        self.img4.setStyleSheet("border-image: url(luigi.png);")
        


    def changeimg1(self, event):
        self.offset1 -= 1
        if self.offset1 < 0:
            self.offset1 = 7
            self.img1.setStyleSheet("border-image: url(waluigi.png);")
        else:
            self.img1.setStyleSheet("border-image: url({}.png);".format(self.imagenes[self.offset1]))
    
    def changeimg2(self, event):
        self.offset2 -= 1
        if self.offset2 < 0:
            self.offset2 = 7
            self.img2.setStyleSheet("border-image: url(waluigi.png);")
        else:
            self.img2.setStyleSheet("border-image: url({}.png);".format(self.imagenes[self.offset2]))
    
    def changeimg3(self, event):
        self.offset3 -= 1
        if self.offset3 < 0:
            self.offset3 = 7
            self.img3.setStyleSheet("border-image: url(waluigi.png);")
        else:
            self.img3.setStyleSheet("border-image: url({}.png);".format(self.imagenes[self.offset3]))

    def changeimg4(self, event):
        self.offset4 -= 1
        if self.offset4 < 0:
            self.offset4 = 7
            self.img4.setStyleSheet("border-image: url(waluigi.png);")
        else:
            self.img4.setStyleSheet("border-image: url({}.png);".format(self.imagenes[self.offset4]))
    
    def changeimg1Right(self, event):
        self.offset1 += 1
        if self.offset1 > 7:
            self.offset1 = 0
            self.img1.setStyleSheet("border-image: url(mario.png);")
        else:
            self.img1.setStyleSheet("border-image: url({}.png);".format(self.imagenes[self.offset1]))
    
    def changeimg2Right(self, event):
        self.offset2 += 1
        if self.offset2 > 7:
            self.offset2 = 0
            self.img2.setStyleSheet("border-image: url(mario.png);")
        else:
            self.img2.setStyleSheet("border-image: url({}.png);".format(self.imagenes[self.offset2]))
    
    def changeimg3Right(self, event):
        self.offset3 += 1
        if self.offset3 > 7:
            self.offset3 = 0
            self.img3.setStyleSheet("border-image: url(mario.png);")
        else:
            self.img3.setStyleSheet("border-image: url({}.png);".format(self.imagenes[self.offset3]))

    def changeimg4Right(self, event):
        self.offset4 += 1
        if self.offset4 > 7:
            self.offset4 = 0
            self.img4.setStyleSheet("border-image: url(mario.png);")
        else:
            self.img4.setStyleSheet("border-image: url({}.png);".format(self.imagenes[self.offset4]))
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = GUILogic()
    GUI.show()
    sys.exit(app.exec_())