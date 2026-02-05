# -- Practical => Image Manipulation With Pillow --

from PIL import Image  # this is buge in vscode


openImage = Image.open(r'c:\Users\almostkbal\Desktop\Python\pubge.webp')

openImage.show()


# My Cropped Image
imageSize = (300, 300, 800, 800)
myNewImage = openImage.crop(imageSize)

# Show The New Image
myNewImage.show()

# My Converted Mode Image
myConverted = openImage.convert("L")
myConverted.show()