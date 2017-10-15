import glob

import vectorize

import shuffle

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

    # Add the y values
    for v in originalVec:
        v.append(1)
    imposterVec = vec.getVectors(labelList, imposterFiles)
    for v in imposterVec:
        v.append(0)

    # Combine vectors
    vec = originalVec
    vec.extend(imposterVec)

    shuffle.shuffle(vec)

    # Use most of the data to train and save a fraction for testing accuracy
    cutoff = int(len(vec)*0.8)

    trainVec = vec[0:cutoff]
    testVec = vec[cutoff:]

    # Write data out to csv files
    printVec('train',trainVec)
    printVec('test',testVec)

def printVec(name, vec):
    path = f"data/{name}.csv"
    f = open(path, 'w')
    f.write(f"{len(vec)},{len(vec[0])-1},not,original\n")
    for v in vec:
        for i in range(0,len(v)):
            f.write(str(v[i]))
            if i<len(v)-1:
                f.write(',')
        f.write('\n')
    f.close()
main()