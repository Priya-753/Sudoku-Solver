# import the necessary packages
from sudokusolver.Sudoku.puzzle import extract_digit
from sudokusolver.Sudoku.puzzle import find_puzzle
from tensorflow.keras.preprocessing.image import img_to_array
from sudoku import Sudoku
import numpy as np
import argparse
import imutils
import cv2
from utils import load_image, save_image


def solve_sudoku_with_model(model, image_path, image_name):
	print("[INFO] processing image...")
	image = load_image(image_path)
	orig = image.copy()
	image = imutils.resize(image, width=600)

	(puzzleImage, warped) = find_puzzle(image, debug=False)

	board = np.zeros((9, 9), dtype="int")

	stepX = warped.shape[1] // 9
	stepY = warped.shape[0] // 9

	cellLocs = []

	for y in range(0, 9):
		row = []
		for x in range(0, 9):
			startX = x * stepX
			startY = y * stepY
			endX = (x + 1) * stepX
			endY = (y + 1) * stepY

			row.append((startX, startY, endX, endY))
			
			cell = warped[startY:endY, startX:endX]
			digit = extract_digit(cell, debug=False)

			if digit is not None:
				roi = cv2.resize(digit, (28, 28))
				roi = roi.astype("float") / 255.0
				roi = img_to_array(roi)
				roi = np.expand_dims(roi, axis=0)
				pred = model.predict(roi).argmax(axis=1)[0]
				board[y, x] = pred
		
		cellLocs.append(row)

	# construct a Sudoku puzzle from the board
	print("[INFO] OCR'd Sudoku board:")
	puzzle = Sudoku(3, 3, board=board.tolist())
	puzzle.show()
	# solve the Sudoku puzzle
	print("[INFO] solving Sudoku puzzle...")
	solution = puzzle.solve()
	solution.show_full()

	ys = 0
	for (cellRow, boardRow) in zip(cellLocs, solution.board):
		xs = 0
		for (box, digit) in zip(cellRow, boardRow):
			if not board[ys][xs]:
				startX, startY, endX, endY = box
				
				textX = int((endX - startX) * 0.33)
				textY = int((endY - startY) * -0.2)
				textX += startX
				textY += endY
				# draw the result digit on the Sudoku puzzle image
				cv2.putText(puzzleImage, str(digit), (textX, textY),
					cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)
				
			xs = xs + 1
		ys = ys + 1
	# show the output image
	folder_name = 'results/' + image_name.split(".")[0]
	save_image(folder_name, '1_original_image.jpg', orig)
	save_image(folder_name, '1_solved_image.jpg', puzzleImage)