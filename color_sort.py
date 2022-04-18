from PIL import Image
import numpy as np  
  
def blue(img):
  blue = {}
  hsv = img.convert('HSV')
  hsv = np.array(hsv)
  sensitivity = 15
  for x in range(len(hsv[:,0])):
    for y in range(len(hsv[0, :])):
      if 221 < hsv[x,y][0] < 240 and sensitivity < hsv[x,y][1] < 255-sensitivity and sensitivity < hsv[x,y][2] < 255 - sensitivity:
        blue[(x,y)] = hsv[x,y]
  return blue

def yellow(img):
  yellow = {}
  hsv = img.convert('HSV')
  hsv = np.array(hsv)
  sensitivity = 15
  for x in range(len(hsv[:,0])):
    for y in range(len(hsv[0, :])):
      if 51 < hsv[x,y][0] < 60 and sensitivity < hsv[x,y][1] < 255-sensitivity and sensitivity < hsv[x,y][2] < 255 - sensitivity:
        yellow[(x,y)] = hsv[x,y]
  return yellow

def white(img):
  white = {}
  hsv = img.convert('HSV')
  hsv = np.array(hsv)
  sensitivity = 15
  for x in range(len(hsv[:,0])):
    for y in range(len(hsv[0, :])):
      if 0 < hsv[x,y][1] < sensitivity and 255 - sensitivity < hsv[x,y][2] < 255:
        white[(x,y)] = hsv[x,y]
  return white

def isblue(pixel, image):
  if pixel in blue(image):
    return True

def isyellow(pixel, image):
  if pixel in yellow(image):
    return True

def iswhite(pixel, image):
  if pixel in white(image):
    return True

def points(img):
  listpts = []
  px = img.load()
  step = 2
  for x in range(0, img.width, step):
    for y in range(0, img.height, step):
      if isblue((x,y), img) or isyellow((x,y), img) or iswhite((x,y), img):
        listpts.append((px[x,y][0], px[x,y][1], px[x,y][2], x, y))
  return listpts