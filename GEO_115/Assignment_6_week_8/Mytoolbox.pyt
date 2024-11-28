# -*- coding: utf-8 -*-

import arcpy



class MyToolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "My Toolbox"
        self.alias = "my_toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class ClipTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clip Tool"
        self.description = "Clips the features to the extent of the clip features."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = []
        params.append(arcpy.Parameter(
            displayName="Input Features",
            name="input_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"))
        params.append(arcpy.Parameter(
            displayName="Clip Features",
            name="clip_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"))
        params.append(arcpy.Parameter(
            displayName="Output Features",
            name="output_features",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output"))
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
        try:
            input_features = parameters[0].valueAsText
            clip_features = parameters[1].valueAsText
            output_features = parameters[2].valueAsText
            arcpy.Clip_analysis(input_features, clip_features, output_features)
            messages.addMessage("Clip analysis complete.")
        except Exception as e:
            messages.addErrorMessage(f"An error occurred: {str(e)}")
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
