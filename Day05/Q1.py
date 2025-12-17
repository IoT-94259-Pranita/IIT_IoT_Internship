import math

radius = 5
area = math.pi * math.pow(radius, 2) 
print(f"The area of circle = {area}")

angle_degrees = 30
angle_radians = math.radians(angle_degrees) 
print(f"{angle_degrees} degrees is {angle_radians} radians")

math.sqrt(25)
print(f"sqrt={math.sqrt(25)}")

import os

# 1. Get and print the current working directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# 2. Create a new directory named 'test_folder'
folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Directory '{folder_name}' created.")

# 3. List all files and folders in the current directory
print("Contents of current directory:")
for item in os.listdir("."):
    print(f" - {item}")

# 4. Remove the directory (it must be empty)
os.rmdir(folder_name)
print(f"Directory '{folder_name}' removed.")

