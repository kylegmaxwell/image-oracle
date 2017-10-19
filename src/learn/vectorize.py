import json
import glob
import shuffle

class Vectorizer:

    def __init__(self):
        # keys are file names, values are all labels for that file
        self.fileLabels = {}
        # keys are file names, values are all scores for that file
        self.fileScores = {}
        # map keys are all labels encountered, and value is frequency
        self.allLabels = {}

    def parseLabels(self, labelFiles):
        # Count the annotations in each file
        for file in labelFiles:
            f = open(file, 'r')
            lines = " ".join(f.readlines())
            data = json.loads(lines)
            annotations = data[0]["labelAnnotations"]
            labels = []
            scores = dict();
            for annotationData in annotations :
                a = annotationData["description"]
                if a in self.allLabels :
                    self.allLabels[a] = self.allLabels[a] + 1
                else:
                    self.allLabels[a]=1
                if not a in labels:
                    labels.append(a)
                # TODO there could be redundant labels, so use the first score
                scores[annotationData["description"]]=annotationData["score"]
            self.fileScores[file]=scores;
            self.fileLabels[file]=labels
            # break

    # return all labels as a list, only inluding those with frequency more than min count
    def getLabels(self, minCount):
        # label list is a sorted array of all the labels by their frequency
        # it is used to form the vectors that are input to the learning algorithm
        labelList = []
        labelList = sorted(self.allLabels, key=self.allLabels.__getitem__)
        labelList.reverse()
        trimList = []
        for label in labelList:
            if self.allLabels[label] >= minCount:
                trimList.append(label)
        #     print(label + " " + str(allLabels[label]))
        return trimList

    def getVectors(self, labelList, labelFiles):
        vecs = []
        files = []
        # for each image
        for i in range(0,len(labelFiles)):
            file = labelFiles[i]
            labels = self.fileLabels[file]
            scores = self.fileScores[file]
            labelVec = []
            # Find the labels in the sorted master vec and create weights vec
            for j in range(0,len(labelList)):
                value = 0;
                if labelList[j] in labels:
                    # print(j, labelList[j])
                    value = scores[labelList[j]]
                labelVec.append(value)
            # print("\n"+str(labelVec))
            vecs.append(labelVec)
            files.append(file)
        return [vecs, files]

def vectorize(trainFile, testFile, minCount):
    vec = Vectorizer()

    # Load all the JSON files with annotation data
    originalFiles = glob.glob("./data/original/*.json")
    print("original "+str(len(originalFiles)))
    vec.parseLabels(originalFiles)

    imposterFiles = glob.glob("./data/imposter/*.json")
    print("imposter "+str(len(imposterFiles)))
    vec.parseLabels(imposterFiles)

    labelList = vec.getLabels(minCount)

    vecFileTemp = vec.getVectors(labelList, originalFiles)
    originalVec = vecFileTemp[0]
    originalFileList = vecFileTemp[1]

    # Add the y values
    for v in originalVec:
        v.append(1)

    vecFileTemp = vec.getVectors(labelList, imposterFiles)
    imposterVec = vecFileTemp[0]
    imposterFileList = vecFileTemp[1]

    for v in imposterVec:
        v.append(0)

    # Combine vectors
    vec = originalVec
    vec.extend(imposterVec)

    fileList = originalFileList
    fileList.extend(imposterFileList)

    index = shuffle.shuffle(vec)

    shuffledFileList = [0 for x in fileList]
    for i in range(0,len(index)):
        shuffledFileList[i] = fileList[index[i]]

    # Use most of the data to train and save a fraction for testing accuracy
    cutoff = int(len(vec)*0.8)

    trainVec = vec[0:cutoff]
    testVec = vec[cutoff:]

    trainFiles = shuffledFileList[0:cutoff]
    testFiles = shuffledFileList[cutoff:]

    printFiles(f"{trainFile}-index.csv", trainFiles)
    printFiles(f"{testFile}-index.csv", testFiles)

    # Write data out to csv files
    printVec(f"{trainFile}.csv",trainVec)
    printVec(f"{testFile}.csv",testVec)

def printFiles(path, files):
    print(f"Write file {path}")
    f = open(path, 'w')
    for file in files:
        f.write(file)
        f.write('\n')
    f.close()

def printVec(path, vec):
    print(f"Write file {path}")
    f = open(path, 'w')
    f.write(f"{len(vec)},{len(vec[0])-1},not,original\n")
    for v in vec:
        for i in range(0,len(v)):
            f.write(str(v[i]))
            if i<len(v)-1:
                f.write(',')
        f.write('\n')
    f.close()
