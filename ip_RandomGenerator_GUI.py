#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import asyncio
import PyQt5.QtWidgets as qw
import asyncqt
from asyncqt import asyncSlot
import random



class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(230, 200)
        self.move(300, 300)
        self.setWindowTitle('Random generator')

        self.goBtn = qw.QPushButton('Number', self)
        self.goBtn.move(50, 50)
        self.goBtn.clicked.connect(self.performRandomNumber)

        self.goFileBtn = qw.QPushButton('Latin letter', self)
        self.goFileBtn.move(50, 100)
        self.goFileBtn.clicked.connect(self.performRandomLatinLetter)

        self.quitBtn = qw.QPushButton('Quit', self)
        self.quitBtn.move(50, 150)
        self.quitBtn.clicked.connect(self.close)


    @asyncSlot(bool)
    async def performRandomNumber(self, evt):
        self.goBtn.setEnabled(False)
        c = random.randint(1,1000000)
        print("Random number from 1 to 1000000: ", c)
        self.goBtn.setEnabled(True)

    @asyncSlot(bool)
    async def performRandomLatinLetter(self, evt):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = random.randint(0,25)
        e = alphabet[d]
        print("Random latin letter: ", e)


if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    loop = asyncqt.QEventLoop(app)
    asyncio.set_event_loop(loop)

    w = MainWindow()
    w.show()

    with loop:
        sys.exit(loop.run_forever())