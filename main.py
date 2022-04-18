# yena chang MI1
# vincent villiaumey LDDIM1
# projet 2 isd
import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from scipy import signal
import seaborn as sns

images = load_images(media, "*.png")
image_grid(images)