import cv2
import numpy as np
import pandas as pd
import os
from PIL import Image
import requests
import time

# Function to download the cars.xml file
def download_cars_xml(url, save_path, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(save_path, 'wb') as file:
                    file.write(response.content)
                print("cars.xml downloaded successfully")
                return True
            else:
                print(f"Attempt {attempt + 1} failed: {response.status_code}")
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
        time.sleep(2)  # Wait for 2 seconds before retrying
    return False

# Disable the decompression bomb check
Image.MAX_IMAGE_PIXELS = None

# 📌 1️⃣ Load the UBC Aerial Image
image_path = r"D:\ArcGIS\GEO_215\GEO_215_Assignment_3\UBC_Campus_Clip.tif"
if not os.path.exists(image_path):
    raise FileNotFoundError(f"❌ ERROR: Image file not found at {image_path}")

# Load the TIFF image using PIL
image = Image.open(image_path)

# Convert the image to a NumPy array
image_arr = np.array(image)

# Resize image for faster processing (optional)
image_resized = cv2.resize(image_arr, (1200, 800))

# 📌 2️⃣ Preprocess Image
gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Reduce noise
dilated = cv2.dilate(blur, np.ones((3, 3)))  # Enhance objects
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)  # Close gaps

# Apply additional preprocessing steps
edges = cv2.Canny(closing, 50, 150)  # Edge detection
closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)  # Close gaps again

# Show preprocessed image
cv2.imshow("Preprocessed Image", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 📌 3️⃣ Load Haar Cascade Model
car_cascade_src = r"D:\ArcGIS\GEO_215\GEO_215_Assignment_3\cars.xml"  # Update with correct path
if not os.path.exists(car_cascade_src):
    # Download the cars.xml file if it does not exist
    url = 'https://github.com/andrewssobral/vehicle_detection_haarcascades/raw/master/cars.xml'
    if not download_cars_xml(url, car_cascade_src):
        raise FileNotFoundError(f"❌ ERROR: Haar Cascade XML file not found at {car_cascade_src} and failed to download")

car_cascade = cv2.CascadeClassifier(car_cascade_src)

# Verify if classifier loaded
if car_cascade.empty():
    raise SystemError("❌ ERROR: OpenCV failed to load 'cars.xml'. Check the file.")

print("✅ Success: 'cars.xml' loaded correctly!")

# 📌 4️⃣ Detect Vehicles
cars = car_cascade.detectMultiScale(closing, scaleFactor=1.05, minNeighbors=3, minSize=(30, 30))

# Draw bounding boxes
detected_vehicles = []
cnt = 0
for (x, y, w, h) in cars:
    cv2.rectangle(image_resized, (x, y), (x + w, y + h), (255, 0, 0), 2)
    detected_vehicles.append([x, y, w, h])
    cnt += 1

print(f"✅ {cnt} vehicles detected")

# 📌 5️⃣ Show Detected Vehicles
cv2.imshow("Detected Vehicles", image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 📌 6️⃣ Save Results as CSV for ArcGIS Pro
if detected_vehicles:
    df = pd.DataFrame(detected_vehicles, columns=["X", "Y", "Width", "Height"])
    csv_output = r"D:\ArcGIS\GEO_215\GEO_215_Assignment_3\detected_vehicles.csv"
    df.to_csv(csv_output, index=False)
    print(f"✅ Detection results saved as {csv_output}")
else:
    print("⚠️ No vehicles detected.")