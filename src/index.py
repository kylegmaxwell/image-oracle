import glob
import json

def main():
    print("hello")
    # Load all the JSON files with annotation data
    dataDir = './data/original'
    labels = glob.glob(dataDir+"/*.json")

    allLabels = dict()
    allDescriptions = []
    allAnnotations = []
    # Count the annotations in each file
    for file in labels:
        f = open(file, 'r')
        lines = " ".join(f.readlines())
        data = json.loads(lines)
        annotations = data[0]["labelAnnotations"]
        descriptions = []
        annDict = dict();
        for annotationData in annotations :
            a = annotationData["description"]
            if a in allLabels :
                allLabels[a] = allLabels[a] + 1
            else:
                allLabels[a]=1
            if not a in descriptions:
                descriptions.append(a)
            annDict[annotationData["description"]]=annotationData["score"]
        allAnnotations.append(annDict);
        allDescriptions.append(descriptions)
        # break
    labelList = []
    labelList = sorted(allLabels, key=allLabels.__getitem__)
    labelList.reverse()

    # for each image
    for i in range(0,len(allDescriptions)):
        descriptions = allDescriptions[i]
        annDict = allAnnotations[i]
        labelVec = []
        # Find the labels in the sorted master vec and create weights vec
        for j in range(0,len(labelList)):
            value = 0;
            if labelList[j] in descriptions:
                print(j, labelList[j])
                value = annDict[labelList[j]]
            labelVec.append(value)
        print("\n"+str(labelVec))


main()