# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "My_Buffer"
        self.alias = "buffer_toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buf_Tool"
        self.description = "Tool creates a buffer"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = None
        
        #First parameter
        param0 = arcpy.Parameter(
            displayName = "Input Feature Class",
            name = "in_features",
            datatype = "GPFeatureLayer",
            parameterType = "Required",
            direction = "Input")
        #Second parameter
        param1 = arcpy.Parameter(
            displayName = "Output Feature Class",
            name = "out_features",
            datatype = "GPFeatureLayer",
            parameterType = "Required",
            direction = "Output")
        #third parameter
        param2 = arcpy.Parameter(
            displayName = "Buffer Distance",
            name = "bf_distance",
            datatype = "GPLinearUnit",
            parameterType = "Required",
            direction = "Input")
        #Forth parameter
        param3 = arcpy.Parameter(
            displayName = "Method",
            name = "bf_method",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input")
        param3.filter.type = "Value List"
        param3.filter.list = ["PLANAR", "GEODESIC"]

        param3.parameterDependencies = [param0.name]
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        in_features = parameters[0].valueAsText
        out_features = parameters[1].valueAsText
        bf_distance = parameters[2].valueAsText
        bf_method = parameters[3].valueAsText

        arcpy.Buffer_analysis(in_features, out_features, bf_distance, method=bf_method)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
