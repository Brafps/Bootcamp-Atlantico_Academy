import cv2
import os
import random
import cv2
import skimage
import matplotlib.pyplot as plt
import numpy as np
import tolerance as tolerance
from skimage import segmentation


from src.utils.utl import load_random_img, show_img, load_img, escrever
from vc import histograma, cut_img

#(nome , img, tipo) = load_random_img()
(nome , img, tipo) = load_img("08540")




img = cut_img(img)
original = img

lista = []
for i in range(9):
  lista.append(img[46 + i, 50])
  lista.append(img[50, 46 + i])
tom_de_cinza = max(lista)
print(lista)



print(img[50, 50])
img = cv2.GaussianBlur(img, (3,3), 0)
print(img[50, 50])
img = segmentation.flood_fill(img, (50, 50), 255, tolerance = 10)
print(img[50, 50])
img = cv2.threshold(img, 254, tom_de_cinza, cv2.THRESH_TOZERO)[1]



img_modified = img.copy()
original_img = img


for i, key_i in enumerate(img):
  for j,key_j in enumerate(img[i]):

    if key_j > 254:
      img_modified[i][j] = original_img[i][j]
    else:
      img_modified[i][j] = img[i][j]

# Passando a mascara
img_mask = cv2.bitwise_and(original, original, mask = img_modified)


escrever(img_mask, "Segmentada")
escrever(original, "Original")

#imagem = img_mask
imagem = np.hstack([original, img_mask])

show_img(f"Tumor {nome}, {tipo}", imagem)

