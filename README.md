# Image oracle
This is a computer vision and machine learning tool that will learn a class of images and then detect similar images, or not similar ones.

The learning is done in two steps, first the images are assigned labels that describe their contents. Then then labels are fed into a machine learning algorithm. The algorithm is gives images of the category to recognize and other images, and learns to recognize the "original" set. The other images are called "imposter" images.

The code is two chunks, one in JavaScript and the other in Python. The JavaScript code uses the Google Cloud Vision API to get the "labels" that describe the contents of the image. The result is stored as a JSON files next to the original images.

Then the Python code loads the JSON files and creates an index of all the labels. This index is used to create a numeric vector representation of the labels applied to each image. Then the vectors are fed into Tensorflow, along with the original or imposter value. The data is split into training and test data, and the values for the test data are used to test and evaluate the accuracy of the model.

# Prerequisites
These programs must be installed
* git - https://git-scm.com/downloads#
* yarn - https://yarnpkg.com/lang/en/docs/install/
* node - https://nodejs.org/en/download/
* python 3 - https://www.python.org/downloads/
* tensorflow - https://www.tensorflow.org/install/

# Set up
yarn install

# Run
yarn start

py3 src/learn/index.py

# Results
You will need to provide images in the data/imposter and data/original directories to serve as inputs (you can use the provided ones in data-sample). The images can be png or jpg. After running the program, the results can be found in data/results.txt. You can use the csv files in the same directory to look up what images the test data correspond to (test-index.csv) and what labels are used in the vectors (labels.csv).
