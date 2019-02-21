#!/usr/bin/python3
# -*- coding: utf-8 -*-
import platform

print('Python {}'.format(platform.python_version()))

"""
install with 
pip3 install -e .
or 
pip3 install .
don't forget the trailing dot!
"""

import importme

print(importme.test())

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Simple')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
