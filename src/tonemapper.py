from PIL import Image
from sys import argv
import util

IM_MODE = "RGB"

# check for same sizes in source images
# return an array of sources and a blank image of the same size
def import_source_data(folder_name):
    im_arr = []
    first_iteration = True
    for filename in util.loop_files(folder_name):
        im_source = Image.open(filename)
        im_arr.append(im_source)
        if first_iteration:
            first_iteration = False
            im_size = im_source.size
        else:
            if im_source.size != im_size:
                print("Source image sizes do not match")
                exit()
    return im_arr, Image.new(IM_MODE, im_size)

# import data and create a blank canvas
folder_name = argv[1]
sources, im = import_source_data(folder_name)
im_size_x, im_size_y = im.size

for x in range(im_size_x):
    for y in range(im_size_y):
        r = 0
        g = 0
        b = 0
        for source in sources:
            # sum the values of the sources
            source_rgb = source.getpixel((x,y)) 
            r += source_rgb[0]
            g += source_rgb[1]
            b += source_rgb[2]

        # map the summed values to [0,255]
        r = int(r/len(sources))
        g = int(g/len(sources))
        b = int(b/len(sources))
        im.putpixel((x,y), (r,g,b))

im.save(folder_name + "output.png")
