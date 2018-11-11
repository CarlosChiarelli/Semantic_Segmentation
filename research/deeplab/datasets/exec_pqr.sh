#!/bin/bash
python slicer.py
python label_pqr.py
./convert_pqr.sh
