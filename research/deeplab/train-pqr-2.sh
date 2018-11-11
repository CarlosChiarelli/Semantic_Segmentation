#!/bin/bash
cd ..
# Set up the working environment.
CURRENT_DIR=$(pwd)
SLIM_DIR="${CURRENT_DIR}/slim"
WORK_DIR="${CURRENT_DIR}/deeplab"
DATASET_DIR="datasets"

export PYTHONPATH="$PYTHONPATH:${SLIM_DIR}"
export PYTHONPATH="$PYTHONPATH:${WORK_DIR}"

# Set up the working directories.
PQR_FOLDER="PQR"
EXP_FOLDER="exp/train_on_trainval_set"
INIT_FOLDER="${WORK_DIR}/${DATASET_DIR}/${PQR_FOLDER}/${EXP_FOLDER}/init_models"
TRAIN_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${PQR_FOLDER}/${EXP_FOLDER}/train"
DATASET="${WORK_DIR}/${DATASET_DIR}/${PQR_FOLDER}/tfrecord"

mkdir -p "${WORK_DIR}/${DATASET_DIR}/${PQR_FOLDER}/exp"
mkdir -p "${TRAIN_LOGDIR}"

python "${WORK_DIR}"/train.py \
  --logtostderr \
  --training_number_of_steps=2000 \
  --train_batch_size=1 \
  --train_split="train" \
  --model_variant="xception_65" \
  --atrous_rates=12 \
  --atrous_rates=24 \
  --atrous_rates=36 \
  --output_stride=8 \
  --decoder_output_stride=4 \
  --train_crop_size=321 \
  --train_crop_size=321 \
  --dataset="pqr" \
  --train_logdir="${TRAIN_LOGDIR}" \
  --dataset_dir="${DATASET}" \
  --tf_initial_checkpoint="${INIT_FOLDER}/Segmentador/model.ckpt" \
  --fine_tune_batch_norm=false \
  --initialize_last_layer=true \
  --last_layers_contain_logits_only=true
