# Wetland Analysis Toolbox

## Overview
The **Wetland Analysis Toolbox** is a custom Python toolbox designed for ArcGIS Pro that identifies wetlands located within a specified distance from national parks. This tool automates the spatial query analysis process, making it easier for users to conduct environmental assessments and planning.

## Features
- Select national parks based on an optional province code.
- Create a buffer around selected national parks.
- Identify wetlands that fall within the buffer zone.
- Export the selected wetlands to a new feature class.

## Requirements
- **ArcGIS Pro** (version X.X or later)
- **Python** (version X.X or later)
- **arcpy** module (included with ArcGIS Pro)

## Installation
1. Clone the GitHub repository or download the ZIP file.
2. Open ArcGIS Pro and create a new project.
3. Add the `WetlandAnalysis.pyt` toolbox to your project:
   - In the Catalog pane, right-click on **Toolboxes**.
   - Select **Add Toolbox** and browse to the location of `WetlandAnalysis.pyt`.

## Usage
1. Open the Wetland Analysis Toolbox in ArcGIS Pro.
2. Select the **Wetlands Near National Parks** tool.
3. Fill in the required parameters:
   - **National Parks Feature Class**: Input feature class containing national parks.
   - **Wetlands Feature Class**: Input feature class containing wetlands.
   - **Buffer Distance**: Distance around national parks to search for wetlands (e.g., "20000 Meters").
   - **Output Feature Class**: Specify the output feature class for selected wetlands.
   - **Province Code (Optional)**: Enter a province code to filter national parks (if desired).
4. Click **Run** to execute the tool.

## Example
Here is an example of how to run the tool programmatically:

```python
import arcpy

# Set parameters
parks_fc = "path/to/national_parks.shp"
wetlands_fc = "path/to/wetlands.shp"
buffer_distance = "20000 Meters"
output_fc = "path/to/output_wetlands.shp"
province_code = "ON"  # Optional

# Run the tool
arcpy.management.ExecuteToolbox("WetlandAnalysis.pyt", "WetlandsNearParks", parks_fc, wetlands_fc, buffer_distance, output_fc, province_code)