print(f'Hello world, exercise 3')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import PIL.Image

# Read Images
# img = mpimg.imread('stopsign.jpg') plt
img = PIL.Image.open("stopsign.jpg") # PIL

size = img.size

# 83 6 5
tMin = 70
tMax = 110
displayed = 0
for x in range(size[0]):
    for y in range(size[1]):
        if img.getpixel((x, y))[0] < tMin or img.getpixel((x, y))[0] > tMax or img.getpixel((x, y))[1] > 20 or img.getpixel((x, y))[2] > 10:
            img.putpixel((x, y), (0, 0, 0))
        else:
            img.putpixel((x, y), (255, 0, 0))
    percentage = 100*x/size[0]
    if displayed == 0 and percentage % 5 == 0:
        print("{:.0f}".format(percentage))
        displayed = 1
    displayed = 0


plt.imshow(img)
plt.show()
img.save('result.jpg')
print("done")

