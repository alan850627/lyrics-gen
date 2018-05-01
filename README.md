# Scraper
```Bash
python gather.py --output_file hillsong.txt --artists "17018, 137438971086"
```

# Preprocess
* Manually remove tags i.e. [chorus] and (verse)
```Bash
python preprocess.py --input_file hillsong.txt
```

# Train
```Bash
python train.py --training_file hillsong.txt --vocabulary_file hillsong.vocab --model_name lstm_regression_model
```

# Sample
```Bash
python sample.py --model_name lstm_regression_model --vocabulary_file hillsong.vocab --output_file sample.txt