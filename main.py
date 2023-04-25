import cv2
import imutils

class ShapeDetector:
    def __init__(self):
        pass
    def detect(self, c):
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.95 and ar <= 1.05:
                shape = "square"
            else:
                shape = "rectangle"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"

        return shape

image = cv2.imread("C:/Users/1/Desktop/IS_img/IS4_1.png")
cv2.imshow("Input", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

cnts = imutils.grab_contours(cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE))
output = image.copy()
sd = ShapeDetector()

amountCircle = 0
amountTriangle = 0
amountSquare = 0
amountRectangle = 0
amountPentagon = 0

for c in cnts:
    shape = sd.detect(c)

    if shape == "triangle":
        amountTriangle += 1
    elif shape == "square":
        amountSquare += 1
    elif shape == "rectangle":
        amountRectangle += 1
    elif shape == "pentagon":
        amountPentagon += 1
    elif shape == "circle":
        amountCircle += 1

    cv2.drawContours(output, [c], -1, (0, 0, 0), 1)

text = "Objects in the image: Triangle: {} Square: {} Rectangle: {} Pentagon: {} Circle: {}".format\
    (amountTriangle, amountSquare, amountRectangle, amountPentagon, amountCircle)
cv2.putText(output,text, (10, 25), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 0), 1)

cv2.imshow("Output", output)
print ("Objects in the image:")
print ("Triangle:", amountTriangle)
print ("Square:", amountSquare)
print ("Rectangle:", amountRectangle)
print ("Pentagon:", amountPentagon)
print ("Circle:", amountCircle)

cv2.waitKey(0)