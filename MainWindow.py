#!/usr/bin/env python



from PyQt5 import QtCore, QtWidgets, QtGui
from DicomVis import DicomVis
from MainWindow_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dicomVisWidget = DicomVis()
        self.opened_list = []

        self.ui.verticalLayout.insertWidget(0, self.dicomVisWidget)

        studypath = ''
        #self.dicomVisWidget.load_study_from_path(studypath)

    def closeEvent(self, event):
        replay = QtWidgets.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if replay == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        #得到主窗口大小
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @QtCore.pyqtSlot()
    def on_loadStudyBtn_clicked(self):
        dicompath = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Open Directory", "/home", QtWidgets.QFileDialog.ShowDirsOnly))
        try:
            self.dicomVisWidget.load_study_from_path(dicompath)

        except:
            infobox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", "Something went wrong")
            infobox.exec_()

        self.opened_list.append(dicompath.split('/')[-1])
        self.model = QtGui.QStandardItemModel()
        for file in self.opened_list:
            item = QtGui.QStandardItem(file)
            item.setCheckState(False)
            item.setCheckable(True)
            self.model.appendRow(item)
            self.dicomVisWidget.ui.opened_view.setModel(self.model)

    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        infobox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "About", "by:")
        infobox.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exitCode = app.exec_()
    sys.exit(exitCode)


