#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
# Tutorial 1: Drawing with the SimpleGraphics Library. (2016-09-19). Retrieved from https://culearn.carleton.ca/moodle/pluginfile.php/1832043/mod_resource/content/1/COMP1405-F16-XXX-XX-%28Simple%20Graphics%20Tutorial%20-%20Part%201%20of%202%29.pdf.
# Tutorial 2: Using Images with the SimpleGraphics Library. (2016-09-19). Retrieved from https://culearn.carleton.ca/moodle/pluginfile.php/1832053/mod_resource/content/1/COMP1405-F16-XXX-XX-%28Simple%20Graphics%20Tutorial%20-%20Part%202%20of%202%29.pdf.
#

from SimpleGraphics import *

# Load original image
orig_img = loadImage("bubbles.gif")

# Retrieve width and height of original image
orig_img_width  = getWidth(orig_img)
orig_img_height = getHeight(orig_img)

# Create a new image with the same width and length of the original image
new_img = createImage(orig_img_width, orig_img_height)

# Create the negative image
for x in range(orig_img_width):
	for y in range(orig_img_height):
		r, g, b = getPixel(orig_img, x, y)
		putPixel(new_img, x, y, 255-r, 255-g, 255-b)

# Draw the new image
drawImage(new_img, 0, 0)