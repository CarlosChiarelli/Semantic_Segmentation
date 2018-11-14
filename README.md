# Image Segmentation
Image Segmentation with [DeeplabV3+](https://github.com/tensorflow/models/tree/master/research/deeplab), adapted to use on own dataset.

## Pre-trained models
Download the folders from [Google Drive](https://drive.google.com/open?id=1qI1rcNNobAJvHIVXXWHr6NYUthwEasz3)

Copy and paste the Segmentador and xception_65 folders at the path: 
research/deeplab/datasets/PQR/exp/train_on_trainval_set/init_models/

## Adapt to train on own dataset
The following files must be adapted to train on your own dataset.

#### research/deeplab/train-pqr.sh
This bash file calls train.py, with the paths to the directories needed.

--training_number_of_steps is used to inform the amount of steps to run.

--train_bath_size informs the amount of steps evaluated before update the weights of the network.

--initialize_last_layer must be true when the model will be incremented, must be false when the model will be trained without previous chekpoints.

--tf_initial_chekpoint define the path to the initial chekpoint used. If not defined your own, use xception_65 path.

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

## Evaluation and Visualization
