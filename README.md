# Image Segmentation
I created this repository to simplify the adaptation of Image Segmentation with [DeeplabV3+](https://github.com/tensorflow/models/tree/master/research/deeplab), to use on own dataset.

## Pre-trained models
Download the folders from [Google Drive](https://drive.google.com/open?id=1qI1rcNNobAJvHIVXXWHr6NYUthwEasz3)

Copy and paste the Segmentador and xception_65 folders at the path: 
research/deeplab/datasets/PQR/exp/train\_on\_trainval\_set/init_models/

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
-from \_\_future\_\_ import absolute_import, division, print_function

## Adapt to train on own dataset
The following files must be adapted to train on your own dataset.

#### research/deeplab/train-pqr.sh
This bash file calls train.py, with the paths to the directories needed.

--training\_number\_of\_steps is used to inform the amount of steps to run.

--train\_bath\_size informs the amount of steps evaluated before update the weights of the network.

--train_split informs wich split will be used during the training, choose between train, trainval or val.

--initialize\_last\_layer must be true when the model will be incremented (by the initial chekpoint or the already trained at  research/deeplab/datasets/PQR/exp/train_on_trainval_set/train/), must be false when the model will be trained by the first time or if you want to reset the weights.

--tf\_initial\_chekpoint define the path to the initial chekpoint used. If not defined your own, use xception_65 path. To use your own chekpoint, place your chekpoint files at Segmentador path and set --tf\_initial\_chekpoint as the Segmentador path.

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
Try to delete every \_\_pycache\_\_ directory existent and run the code again.

## Evaluation and Visualization
To evaluate or test new images on your trained model, the chekpoints need to be on research/deeplab/datasets/PQR/exp/train_on_trainval_set/train/ directory.

#### Evaluation
Edit the file eval-pqr.sh at research/deeplab/. Choose the --eval_split between val, train or trainval.  
The --eval_crop_size must be the size of the greater image in the dataset. The first measure refers to hight and the second refers to width.  
Keep the rest as it is.

It will create a file at research/deeplab/datasets/PQR/exp/train_on_trainval_set/eval/ and will show the mIoU (mean intersection over union) of the model.

#### Visualization
Edit the file vis-pqr.sh at research/deeplab/. Choose the --vis_split between val, train or trainval.
The --eval_crop_size must be the size of the greater image in the dataset. The first measure refers to hight and the second refers to width.  
Keep the rest as it is.

It will put the original and segmented results based on the split defined (val, train or trainval) at  research/deeplab/datasets/PQR/exp/train_on_trainval_set/vis/segmentation_results/ .
