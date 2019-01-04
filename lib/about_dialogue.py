# 'About' dialogue for CalCorrupt
# 4th January, 2019

from lib import uitext
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 197)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 10, 341, 131))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 150, 82, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About CalCorrupt "+uitext.VERSION))
        self.label.setText(_translate("Dialog", "CalCorrupt "+uitext.VERSION+" is an open-source file corrupter\n"
"licenced under the GNU GPL-3.0-or-later.\n"
"\n"
"Authors:\n"
"github.com/Calendis"))
        self.pushButton.setText(_translate("Dialog", "OK"))

