import tensorflow as tf
from PIL import Image
import numpy as np

import os, shutil

# palette (color map) describes the (R, G, B): Label pair
palette = {(0,   0,   0) : 0 ,      # EXTERNO - PRETO
           (255,  0, 0) : 1,        # DEFEITOS - VERMELHO
           (0,  156, 222) : 2 ,     # NÃO USINADO - AZUL
           (255,  255, 0) : 3 ,     # USINADO - AMARELO
           (125,  125, 125) : 4     # ORIFÍCIOS - CINZA
          }

def convert_from_color_segmentation(arr_3d):
    arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)

    for c, i in palette.items():
        m = np.all(arr_3d == np.array(c).reshape(1, 1, 3), axis=2)
        arr_2d[m] = i
    return arr_2d

cur_dir = os.getcwd()
label_dir = cur_dir + '/PQR/dataset/SegmentationClass/'
new_label_dir = cur_dir + '/PQR/dataset/SegmentationClassRaw/'

if not os.path.isdir(new_label_dir):
	print("creating folder: ",new_label_dir)
	os.mkdir(new_label_dir)
else:
	print("Folder alread exists. Deleting files...")
	dire = os.listdir(new_label_dir)
	for arq in dire:
		arq = new_label_dir + arq
		os.remove(arq)

label_files = os.listdir(label_dir)

for l_f in label_files:
	arr = np.array(Image.open(label_dir + l_f))
	arr = arr[:,:,0:3]
	arr_2d = convert_from_color_segmentation(arr)
	Image.fromarray(arr_2d).save(new_label_dir + l_f)
