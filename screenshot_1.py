#!/usr/bin/env python3

import os
from PySide2.QtGui import QScreen
from PySide2.QtWidgets import QApplication

app = QApplication.instance()
screenshot = QScreen.grabWindow(app.desktop().winId())
screenshot.save(os.path.expanduser("~/screenshot.jpg"), "jpg")
