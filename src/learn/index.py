import glob

import vectorize

def main():
    print("hello")

    vec = vectorize.Vectorizer()

    # Load all the JSON files with annotation data
    originalFiles = glob.glob("./data/original/*.json")
    print("original "+str(len(originalFiles)))
    vec.parseLabels(originalFiles)

    imposterFiles = glob.glob("./data/imposter/*.json")
    print("imposter "+str(len(imposterFiles)))
    vec.parseLabels(imposterFiles)

    labelList = vec.getLabels(2)
    print(labelList)

    originalVec = vec.getVectors(labelList, originalFiles)
    printVec(originalVec);

    imposterVec = vec.getVectors(labelList, imposterFiles)
    printVec(imposterVec);


def printVec(vec):
    for v in vec:
        # print(",".join(v))
        print("")
        print(str(v))
    print(len(vec))
main()