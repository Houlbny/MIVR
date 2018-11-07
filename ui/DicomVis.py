# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DicomVis.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1239, 755)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, -1, -1, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_XY_slice = QtWidgets.QLabel(Form)
        self.label_XY_slice.setObjectName("label_XY_slice")
        self.verticalLayout.addWidget(self.label_XY_slice)
        self.XYPlaneWidget = QVTKWidget(Form)
        self.XYPlaneWidget.setObjectName("XYPlaneWidget")
        self.verticalLayout.addWidget(self.XYPlaneWidget)
        self.XYSlider = QtWidgets.QSlider(Form)
        self.XYSlider.setOrientation(QtCore.Qt.Horizontal)
        self.XYSlider.setObjectName("XYSlider")
        self.verticalLayout.addWidget(self.XYSlider)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_YZ_slice = QtWidgets.QLabel(Form)
        self.label_YZ_slice.setObjectName("label_YZ_slice")
        self.verticalLayout_2.addWidget(self.label_YZ_slice)
        self.YZPlaneWidget = QVTKWidget(Form)
        self.YZPlaneWidget.setObjectName("YZPlaneWidget")
        self.verticalLayout_2.addWidget(self.YZPlaneWidget)
        self.YZSlider = QtWidgets.QSlider(Form)
        self.YZSlider.setOrientation(QtCore.Qt.Horizontal)
        self.YZSlider.setObjectName("YZSlider")
        self.verticalLayout_2.addWidget(self.YZSlider)
        self.verticalLayout_2.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_XZ_slice = QtWidgets.QLabel(Form)
        self.label_XZ_slice.setObjectName("label_XZ_slice")
        self.verticalLayout_3.addWidget(self.label_XZ_slice)
        self.XZPlaneWidget = QVTKWidget(Form)
        self.XZPlaneWidget.setObjectName("XZPlaneWidget")
        self.verticalLayout_3.addWidget(self.XZPlaneWidget)
        self.XZSlider = QtWidgets.QSlider(Form)
        self.XZSlider.setOrientation(QtCore.Qt.Horizontal)
        self.XZSlider.setObjectName("XZSlider")
        self.verticalLayout_3.addWidget(self.XZSlider)
        self.verticalLayout_3.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_Volume = QtWidgets.QLabel(Form)
        self.label_Volume.setObjectName("label_Volume")
        self.verticalLayout_5.addWidget(self.label_Volume)
        self.VolumeWidget = QVTKWidget(Form)
        self.VolumeWidget.setObjectName("VolumeWidget")
        self.verticalLayout_5.addWidget(self.VolumeWidget)
        self.verticalLayout_5.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.window_center_num = QtWidgets.QLabel(Form)
        self.window_center_num.setMinimumSize(QtCore.QSize(45, 22))
        self.window_center_num.setObjectName("window_center_num")
        self.gridLayout.addWidget(self.window_center_num, 1, 2, 1, 1)
        self.WindowWidthSlider = QtWidgets.QSlider(Form)
        self.WindowWidthSlider.setMinimumSize(QtCore.QSize(181, 22))
        self.WindowWidthSlider.setMaximumSize(QtCore.QSize(181, 22))
        self.WindowWidthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.WindowWidthSlider.setObjectName("WindowWidthSlider")
        self.gridLayout.addWidget(self.WindowWidthSlider, 2, 1, 1, 1)
        self.WindowCenterLabel = QtWidgets.QLabel(Form)
        self.WindowCenterLabel.setObjectName("WindowCenterLabel")
        self.gridLayout.addWidget(self.WindowCenterLabel, 1, 0, 1, 1)
        self.WindowWidthLabel = QtWidgets.QLabel(Form)
        self.WindowWidthLabel.setObjectName("WindowWidthLabel")
        self.gridLayout.addWidget(self.WindowWidthLabel, 2, 0, 1, 1)
        self.WindowCenterSlider = QtWidgets.QSlider(Form)
        self.WindowCenterSlider.setMinimumSize(QtCore.QSize(181, 22))
        self.WindowCenterSlider.setMaximumSize(QtCore.QSize(181, 22))
        self.WindowCenterSlider.setOrientation(QtCore.Qt.Horizontal)
        self.WindowCenterSlider.setObjectName("WindowCenterSlider")
        self.gridLayout.addWidget(self.WindowCenterSlider, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.window_width_num = QtWidgets.QLabel(Form)
        self.window_width_num.setMinimumSize(QtCore.QSize(45, 22))
        self.window_width_num.setObjectName("window_width_num")
        self.gridLayout.addWidget(self.window_width_num, 2, 2, 1, 1)
        self.opened_view = QtWidgets.QListView(Form)
        self.opened_view.setObjectName("opened_view")
        self.gridLayout.addWidget(self.opened_view, 3, 1, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DICOM Visualizer"))
        self.label_XY_slice.setText(_translate("Form", "XY slice"))
        self.label_YZ_slice.setText(_translate("Form", "YZ slice"))
        self.label_XZ_slice.setText(_translate("Form", "XZ slice"))
        self.label_Volume.setText(_translate("Form", "Volume render"))
        self.window_center_num.setText(_translate("Form", "0"))
        self.WindowCenterLabel.setText(_translate("Form", "Window Center"))
        self.WindowWidthLabel.setText(_translate("Form", "Window Width"))
        self.window_width_num.setText(_translate("Form", "0"))

from QVTKWidget import QVTKWidget
