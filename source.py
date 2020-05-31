import optparse
from PIL import Image
from numpy import array

parser = optparse.OptionParser()

parser.add_option('--file', action = "store", dest = "file", help = "file path") # Set file path to image
parser.add_option('--height', action = "store", dest = "height", help = "height", default = 40) # Set height of image from parser, defaults to 40
parser.add_option('--width', action = "store", dest = "width", help = "width", default = 40) # Set width of image from parser, defaults to 40
options, args = parser.parse_args()
FILE = options.file # Insert path to image

size = (int(options.height), int(options.width)) # Size of image 

matrix = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

factor = 255 / len(matrix)

img = Image.open(FILE)
img = img.resize(size)
arr = array(img) # Stores pixel data [R, G, B]
averaged_arr = [] # Stores averaged values of each pixel
ascii_arr = [] # Stores ASCII art

def average(pixel):
    return (pixel[0] + pixel[1] + pixel[2]) / 3

for i in range(len(arr)):
    for j in range(len(arr[0])):
        pixel = arr[i][j]
        averaged_arr.append(average(pixel))

for i in range(len(averaged_arr)):
    ascii_arr.append(matrix[int(averaged_arr[i] / factor)])

for i in range(size[0]):
    for j in range(size[1]):
        print(ascii_arr[i * size[0] + j], end = " ")
    print(' ')