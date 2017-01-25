from qgis.core import QgsFeature,  QgsMapLayerRegistry
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


class AutoForm:
    def __init__( self, iface ):
        self.iface = iface

    def initGui(self):

        self.action = QAction("Generate Form", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("activated()"), self.validateLayer)
        self.iface.addPluginToMenu("AutoForm", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("AutoForm", self.action)

    def validateLayer(self):
        layer = self.iface.activeLayer()
        if layer:
            features = layer.getFeatures()
            for feature in features:
                field_index = 0
                for field in feature.fields():
                    f_type = field.typeName()
                    field_index = field_index + 1
                    print field.name()
                    if f_type == "text":
                        layer.setEditorWidgetV2(field_index, 'TextEdit')
                    if f_type == "varchar":
                        pass
                    if f_type == "date":
                        layer.setEditorWidgetV2(field_index, 'DateTime')
                    if f_type == "bool":
                        layer.setEditorWidgetV2(field_index, 'CheckBox')
                    if f_type == "int8":
                        pass
                    if f_type == "int4":
                        pass
        else:
            print "Please select a Layer"
