from PIL import Image
from pytesseract import pytesseract

path = "/home/dom/.local/pytesseract"

imageName  = "Sudoku-with-start-squares.png"

image = Image.open(imageName)

pytesseract.tesseract_cmd = path

result = pytesseract.image_to_data(image)

print(result)