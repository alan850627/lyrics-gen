# Scraper
```Bash
python gather.py --output_file worship.txt --artists "8589948384, 7077, 16817, 17018, 137438971086"
```

# Preprocess
* Manually remove tags i.e. [chorus] and (verse)
```Bash
python preprocess.py --input_file worship.txt
```

# Train
```Bash
python train.py --training_file worship.txt --vocabulary_file worship.vocab --model_name lstm_regression_model
```

# Sample
```Bash
python sample.py --model_name lstm_regression_model --vocabulary_file worship.vocab --output_file sample.txt
```