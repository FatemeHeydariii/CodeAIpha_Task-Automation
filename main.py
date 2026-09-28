import os
import shutil

# Source folder
source_folder = "photos"

# Destination folder
destination_folder = "jpg_files"


# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)


# Get all files in source folder
files = os.listdir(source_folder)

for file in files:

    if file.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")


print("All JPG files have been moved.")