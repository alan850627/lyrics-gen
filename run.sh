#!/bin/bash

python preprocess.py --input_file scraped/children.txt
mkdir scraped/children-samples
python train.py --training_file scraped/children.txt --vocabulary_file scraped/children.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model

python preprocess.py --input_file scraped/worship.txt
mkdir scraped/worship-samples
python train.py --training_file scraped/worship.txt --vocabulary_file scraped/worship.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model
