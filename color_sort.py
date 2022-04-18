from PIL import Image
from scipy.ndimage import gaussian_filter
import numpy as np

def colored(color, img):
  hsv = img.convert('HSV')
  hsv = np.array(hsv)
  


def partitionbycolor(color, img):
  partitioned = {}
  partitioned[blue] = colored(blue, img)
  partitioned[yellow] = colored(yellow, img)
  partitioned[white] = colored(white, img)
  return partitioned

