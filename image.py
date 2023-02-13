from PIL import Image

img = Image.open("example.jpg")

img.save("compressed_example.jpg", quality=20)
