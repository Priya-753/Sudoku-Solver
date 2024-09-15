# Document Scanner
A Python-based document scanner that processes images to detect and extract documents. This script leverages OpenCV to handle image processing tasks and generates results saved in a specified directory.

## Features
- Scans all images in a folder.
- Detects documents within images.
- Saves processed results in a designated folder.
- Utilizes OpenCV for image processing.

## Set Up
### Clone the Repository

```bash
git clone https://github.com/your-username/Document-Scanner.git
cd Document-Scanner
```

### Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
Make sure you have the latest versions of the required libraries. Install them using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Usage
### Prepare Your Folders

Place all images you want to process in a folder named images.
Ensure there is a folder named results where the processed images will be saved.

### Run the Script

Execute the script to process images:

```bash
python document_scanner.py
```

The script will:
 - Read all images from the images folder.
 - Process each image to detect and extract documents.
 - Save the processed images to the results folder with the same name.

### Script Overview
The main script document_scanner.py performs the following steps:

- Load Images: Reads images from the images folder.
- Process Images: Applies document scanning techniques to detect and extract documents.
- Save Results: Saves the processed images in the results folder.

Ensure that you have images in the images folder, and you will find the results in the results folder.

Contributing
Feel free to open issues or submit pull requests if you have improvements or fixes. Contributions are welcome!
