# yena chang MI1
# vincent villiaumey LDDIM1
# projet 2 isd
import os, re
from glob import glob as ls
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sys import path
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from scipy import signal
import seaborn as sns; sns.set()
from color_sort import *
from clusters import*
from envelopes import *

# load tous les images

dataset_dir = 'media'
images = load_images(dataset_dir, "*.png")

# points(img) pour tous les images (c'est par boucle? paslu les tps)

# graph(points(img)) (pr chaque image, encore)

# clusters(graph) evident

# envelopes(clusters, graph) je repete

# reduction(envelopes) utile pour identifier la forme mais j'ai pas vraiment utilise ca en caracteristiques

# apres avec les fonctions de chara tu extrais les attributs et les met dans un csv
