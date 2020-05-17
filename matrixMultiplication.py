def bruteForceWay(matrixA, matrixB):
    rowsA= len(matrixA)
    rowsB= len(matrixB)
    columns= len(matrixB[0])

    matrixAnswer= []

    #For loop to choose row of matrixA
    for index in range(rowsA):
        row= []

        #For loop to choose columns in matrixB
        for index_ in range(columns):
            answerElement= 0

            # For loop to choose rows of matrixB
            for index__ in range(rowsB):

                answerElement+= matrixA[index][index__]* matrixB[index__][index_]

            row.append(answerElement)
            
        
        matrixAnswer.append(row)

    return matrixAnswer

if __name__== '__main__':
    matrixA= [[2, 1, 4, 4], [0, 1, 1, 2], [0, 4, -1, 2]]
    matrixB= [[6, 1], [3, 1], [-1, 0], [-1, -2]]

    answer= bruteForceWay(matrixA, matrixB)
    print(answer)