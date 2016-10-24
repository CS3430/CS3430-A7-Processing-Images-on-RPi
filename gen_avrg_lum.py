import argparse
import cv2
import fnmatch
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument('-id', '--idir', required = True, help = 'Path to image')
args = vars(ap.parse_args())

## a function you may want to use in debugging
def display_image_pix(image, h, w):
    image_pix = list(image)
    for r in xrange(h):
        for c in xrange(w):
            print list(image_pix[r][c]), ' ',
        print


## luminosity conversion
def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]


## This function takes a path to an image and computes the average luminosity of the image by computing
## the sum of the pixel luminosities and dividing it by the number of pixels.
def compute_avrg_luminosity(imagepath):
    image = cv2.imread(imagepath)
    (rows, cols, num_channels) = image.shape
    totalLum = 0;
    for r in xrange(rows):
        for c in xrange(cols):
            totalLum += luminosity(image[r,c])
    return totalLum/(r*c)


# This generator takes an directory where images are stored and a regular
# expression that specifies which images should be processed and yields 2-tuples
# of image filenames that match the pattern and their average luminosities.
def gen_avrg_lumin_for_dir(imgdir, filepat=r'*.png'):
    fns = generate_file_names(filepat, imgdir)
    for f in fns:
        yield (f, compute_avrg_luminosity(f))


def generate_file_names(fnpat, rootdir):
  for path, dirlist, filelist in os.walk(rootdir):
    for file_name in fnmatch.filter(filelist, fnpat):
        yield os.path.join(path, file_name)


## run ghe generator and output into STDOUT           
for fp, lum_avrg in gen_avrg_lumin_for_dir(args['idir'], r'*.png'):
    sys.stdout.write(fp + '\t'  + str(lum_avrg) + '\n')
    sys.stdout.flush()
