import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    _, frame = camera.read()

    #cv.imshow('Camera',frame)

    laplacian = cv.Laplacian(frame, cv.CV_64F) # using the laplacian function

    laplacian = np.uint8(laplacian) # converting the float to int and into the pizel range of 0-256
    #cv.imshow('Laplacian', laplacian)

    edges = cv.Canny(frame, 120, 120)
    # bascially the parameters in canny are the threshold if more detailing is required we can use
    # lower thresholds and less detailing then the higher thresholds.
    cv.imshow('Canny', edges)

    if cv.waitKey(5) == ord('x'):
        break


camera.release()
camera.destroyAllWindows()
