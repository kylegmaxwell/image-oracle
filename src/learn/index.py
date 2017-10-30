import vectorize
import os
import flow

# Convert data to vectors and run macine learning
def main():
    # Data sets
    IMAGE_TRAINING = "./data/train"
    IMAGE_TEST = "./data/test"
    # Labels must appear this many times to be counted
    MIN_COUNT = 7
    # Training steps
    STEPS = 2000

    # Convert labels to vectors
    vectorize.vectorize(IMAGE_TRAINING, IMAGE_TEST, MIN_COUNT);

    # Run machine learning
    flow.flow(f"{IMAGE_TRAINING}.csv", f"{IMAGE_TEST}.csv",STEPS)

print(__name__)
if __name__ == "__main__":
    main()