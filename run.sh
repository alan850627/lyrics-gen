#!/bin/bash

python preprocess.py --input_file scraped/country.txt
mkdir scraped/country-samples
python train.py --training_file scraped/country.txt --vocabulary_file scraped/country.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model

python preprocess.py --input_file scraped/jazz.txt
mkdir scraped/jazz-samples
python train.py --training_file scraped/jazz.txt --vocabulary_file scraped/jazz.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model

python preprocess.py --input_file scraped/latin.txt
mkdir scraped/latin-samples
python train.py --training_file scraped/latin.txt --vocabulary_file scraped/latin.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model

python preprocess.py --input_file scraped/rap.txt
mkdir scraped/rap-samples
python train.py --training_file scraped/rap.txt --vocabulary_file scraped/rap.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model

python preprocess.py --input_file scraped/children.txt
mkdir scraped/children-samples
python train.py --training_file scraped/children.txt --vocabulary_file scraped/children.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model

python preprocess.py --input_file scraped/worship.txt
mkdir scraped/worship-samples
python train.py --training_file scraped/worship.txt --vocabulary_file scraped/worship.vocab --model_name lstm_regression_model
rm -rf lstm_regression_model
