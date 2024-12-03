import arcpy
from arcpy.sa import *

# Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# Set workspace
arcpy.env.workspace = r"D:\ArcGIS\GEO_111\GEO_111_lab_5\GEO_111_lab_5.aprx"

# Define input raster
input_raster = r"D:\GEO 111\NB_ETM.pix"

# IsoData Classification
isodata_output = r"D:\GEO 111\Lab 5\New folder\isodata_output"
IsoClusterUnsupervisedClassification(input_raster, 5, 10, 20, isodata_output)

# Create Training Samples
training_area = r"D:\GEO 111\Lab 5\New folder\Training_Area"
arcpy.management.CreateTrainingSamples(input_raster, training_area, "2;3;4;5;7")

# Maximum Likelihood Classification
max_likelihood_output = r"D:\GEO 111\Lab 5\New folder\max_likelihood_output"
arcpy.management.MaximumLikelihoodClassification(input_raster, max_likelihood_output, training_area)

# Define input data
k_means_output = r"D:\GEO 111\Lab 5\New folder\k_means_output"
reference_data = r"D:\GEO 111\Lab 5\New folder\reference_data"

# Accuracy Assessment
confusion_matrix = arcpy.sa.ConfusionMatrix(max_likelihood_output, reference_data)

# Save results and generate reports
arcpy.management.SaveToLayerFile(k_means_output, "K_Means_Results.lyrx")
arcpy.management.SaveToLayerFile(isodata_output, "IsoData_Results.lyrx")
arcpy.management.SaveToLayerFile(max_likelihood_output, "Max_Likelihood_Results.lyrx")

print("Classification and accuracy assessment completed.")