import arcpy

class BufferTool(object):
    def __init__(self):
        self.label = "Buffer Tool"
        self.description = "Creates a buffer around the input feature."
        self.canRunInBackground = False
    
    def getParameterInfo(self):
        params = []
        
        params.append(arcpy.Parameter(
            displayName="Input Feature",
            name="input_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"))
        
        params.append(arcpy.Parameter(
            displayName="Buffer Distance",
            name="buffer_distance",
            datatype="GPLinearUnit",
            parameterType="Required",
            direction="Input"))
     
        params.append(arcpy.Parameter(
            displayName="Output Feature",
            name="output_feature",
            datatype="DPFeatureClass",
            parameterType="Required",
            direction="Output"))
        
        return params
    def execute(self, parameters, messages):
        try:
            input_feature = parameters[0].valueAsText
            buffer_distance = parameters[1].valueAsText
            output_feature = parameters[2].valueAsText
            
            arcpy.Buffer_analysis(input_feature, output_feature, buffer_distance)
            messages.addMessage("Buffer analysis complete.")
        except Exception as e:
            messages.addErrorMessage(f"An error occurred: {str(e)}")
        return