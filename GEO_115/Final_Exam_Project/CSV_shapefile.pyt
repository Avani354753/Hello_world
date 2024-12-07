import csv

# Define the path to the CSV file
csv_file_path = r"D:\New folder\Canada_Population.csv\98-401-X2021021_English_CSV_data.csv"

try:
    # Open the CSV file and read its contents
    with open(csv_file_path, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the header row
        for row in csvreader:
            print(row)
except PermissionError as e:
    print(f"PermissionError: {e}")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

    import arcpy
    import csv
    
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
    
            # Define the spatial reference (e.g., WGS 1984)
            spatial_reference = arcpy.SpatialReference(4326)
    
            # Create a new feature class
            arcpy.management.CreateFeatureclass(
                out_path=arcpy.env.workspace,
                out_name=output_shapefile,
                geometry_type="POINT",
                spatial_reference=spatial_reference
            )
    
            # Add fields to the feature class
            with open(input_csv_file, mode='r', newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                header = next(csvreader)  # Read the header row
                for field in header:
                    arcpy.management.AddField(output_shapefile, field, "TEXT")
    
            # Insert rows into the feature class
            with open(input_csv_file, mode='r', newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                header = next(csvreader)  # Read the header row
                cursor = arcpy.da.InsertCursor(output_shapefile, ["SHAPE@XY"] + header)
                for row in csvreader:
                    x, y = float(row[0]), float(row[1])  # Assuming the first two columns are X and Y coordinates
                    cursor.insertRow([(x, y)] + row[2:])
                del cursor
    
            return