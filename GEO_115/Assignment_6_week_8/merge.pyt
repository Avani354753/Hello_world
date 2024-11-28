# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Merge Toolbox"
        self.alias = "merge_toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [MergeFeatures]


class MergeFeatures(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Merge Features"
        self.description = "Merges multiple feature classes or shapefiles into a single feature class."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        # Input Features parameter
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="input_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input",
            multiValue=True)
        params.append(param0)

        # Output Feature Class parameter
        param1 = arcpy.Parameter(
            displayName="Output Feature Class",
            name="output_feature_class",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output")
        params.append(param1)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal validation is performed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool parameter."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_features = parameters[0].valueAsText.split(";")
        output_feature_class = parameters[1].valueAsText

        # Perform the merge
        arcpy.management.Merge(input_features, output_feature_class)

        return
