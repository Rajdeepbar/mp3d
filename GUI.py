import matplotlib.pyplot as mp                             #Plot the graph         
import sys                                                 #System-specific parameters and functions
from PyQt5 import QtWidgets,QtGui,QtCore,sip               #Creating a GUI
from functools import partial                              #Create partial Functions
import Application


Search_Output = 5


class Window(QtWidgets.QWidget):

    def __init__(self,Options):
        QtWidgets.QWidget.__init__(self)
        super().__init__()                                 #used for providing control to the inherited module
        self.setGeometry(700,200,500,500)
        self.setWindowTitle("MP3 Downloader")
        self.setWindowIcon(QtGui.QIcon('Music.jpg'))
        self.song = Application.MP3D()
        self.home()
        self.option = Options
        

    def home(self):
        self.le = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("Search")
        self.btn1 = QtWidgets.QPushButton("Download")
        self.result = QtWidgets.QTextEdit(self)
        self.result.setReadOnly(True)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.le)
        box.addWidget(self.result)
        box.addWidget(self.btn)
        box.addWidget(self.btn1)
        self.setLayout(box)
        self.btn.clicked.connect(self.__search__)
        self.btn1.clicked.connect(self.__download__)
        self.show()
        

    def __search__(self):
        self.result.clear()
        #self.result.insertPlainText(" Searching...")
        i = 1
        text = self.le.text()
        minutes = 0
        self.title, minutes, seconds = self.song.search(text,self.option)

        for a in self.title:
            if a is not "":
                self.result.append(str(i) + "-"+ a)
                self.result.insertPlainText(" ("+minutes[i-1] + "min " + seconds[i-1] + " sec)")
                i = i+1
                if i > self.option:
                    break

        self.le.clear()


    def __download__(self):
        check = 0
        option = self.le.text()
        if option in '123456789':
            self.result.setText(" Downloading...")
            check = self.song.download(int(option))
        else:
            self.result.setText(" Try Again")
        if check== 1:
            self.result.setText(" Download Completed")
                
        

app = QtWidgets.QApplication(sys.argv)
song = Application.MP3D()
w = Window(Search_Output)
sys.exit(app.exec_())
