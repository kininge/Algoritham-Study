def crossMaxSubArray(inputList, low, mid, high):
    print('low: '+str(low)+' mid: '+str(mid)+' high: '+str(high))

    total= 0
    leftSum= -10** 9

    for index in range(mid, low- 1, -1):
        total+= inputList[index]

        if(total> leftSum):
            leftSum= total
        
        print('index: '+str(index)+' total: '+str(total)+' leftSum: '+str(leftSum))

    total= 0
    rightSum= -10** 9

    for index in range(mid+ 1, high+ 1, 1):
        total+= inputList[index]

        if(total> rightSum):
            rightSum= total
        
        print('index: '+str(index)+' total: '+str(total)+' rightSum: '+str(rightSum))

    print('leftSum: '+str(leftSum)+' rightSum: '+str(rightSum))
    return max((leftSum+ rightSum), leftSum, rightSum)

def divideAndConcorAlgoritham(inputList, low, high):
    print('low: '+str(low)+' high: '+str(high))

    if(low== high):
        return inputList[low]
    else:
        mid= (low+ high)// 2

        lowMax= divideAndConcorAlgoritham(inputList, low, mid)
        print('lowMax: '+str(lowMax))
        highMax= divideAndConcorAlgoritham(inputList, mid+ 1, high)
        print('highMax: '+str(highMax))
        crossMax= crossMaxSubArray(inputList, low, mid, high)
        print('crossMax: '+str(crossMax))

    return max(lowMax, highMax, crossMax)

def kadanesAlgoritham(inputList):
    n= len(inputList)
    answerIndexs= [0, 0]
    maxSubTotal= inputList[0]

    answerIndexsForNow= [0, 0]
    maxSubTotalForNow= inputList[0]
       
    for index in range(1, n): 
        maxSubTotalForNow+= inputList[index]
        
        if(maxSubTotalForNow>= inputList[index]):
            answerIndexsForNow[1]+= 1
        else:
            maxSubTotalForNow= inputList[index]
            answerIndexsForNow= [index, index]

        if(maxSubTotalForNow>= maxSubTotal):
            maxSubTotal= maxSubTotalForNow
            answerIndexs[0]= answerIndexsForNow[0]
            answerIndexs[1]= answerIndexsForNow[1]

    return [answerIndexs, maxSubTotal]

def bruteForce(inputList):
    n= len(inputList)
    answer=[[0, 0],0]

    for index in range(n):

        addition= 0
        for index_ in range(index, n):
            addition+= inputList[index_]

            if(answer[1]< addition):
                answer= [[index, index_], addition]

    return answer

if __name__== '__main__':
    inputList= [1, -3, 6, -5, 7, 6, -1, -4, 4, -23]
    answer= divideAndConcorAlgoritham(inputList, 0, len(inputList)- 1)
    print(answer)