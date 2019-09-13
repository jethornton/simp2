#!/usr/bin/python3
import platform

print('Python {}'.format(platform.python_version()))

import sys
print('File Location {}'.format(sys.argv[0]))

"""
install with 
pip3 install -e .
or 
pip3 install .
don't forget the trailing dot!
"""

import simple_import.importme as testme
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle(testme.title())
        versionLb = QLabel('Python {}'.format(platform.python_version()), self)
        versionLb.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(versionLb)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
