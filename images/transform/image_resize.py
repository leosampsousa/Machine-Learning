 # -*- coding: utf-8 -*-
 # project: ambiente-classification
 # course: Aprendizagem de Máquina
 # university: Universidade Federal do Ceará - UFC
 # authors (github): heldercostaa, leosampsousa, lucasprimo375


from PIL import Image
import os, sys

# -------------------- #

def resizeImage(file, input_dir, output_dir, size=(200,200)):
	outfile = os.path.splitext(file)[0]
	extension = os.path.splitext(file)[1]

	# if not on format .jpg, the image is not converted
	if (cmp(extension, ".jpg")):
		print('Cannot convert image: ' + outfile + '. Wrong format.')
		return

	# convert image
	try:
		im = Image.open(input_dir + file)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save(output_dir + outfile + extension, "JPEG")
		print (outfile + ' converted.')
	except IOError:
		print('Cannot convert image: ' + outfile)

# -------------------- #

input_dir = os.getcwd() + "/unresized/deserto/"
output_dir = os.getcwd() + "/resized/deserto/"

# create folder 'unresized' if not exists
if not os.path.exists(output_dir):
	os.mkdir(output_dir)

# resize each image on 'unresized' to 'resized'
for file in os.listdir(input_dir):
	resizeImage(file, input_dir, output_dir)