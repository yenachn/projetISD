# yena chang MI1
# vincent villiaumey LDDIM1
# projet 2 isd
import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from scipy import signal
import seaborn as sns
from color_sort import *
from clusters import*
from envelopes import *

img = Image.open("media/a01.png")

print(points(img))