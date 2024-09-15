import numpy as np
import cv2

def order_points(pts):
    # pts is a set of 4 points given. With these points we have to 
    # figure the respective corners of a rectangle. 
    # The name of the points do not matter but they must maintain 
    # a consistnet order. 
    # Lets try to go with top left, top right, bottom right and bottom left
    rect = np.zeros((4,2), dtype="float32")

    # We find sum in every row, so the sum of x + y for every point. The lowest sum must be diagnol to the highest sum
    # We then find the diff in every row, so x - y for every point. The lowest diff be diagnol to the highest diff

    sums = pts.sum(axis=1)
    diff = np.diff(pts, axis = 1)

    # Points at 0 and 2 will be diagonal
    rect[0] = pts[np.argmin(sums)]
    rect[2] = pts[np.argmax(sums)]

    # Points at 1 and 3 will be diagonal
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def four_point_transform(image, pts):
    # We have 4 points, we return the transform
    rect = order_points(pts)
    (tl, tr, bl, br) = rect

    width1 = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
    width2 = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
    max_width = max(int(width1), int(width2))

    height1 = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    height2 = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    max_height = max(int(height1), int(height2))

    dst = np.array([[0, 0], [max_width - 1, 0], [max_width - 1, max_height - 1], [0, max_height - 1]], dtype = "float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (max_width, max_height))

	# return the warped image
    return warped













