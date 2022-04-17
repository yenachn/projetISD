
#color filter
def colored(color, img):
  for pxl in img:
    

#pixels to points
def pxltopts(img):
  listpts = []
  px = img.load()
  #modify step size based on image res
  for x in range(0, img.width, 2):
    for y in range(0, img.height, 2):
      if ():
        listpts.append((px[x,y][0], px[x,y][1], px[x,y][2], x, y))
  return listpts