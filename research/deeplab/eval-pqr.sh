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
TRAIN_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${PQR_FOLDER}/${EXP_FOLDER}/train"
EVAL_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${PQR_FOLDER}/${EXP_FOLDER}/eval"
DATASET="${WORK_DIR}/${DATASET_DIR}/${PQR_FOLDER}/tfrecord"

python "${WORK_DIR}"/eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --eval_crop_size=1040 \
    --eval_crop_size=1377 \
    --dataset="pqr" \
    --checkpoint_dir="${TRAIN_LOGDIR}" \
    --eval_logdir="${EVAL_LOGDIR}" \
    --dataset_dir="${DATASET}"
