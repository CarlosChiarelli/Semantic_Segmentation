# Image Segmentation
I created this repository to simplify the adaptation of Image Segmentation with [DeeplabV3+](https://github.com/tensorflow/models/tree/master/research/deeplab), to use on own dataset.

## Pre-trained models
Download the folders from [Google Drive](https://drive.google.com/open?id=1qI1rcNNobAJvHIVXXWHr6NYUthwEasz3)

Copy and paste the Segmentador and xception_65 folders at the path: 
research/deeplab/datasets/PQR/exp/train_on_trainval_set/init_models/

## Dependencies
The algorithm makes use of the following imports, make sure that they are already installed:
-os.path
-contextlib
-functools
-PIL.Image
-os
-shutil
-glob
-image_slicer
-time
-numpy
-math
-six
-sys
-collections
-copy
-tensorflow
-from __future__ import absolute_import, division, print_function

## Adapt to train on own dataset
The following files must be adapted to train on your own dataset.

#### research/deeplab/train-pqr.sh
This bash file calls train.py, with the paths to the directories needed.

--training_number_of_steps is used to inform the amount of steps to run.

--train_bath_size informs the amount of steps evaluated before update the weights of the network.

--initialize_last_layer must be true when the model will be incremented (by the initial chekpoint or the already trained at  research/deeplab/datasets/PQR/exp/train_on_trainval_set/train/), must be false when the model will be trained by the first time or if you want to reset the weights.

--tf_initial_chekpoint define the path to the initial chekpoint used. If not defined your own, use xception_65 path. To use your own chekpoint, place your chekpoint files at Segmentador path and set --tf_initial_chekpoint as the Segmentador path.

Others parameters can be keeped as they are.

#### research/deeplab/datasets/slicer.py
To train on low memory PCs, edit the qtd value (line 16) to define the quantity of slices that each image will be partitioned.
If want to train without slicing, define qtd=1.

#### research/deeplab/datasets/segmentation_dataset.py
num_classes (line 36) must be the number of classes in your dataset.

ignore_labels (line 37) must be the grey scale value of the label not used (255 as default, it means that white can not be used as class label).

#### research/deeplab/datasets/label_pqr.py
Change the palette definition (line 8). The dictionary must be defined as (R, G, B) : LABEL, where R, G, B are the values of the label color of each class, and LABEL is a number from 0 to number of classes (the ignore_labels value must not be in the list).

#### Original and Segmented labeled Images (your dataset)
The original images must be in .jpg format, placed at research/deeplab/datasets/PQR/originals/JPEGImages

The labeled images must be in .png format, placed at research/deeplab/datasets/PQR/originals/SegmentationClass

## Training
#### Convert Images to Tensorflow format
Go to research/deeplab/datasets/ and run the "exec_pqr.sh".

It will split the original and labeled images and put them on respective folders at research/deeplab/datasets/PQR/dataset/. Also creating the respective sets of train, trainval and val at research/deeplab/datasets/PQR/dataset/ImageSets. By default it will use 10% of images for val and 90% for train.

After that, it will transform the segmented images, switching the colors by the respective label defined in the label_pqr.py palette, at research/deeplab/datasets/PQR/dataset/SegmentationClassRaw.

By the end, will convert the original jpg and the raw labeled images in tensor format, creating files for each set (train, trainval and val) at research/deeplab/datasets/PQR/tfrecord.

#### Train
Run the "train-pqr.sh" at research/deeplab/.

It will create the chekpoints at research/deeplab/datasets/PQR/exp/train_on_trainval_set/train/ that will be used as initial chekpoints in the next time you train your model. You can delete the files from that folder to start the training from 
research/deeplab/datasets/PQR/exp/train_on_trainval_set/init_models/ Segmentador or xception_65 chekpoints.

#### Common error
If you downloaded the repository, run everything in your own dataset, and then tried to copy and paste to other computer, 
you may have some trouble with paths. The most common problem are the pycache files created, that use the pre-defined paths.
Try to delete every __pycache__ directory existent and run the code again.

## Evaluation and Visualization
