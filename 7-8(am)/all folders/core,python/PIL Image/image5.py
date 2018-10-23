from PIL import Image as im
img =im.open(r'C:\Users\Azeem\Desktop\ismail.jpg')
print(img)
name =input('enter a file name with format:')
img.save(name)
print('new Image created')