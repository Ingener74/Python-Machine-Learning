#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

subprocess.Popen(['pyside-rcc', 'res/res.qrc', '-o', 'res_rc.py'])

subprocess.Popen(['pyside-uic', 'res/main.ui', '-o', 'main.py'])
# subprocess.Popen(['pyside-uic', 'res/add.ui', '-o', 'add.py'])
# subprocess.Popen(['pyside-uic', 'res/settings.ui', '-o', 'settings.py'])
