import os
import cv2

def load_image(path: str):
    """
    Args:
        path: string representing a file path to an image

    """
    img = cv2.imread(path)
    print(path)
    return img


def save_image(path: str, image_name: str, image) -> None:
    """
    Args:
        path: string representing a file path to an image
        image_name: the name of the image to be saved
        image: the image to be saved
    """
    base_path = os.path.split(path)[0]
    os.chdir(base_path)
    folder_path = os.path.split(path)[1]
    if not os.path.exists(folder_path):
        print("Path doesn't exist so creating one")
        os.makedirs(folder_path)
    
    os.chdir("../")

    new_image_path = os.path.join(path, image_name)
    print(new_image_path)
    if image is None:
        print("Error: Image data is empty.")
    else:
        success = cv2.imwrite(new_image_path, image)
        if not success:
            print("Error: Failed to save the image.")