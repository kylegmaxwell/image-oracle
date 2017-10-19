import vectorize
import os
import flow

def main():
    print("hello")

    # Data sets
    IMAGE_TRAINING = "./data/train"
    IMAGE_TEST = "./data/test"
    # Labels must appear this many times to be counted
    MIN_COUNT = 7
    # Training steps
    STEPS = 2000

    # If the training and test sets aren't stored locally, calculate them.
    # if not os.path.exists(IMAGE_TRAINING) or not os.path.exists(IMAGE_TEST):
    print('vectorize')
    vectorize.vectorize(IMAGE_TRAINING, IMAGE_TEST, MIN_COUNT);

    flow.flow(f"{IMAGE_TRAINING}.csv", f"{IMAGE_TEST}.csv",STEPS)

print(__name__)
if __name__ == "__main__":
    main()