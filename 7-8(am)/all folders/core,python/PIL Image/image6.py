from PIL import Image as im
img =im.open(r'C:\Users\Azeem\Desktop\download.jpg').convert('L')
img.show()