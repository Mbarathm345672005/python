from PIL import Image

img=Image.open("flip.jpg")
transpose_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transpose_img.save("new_img.jpg")
print("Done flipping")
