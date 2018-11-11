# -*- coding: utf-8 -*-
"""
Spyder Editor

This file slices the image in the qtd desired
"""

import os, glob
import image_slicer

# ORIGINAL JPEG
local_files = os.getcwd()
source = local_files + "/PQR/originals/JPEGImages"
target = local_files + "/PQR/dataset/JPEGImages"
fyletipe = "jpg"
qtd = 9

dire = os.listdir(target)
for arq in dire:
    arq = target + "/" +  arq
    os.remove(arq)

os.chdir(source)
for file in glob.glob("*."+fyletipe):
	tiles = image_slicer.slice(file, qtd, save=False)
	image_slicer.save_tiles(tiles, directory=target, prefix=file[:-4], format=fyletipe)

# SEGMENTED PNG
source = local_files + "/PQR/originals/SegmentationClass"
target = local_files + "/PQR/dataset/SegmentationClass"
fyletipe = "png"

dire = os.listdir(target)
for arq in dire:
    arq = target + "/" +  arq
    os.remove(arq)

os.chdir(source)
for file in glob.glob("*."+fyletipe):
	tiles = image_slicer.slice(file, qtd, save=False)
	image_slicer.save_tiles(tiles, directory=target, prefix=file[:-4], format=fyletipe)

# CREATE SETS
imageset = local_files + "/PQR/dataset/ImageSets"
os.chdir(imageset)
open("trainval.txt", "w").close
trainval = open("trainval.txt", 'a')

os.chdir(target)
for file in glob.glob("*."+fyletipe):
	trainval.write(file[:-4]+"\n")

trainval.close()

os.chdir(imageset)
trainval = open("trainval.txt", 'r')
open("train.txt", "w").close
train = open("train.txt", 'a')
open("val.txt", "w").close
val = open("val.txt", 'a')

cont = 0
trainval_lines = trainval.readlines()
for line in trainval_lines:
	cont = cont + 1
	if not cont%10: #10% used for tests
		val.write(line)
	else:
		train.write(line)

train.close()
val.close()
trainval.close()

# REWRITE PROPORTION OF FILES IN SEGMENTATION_DATASET.PY
def change_line(path,index_linha,nova_linha):
    with open(path,'r') as f:
        texto=f.readlines()
    with open(path,'w') as f:
        for i in texto:
            if texto.index(i)==index_linha:
                f.write(nova_linha+'\n')
            else:
                f.write(i)

os.chdir(local_files)
seg_dataset = local_files+"/segmentation_dataset.py"
train_str = "        'train': " + str(cont - int(cont/10)) + ","
change_line(seg_dataset, 31, train_str)
trainval_str = "        'trainval': " + str(cont) + ","
change_line(seg_dataset, 32, trainval_str)
val_str = "        'val': " + str(int(cont/10)) + ","
change_line(seg_dataset, 33, val_str)






















