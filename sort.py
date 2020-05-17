
def inserstionSort(inputList):

    for index in range(1, len(inputList)):
        element= inputList[index]

        for index_ in range(index):

            if(inputList[index_]> element):
                inputList.insert(index_, element)
                inputList.pop(index+ 1)
                break

def selectionSort(inputList):

    numberOfElements= len(inputList)
    for index in range(0, numberOfElements- 1):
        smallestIndex= index
        smallestElement= inputList[index]

        for index_ in range(index+ 1, numberOfElements):
            newElement= inputList[index_]
            if(smallestElement> newElement):
                smallestIndex= index_
                smallestElement= newElement

        temp= inputList[index]
        inputList[index]= smallestElement
        inputList[smallestIndex]= temp

def merge(inputList, leftIndex, mid, rightIndex):

    leftLenght= mid- leftIndex
    leftList= inputList[leftIndex: mid]
    rightLenght= rightIndex- mid
    rightList= inputList[mid: rightIndex]

    indexLeft= 0
    indexRight= 0
    mainIndex= leftIndex

    while((indexLeft< leftLenght) and (indexRight< rightLenght)):
        if(leftList[indexLeft]<= rightList[indexRight]):
            inputList[mainIndex]= leftList[indexLeft]
            indexLeft+= 1
        else:
            inputList[mainIndex]= rightList[indexRight]
            indexRight+= 1

        mainIndex+= 1

    while(indexLeft< leftLenght):
        inputList[mainIndex]= leftList[indexLeft]
        indexLeft+= 1
        mainIndex+= 1
        

    while(indexRight< rightLenght):
        inputList[mainIndex]= rightList[indexRight]
        indexRight+= 1
        mainIndex+= 1

def mergeSort(inputList, leftIndex, rightIndex):

    if((leftIndex+ 1)< rightIndex):
        mid= (rightIndex+ leftIndex)// 2

        mergeSort(inputList, leftIndex, mid)
        mergeSort(inputList, mid, rightIndex)
        merge(inputList, leftIndex, mid, rightIndex)

def bubbleSort(inputList):
    exchnage= 1
    while(exchnage> 0):
        exchnage= 0
        for index in range(len(inputList)- 1):
            if(inputList[index]> inputList[index+ 1]):
                temp= inputList[index]
                inputList[index]= inputList[index+ 1]
                inputList[index+ 1]= temp
                exchnage+= 1

    return inputList

if __name__== '__main__':
    inputList= [3, 2, 1]
    bubbleSort(inputList)
    print(inputList)