from solve_sudoku_puzzle import solve_sudoku_with_model
import os
import cv2
from tensorflow.keras.models import load_model

def load_images_and_process(folder_path):
    print("[INFO] loading digit classifier...")
    model = load_model("output/digit_classifier.keras")


    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]

    for image_file in image_files:
        # Build full path to the image
        image_path = os.path.join(folder_path, image_file)
        
        # Load the image using OpenCV
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"Failed to load image: {image_path}")
            continue
        
        print(f"Processing image: {image_file}")
        
        # Call your document_scan method to process the image
        solve_sudoku_with_model(model, image_path, image_file)

# Folder containing the images
image_folder = 'images'

# Load images and process them one by one
load_images_and_process(image_folder)