import arcpy
import csv
import os

def csv_to_shapefile(input_csv_file, output_shapefile):
    """Converts a CSV file to a shapefile."""
    
    # Define the spatial reference (e.g., WGS 1984)
    # This sets the coordinate system for the shapefile
    spatial_reference = arcpy.SpatialReference(4326)

    # Extract the output path and name
    # This splits the output shapefile path into directory and file name
    out_path, out_name = os.path.split(output_shapefile)

    # Delete the shapefile if it already exists
    # This ensures that an existing shapefile with the same name is removed before creating a new one
    if arcpy.Exists(output_shapefile):
        arcpy.management.Delete(output_shapefile)

    # Create a new feature class
    # This creates a new shapefile with point geometry and the specified spatial reference
    arcpy.management.CreateFeatureclass(
        out_path=out_path,
        out_name=out_name,
        geometry_type="POINT",
        spatial_reference=spatial_reference
    )

    # Add fields to the feature class
    # Open the CSV file and read the header row to get the field names
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
    # Open the CSV file again to read the data rows
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
    # This adds the newly created shapefile to the current map in ArcGIS Pro
    try:
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        map = aprx.listMaps()[0]  # Get the first map in the project
        map.addDataFromPath(output_shapefile)
        arcpy.AddMessage(f"Shapefile created and added to the map: {output_shapefile}")
    except Exception as e:
        arcpy.AddError(f"Error adding shapefile to the map: {e}")

# Example usage
input_csv_file = r"D:\GEO 115\Final project\Planning_Local_Government_-7120577768134160590.csv"
output_shapefile = r"D:\GEO 115\Final project\Planning_Local_Government.shp"
csv_to_shapefile(input_csv_file, output_shapefile)