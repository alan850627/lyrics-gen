#!/bin/bash

python preprocess.py --input_file scraped/latin.txt
mkdir scraped/latin-samples
python train.py --training_file scraped/latin.txt --vocabulary_file scraped/latin.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model

python preprocess.py --input_file scraped/rap.txt
mkdir scraped/rap-samples
python train.py --training_file scraped/rap.txt --vocabulary_file scraped/rap.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model

