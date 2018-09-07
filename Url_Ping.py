# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 21:27:05 2018

@author: arti jaiswal
"""

import socket
from urllib.request import urlopen, URLError, HTTPError
import traceback

def urlPing():
    url = 'https://www.google.com/'
    try :
        response = urlopen( url )
    except HTTPError :
        return 'The server couldn\'t fulfill the request. Reason:'
    except URLError :
        return 'We failed to reach a server. Reason:'
        traceback.print_exc()
    else :
        html = response.read()
        return 'Got the response.'
        
urlPing()
from PyQt5 import Qt
import sys
import threading
app = Qt.QApplication(sys.argv)
systemtray_icon= Qt.QSystemTrayIcon(Qt.QIcon(r'C:/Users/arti jaiswal/Desktop/video-camera-icon.png'), app)
systemtray_icon.show()
def notification():
    threading.Timer(60.0, notification).start()
    systemtray_icon.showMessage('Visual Studio status', urlPing())

notification()