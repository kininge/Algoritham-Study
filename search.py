def binarySearch(inputList, element):
    left= 0
    right= len(inputList)- 1

    while(left< right):
        mid= ((left+ right)// 2)

        if(inputList[mid]> element):
            right= mid
        elif(inputList[mid]< element):
            left= mid+ 1
        else:
            return mid
    
    return -1

def exactSearch(inputList, element):
    firstElement= inputList[0]
    lastElement= inputList[-1]
    lengthOfList= len(inputList)

    index= (((lastElement- firstElement)* element)// lengthOfList)- 1

    if(inputList[index]== element):
        return index
    elif(inputList[index]> element):

        for index_ in range(index- 1, -1, -1):

            if(inputList[index_]== element):
                return index_
            elif(inputList[index_]< element):
                return -1
        return -1
    else:
        for index_ in range(index+ 1, lengthOfList):
    
            if(inputList[index_]== element):
                return index_
            elif(inputList[index_]> element):
                return -1
        return -1

if __name__== '__main__':
    inputList= [1, 2, 2, 5, 6, 7, 7, 8, 9, 9]
    element= 9

    print(exactSearch(inputList, element))
    print(binarySearch(inputList, element))