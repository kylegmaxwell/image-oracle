import json

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
        return vecs