import os
import random

filepath = '.\\time_series\\Time_normalized_stages\\1_unprocessed\\'
files = os.listdir(filepath)

test_examples = random.sample(files, 93)

with open("test_examples.txt", "w") as test:
    for example in test_examples:
        # test.write(example)
        # test.write("\n")

with open("training_examples.txt", "w") as train:
    for file in files:
        if (file not in test_examples):
            # train.write(file)
            # train.write("\n")
