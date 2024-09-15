# Sudoku Solver
A Python-based sudoku solver that processes sudoku puzzle images and solves it using OpenCV and Py Sudoku. This is an extension of the document scanner project in my repository.

## Features
- Scans all images in a folder.
- Detects sudoku puzzles within images.
- Saves processed results in a results folder.
- Utilizes OpenCV for image processing.
- Utilizes PySudoku to solve the sudoku puzzles.
- Utilizes tensorflow to train the model for digit recognition.

## Set Up
### Clone the Repository

```bash
git clone https://github.com/your-username/Sudoku-Solver.git
cd Sudoku-Solver
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
python solve_sudoku.py
```

The script will:
 - Read all images from the images folder.
 - Process each image to detect the sudoku puzzle.
 - Save the solved images to the results folder with the same name.

Ensure that you have images in the images folder, and you will find the results in the results folder.
