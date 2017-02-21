# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playblast_dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_PlayblastDialog(object):
    def setupUi(self, PlayblastDialog):
        PlayblastDialog.setObjectName("PlayblastDialog")
        PlayblastDialog.resize(470, 132)
        self.gridLayout = QtGui.QGridLayout(PlayblastDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmbPercentage = QtGui.QComboBox(PlayblastDialog)
        self.cmbPercentage.setObjectName("cmbPercentage")
        self.horizontalLayout_3.addWidget(self.cmbPercentage)
        self.chbUploadToShotgun = QtGui.QCheckBox(PlayblastDialog)
        self.chbUploadToShotgun.setObjectName("chbUploadToShotgun")
        self.horizontalLayout_3.addWidget(self.chbUploadToShotgun)
        self.chbShowViewer = QtGui.QCheckBox(PlayblastDialog)
        self.chbShowViewer.setChecked(True)
        self.chbShowViewer.setObjectName("chbShowViewer")
        self.horizontalLayout_3.addWidget(self.chbShowViewer)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_3 = QtGui.QGroupBox(PlayblastDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spB_day = QtGui.QSpinBox(self.groupBox_3)
        self.spB_day.setObjectName("spB_day")
        self.horizontalLayout_2.addWidget(self.spB_day)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.spB_hrs = QtGui.QSpinBox(self.groupBox_3)
        self.spB_hrs.setObjectName("spB_hrs")
        self.horizontalLayout_2.addWidget(self.spB_hrs)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.btnPlayblast = QtGui.QPushButton(PlayblastDialog)
        self.btnPlayblast.setMinimumSize(QtCore.QSize(450, 0))
        self.btnPlayblast.setObjectName("btnPlayblast")
        self.verticalLayout.addWidget(self.btnPlayblast)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PlayblastDialog)
        QtCore.QMetaObject.connectSlotsByName(PlayblastDialog)

    def retranslateUi(self, PlayblastDialog):
        PlayblastDialog.setWindowTitle(QtGui.QApplication.translate("PlayblastDialog", "Videogyan Playblast Tool-v0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.chbUploadToShotgun.setText(QtGui.QApplication.translate("PlayblastDialog", "Submit to Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.chbShowViewer.setText(QtGui.QApplication.translate("PlayblastDialog", "Open Mov in RV Player", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("PlayblastDialog", "Time Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PlayblastDialog", "Time Consumed on current Task ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PlayblastDialog", "Day", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PlayblastDialog", "Hours", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPlayblast.setText(QtGui.QApplication.translate("PlayblastDialog", "Playblast", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
