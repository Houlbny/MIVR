#!/usr/bin/env python

import vtk
from PyQt5 import QtWidgets, QtCore, QtGui
from DicomVis_ui import Ui_Form

'''
try:
    from lib import StudyData as StudyData
    from lib import VisuAnalysisWidget
except(ImportError):
    class VisuAnalysisWidget(QtWidgets.QWidget):
        pass
'''

class VisuAnalysisWidget(QtWidgets.QWidget):
    pass


class DicomVis(VisuAnalysisWidget):

    def __init__(self, parent = None):

        self.reader = vtk.vtkDICOMImageReader()
        self.dataExtent = []
        self.dataDimensions = []
        self.dataRange = ()

        # initialize GUI
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.WindowCenterSlider.setRange(0, 1000)
        self.ui.WindowWidthSlider.setRange(0, 1000)
        '''
        opened_list = [u'文件5']
        self.model = QtGui.QStandardItemModel()
        for file in opened_list:
            item = QtGui.QStandardItem(file)
            item.setCheckState(False)
            item.setCheckable(True)
            self.model.appendRow(item)
            self.ui.opened_view.setModel(self.model)
        '''

        # define viewers
        [self.viewerXY, self.viewerYZ, self.viewerXZ] = [vtk.vtkImageViewer2() for x in range(3)]

        # attach interactors to viewers
        self.viewerXY.SetupInteractor(self.ui.XYPlaneWidget)
        self.viewerYZ.SetupInteractor(self.ui.YZPlaneWidget)
        self.viewerXZ.SetupInteractor(self.ui.XZPlaneWidget)

        # set render windows for viewers
        self.viewerXY.SetRenderWindow(self.ui.XYPlaneWidget.GetRenderWindow())
        self.viewerYZ.SetRenderWindow(self.ui.YZPlaneWidget.GetRenderWindow())
        self.viewerXZ.SetRenderWindow(self.ui.XZPlaneWidget.GetRenderWindow())

        # set slicing orientation for viewers
        self.viewerXY.SetSliceOrientationToXZ()
        self.viewerYZ.SetSliceOrientationToYZ()
        self.viewerXZ.SetSliceOrientationToXY()

        # rotate image
        act = self.viewerYZ.GetImageActor()
        act.SetOrientation(90, 0, 0)

        # setup volume rendering
        self.volRender = vtk.vtkRenderer()
        self.volRenWin = self.ui.VolumeWidget.GetRenderWindow()
        self.volRenWin.AddRenderer(self.volRender)

        #self.rayCastFunction = vtk.vtkVolumeRayCastCompositeFunction()
        #self.volumeMapper = vtk.vtkFixedPointVolumeRayCastMapper()
        #self.volumeMapper.SetBlendModeToComposite()
        #self.volumeMapper.SetVolumeRayCastFunction(self.rayCastFunction)
        self.volumeMapper = vtk.vtkGPUVolumeRayCastMapper()


        volumeColor = vtk.vtkColorTransferFunction()
        volumeColor.AddRGBPoint(0,    0.0, 0.0, 0.0)
        volumeColor.AddRGBPoint(500,  1.0, 0.5, 0.3)
        volumeColor.AddRGBPoint(1000, 1.0, 0.5, 0.3)
        volumeColor.AddRGBPoint(1150, 1.0, 1.0, 0.9)
        self.volumeColor = volumeColor

        volumeScalarOpacity = vtk.vtkPiecewiseFunction()
        volumeScalarOpacity.AddPoint(0, 0.00)
        volumeScalarOpacity.AddPoint(50, 0.15)
        volumeScalarOpacity.AddPoint(100, 0.15)
        volumeScalarOpacity.AddPoint(115, 0.85)
        self.volumeScalarOpacity = volumeScalarOpacity

        volumeGradientOpacity = vtk.vtkPiecewiseFunction()
        volumeGradientOpacity.AddPoint(0,   0.0)
        volumeGradientOpacity.AddPoint(100,  0.5)
        volumeGradientOpacity.AddPoint(500, 1)
        self.volumeGradientOpacity = volumeGradientOpacity

        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(volumeColor)
        volumeProperty.SetScalarOpacity(volumeScalarOpacity)
        volumeProperty.SetGradientOpacity(volumeGradientOpacity)
        volumeProperty.SetInterpolationTypeToLinear()
        volumeProperty.ShadeOn()
        volumeProperty.SetAmbient(0.4)
        volumeProperty.SetDiffuse(0.6)
        volumeProperty.SetSpecular(0.2)
        self.volumeProperty = volumeProperty

        volume = vtk.vtkVolume()
        volume.SetMapper(self.volumeMapper)
        volume.SetProperty(self.volumeProperty)
        self.volume = volume

        self.volRender.AddViewProp(volume)


        width_bar = self.ui.WindowWidthSlider
        center_bar = self.ui.WindowCenterSlider
        width_bar.valueChanged.connect(self.changeValue)
        center_bar.valueChanged.connect(self.changeValue)


    def changeValue(self):
        value_width = str(self.ui.WindowWidthSlider.value())
        value_center = str(self.ui.WindowCenterSlider.value())
        self.ui.window_center_num.setText(value_center)
        self.ui.window_width_num.setText(value_width)

    def updateData(self, studydata):
        self.load_study_from_path(studydata.getPath())


    def load_study_from_path(self, studyPath):

        # Update reader
        self.reader.SetDirectoryName(studyPath)
        self.reader.Update()

        self.xyMapper = vtk.vtk

        # Get data dimensionality
        self.dataExtent = self.reader.GetDataExtent()
        dataDimensionX = self.dataExtent[1]-self.dataExtent[0]
        dataDimensionY = self.dataExtent[3]-self.dataExtent[2]
        dataDimensionZ = self.dataExtent[5]-self.dataExtent[4]
        self.dataDimensions = [dataDimensionX, dataDimensionY, dataDimensionZ]

        # Calculate index of middle slice
        midslice1 = int((self.dataExtent[1]-self.dataExtent[0])/2 + self.dataExtent[0])
        midslice2 = int((self.dataExtent[3]-self.dataExtent[2])/2 + self.dataExtent[2])
        midslice3 = int((self.dataExtent[5]-self.dataExtent[4])/2 + self.dataExtent[4])

        # Calculate enter
        center = [midslice1, midslice2, midslice3]

        # Get data range
        self.dataRange = self.reader.GetOutput().GetPointData().GetArray(0).GetRange()
        print(self.dataRange)

        # Set current slice to the middle one
        for pair in zip([self.viewerXY, self.viewerYZ, self.viewerXZ], [midslice1, midslice2, midslice3]):
            pair[0].SetInputData(self.reader.GetOutput())
            pair[0].SetSlice(pair[1])
            pair[0].Render()
        pass

        # Set range and proper value for slice sliders
        for pair in zip([self.ui.XYSlider, self.ui.YZSlider, self.ui.XZSlider,], self.dataDimensions, [midslice1, midslice2, midslice3]):
            pair[0].setRange(0, pair[1])
            pair[0].setValue(pair[2])

        # Set range and value for windowing sliders
        self.ui.WindowCenterSlider.setRange(int(self.dataRange[0]), int(self.dataRange[1]))
        self.ui.WindowWidthSlider.setRange(1, int(self.dataRange[1]))

        # set input for volume renderer
        self.volumeMapper.SetInputConnection(self.reader.GetOutputPort())
        self.volRenWin.Render()


    # setup slots for slicing sliders
    @QtCore.pyqtSlot(int)
    def on_XYSlider_valueChanged(self, value):
        self.viewerXY.SetSlice(value)

    @QtCore.pyqtSlot(int)
    def on_YZSlider_valueChanged(self, value):
        self.viewerYZ.SetSlice(value)

    @QtCore.pyqtSlot(int)
    def on_XZSlider_valueChanged(self, value):
        self.viewerXZ.SetSlice(value)


    # Setup slots for windowing sliders
    @QtCore.pyqtSlot(int)
    def on_WindowCenterSlider_valueChanged(self, value):
        for x in [self.viewerXY, self.viewerXZ, self.viewerYZ]:
            x.SetColorLevel(value)
            x.Render()

    @QtCore.pyqtSlot(int)
    def on_WindowWidthSlider_valueChanged(self, value):
        for x in [self.viewerXY, self.viewerXZ, self.viewerYZ]:
            x.SetColorWindow(value)
            x.Render()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DicomVis()
    print(type(window))
    window.show()

    #studyPath = "/Users/apple/Desktop/3Dplayer/sample"
    #window.load_study_from_path(studyPath)
    exitStatus = app.exec_()
    #del(window)
    sys.exit(exitStatus)
