#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
QApplication.primaryScreen().grabWindow(0).save('s1.png', 'png')
