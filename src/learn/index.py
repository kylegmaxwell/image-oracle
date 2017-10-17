import vectorize
import os
import flow

def main():
    print("hello")

    # Data sets
    IMAGE_TRAINING = "./data/train.csv"
    IMAGE_TEST = "./data/test.csv"

    # If the training and test sets aren't stored locally, calculate them.
    if not os.path.exists(IMAGE_TRAINING) or not os.path.exists(IMAGE_TEST):
        print('vectorize')
        vectorize.vectorize(IMAGE_TRAINING, IMAGE_TEST);

    flow.flow(IMAGE_TRAINING, IMAGE_TEST)

print(__name__)
if __name__ == "__main__":
    main()