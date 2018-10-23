f= open("sample.txt")      # By default the mode is read mode  and no need to specify the mode also.
val=f.read()
print(val)
f.close()
print("File is closed")