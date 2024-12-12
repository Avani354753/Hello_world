import arcpy
import csv
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "CSV to Shapefile Toolbox"
        self.alias = "csv_to_shapefile_toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [CSVToShapefile]

class CSVToShapefile(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "CSV to Shapefile"
        self.description = "Converts a CSV file to a shapefile."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        # Input CSV file parameter
        param0 = arcpy.Parameter(
            displayName="Input CSV File",
            name="input_csv_file",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")
        params.append(param0)

        # Output Shapefile parameter
        param1 = arcpy.Parameter(
            displayName="Output Shapefile",
            name="output_shapefile",
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
        input_csv_file = parameters[0].valueAsText
        output_shapefile = parameters[1].valueAsText

        csv_to_shapefile(input_csv_file, output_shapefile)

        return

def csv_to_shapefile(input_csv_file, output_shapefile):
    """Converts a CSV file to a shapefile."""
    
    # Define the spatial reference (e.g., WGS 1984)
    spatial_reference = arcpy.SpatialReference(4326)

    # Extract the output path and name
    out_path, out_name = os.path.split(output_shapefile)

    # Create a new feature class
    arcpy.management.CreateFeatureclass(
        out_path=out_path,
        out_name=out_name,
        geometry_type="POINT",
        spatial_reference=spatial_reference
    )

    # Add fields to the feature class
    with open(input_csv_file, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the header row
        field_mappings = {}
        for field in header[:-2]:  # Skip the last two columns (x and y coordinates)
            field_name = field.strip()[:10]  # Remove any leading/trailing whitespace and truncate to 10 characters
            field_name = arcpy.ValidateFieldName(field_name, out_path)  # Ensure the field name is valid
            field_mappings[field] = field_name
            arcpy.management.AddField(output_shapefile, field_name, "TEXT")

    # Insert rows into the feature class
    with open(input_csv_file, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the header row
        field_names = [field_mappings[field] for field in header[:-2]]  # Use the validated field names
        cursor = arcpy.da.InsertCursor(output_shapefile, ["SHAPE@XY"] + field_names)
        for row in csvreader:
            try:
                x, y = float(row[-2]), float(row[-1])  # Assuming the last two columns are x and y coordinates
                cursor.insertRow([(x, y)] + [row[header.index(field)] for field in header[:-2]])
            except ValueError:
                arcpy.AddWarning(f"Skipping row with invalid coordinates: {row}")
        del cursor

    # Add the shapefile to the current map
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    map = aprx.activeMap
    map.addDataFromPath(output_shapefile)
    arcpy.AddMessage(f"Shapefile created and added to the map: {output_shapefile}")