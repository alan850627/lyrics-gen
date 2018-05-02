# Scraper
```Bash
python gather.py --output_file worship.txt --artists "8589948384, 7077, 16817, 17018, 137438971086"
```

# Preprocess
* Manually remove tags i.e. [chorus] and (verse)
```Bash
python tolower.py --input_file worship.txt
python preprocess.py --input_file worship_lower.txt
```

# Train
```Bash
python train.py --training_file worship_lower.txt --vocabulary_file worship_lower.vocab --model_name lstm_regression_model
```

# Sample
```Bash
python sample.py --model_name lstm_regression_model --vocabulary_file worship_lower.vocab --output_file sample.txt
```

# Markov
```
python onegram.py --training_file scraped/worship.txt
```