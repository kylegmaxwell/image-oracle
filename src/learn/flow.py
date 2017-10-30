# Adapted from https://www.tensorflow.org/get_started/estimator

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import os
import shutil

N_CLASSES = 2
TMP_DIR = "C:\\tmp\\image_model"
OUT_FILE = "data/results.txt"

# Run tensorflow to predict image categories
# @param trainPath Path to the training data as csv
# @param testPath Path to the test data as csv
# @param steps Number of training iterations
def flow(trainPath, testPath, steps):
  print("flow")
  nColumns = getColumnsFromFile(trainPath)

  if os.path.exists(TMP_DIR):
    shutil.rmtree(TMP_DIR)

  # Load datasets.
  training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=trainPath,
      target_dtype=np.int,
      features_dtype=np.float32)
  test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=testPath,
      target_dtype=np.int,
      features_dtype=np.float32)

  # Specify that all features have real-value data
  feature_columns = [tf.feature_column.numeric_column("x", shape=[nColumns])]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=N_CLASSES,
                                          model_dir=TMP_DIR)
  # Define the training inputs
  train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(training_set.data)},
      y=np.array(training_set.target),
      num_epochs=None,
      shuffle=True)

  # Train model.
  print('Training...')
  classifier.train(input_fn=train_input_fn, steps=steps)

  # Define the test inputs
  test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(test_set.data)},
      y=np.array(test_set.target),
      num_epochs=1,
      shuffle=False)

  # Write results to a file
  print(f"Write file {OUT_FILE}")
  f = open(OUT_FILE, 'w')

  # Evaluate accuracy.
  prediction = classifier.evaluate(input_fn=test_input_fn)

  f.write(f"Prediction accuracy: {int(100*prediction['accuracy'])}%\n")


  f.write(f"Target      [{', '.join([str(x) for x in test_set.target])}]\n")

  predictions = list(classifier.predict(input_fn=test_input_fn))
  predicted_classes = [p["classes"] for p in predictions]

  f.write(f"Predictions {list([int(c[0]) for c in predicted_classes])}\n")

  # Predict the zero vector to see how it would handle unrecognized images
  new_samples = np.array(
      [list(range(0,nColumns))], dtype=np.float32)
  predict_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": new_samples},
      num_epochs=1,
      shuffle=False)

  predictions = list(classifier.predict(input_fn=predict_input_fn))
  predicted_classes = [p["classes"] for p in predictions]
  f.write(f"Zero Prediction {list([int(c[0]) for c in predicted_classes])}\n")

  print("done")

def getColumnsFromFile(path):
    f = open(path, 'r')
    chunks = f.readline().split(",")
    print(f"Number of columns {chunks[1]}")
    return int(chunks[1])