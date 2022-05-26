def do(userInput):
    userInputList = userInput.split()
    symbol1 = '*'
    symbol2 = '/'
    userInputList = doing(userInputList, symbol1, symbol2)

    symbol1 = '+'
    symbol2 = '-'
    userInputList = doing(userInputList, symbol1, symbol2)

    return userInputList[0]


def doing(userInputList, symbol1, symbol2):
    userInputListLength = len(userInputList)
    result_1 = findSymbolIndex(userInputList, symbol1, symbol2)
    result_1Length = len(result_1)
    i = 0

    if symbol1 == '*' or symbol2 == ' /' or symbol1 == '/' or symbol2 == ' *':
        while result_1Length >= 1:
            if userInputList[result_1[i]] == symbol1:
                userInputList.insert(
                    result_1[i] - 1,  (float(userInputList[result_1[i] - 1])) * (float(userInputList[result_1[i] + 1])))
                del userInputList[result_1[i]: result_1[i] + 3]
                result_1.pop(i)
                userInputListLength -= 2
                result_1Length -= 1
                result_1 = findSymbolIndex(userInputList, symbol1, symbol2)

            elif userInputList[result_1[i]] == symbol2:
                userInputList.insert(
                    result_1[i] - 1,  (float(userInputList[result_1[i] - 1]) / float(userInputList[result_1[i] + 1])))
                del userInputList[result_1[i]: result_1[i] + 3]
                result_1.pop(i)
                userInputListLength -= 2
                result_1Length -= 1
                result_1 = findSymbolIndex(userInputList, symbol1, symbol2)
    else:
        while result_1Length >= 1:
            if userInputList[result_1[i]] == symbol1:
                userInputList.insert(
                    result_1[i] - 1, float(userInputList[result_1[i] - 1]) + float(userInputList[result_1[i] + 1]))
                del userInputList[result_1[i]: result_1[i] + 3]
                result_1.pop(i)
                userInputListLength -= 2
                result_1Length -= 1
                result_1 = findSymbolIndex(userInputList, symbol1, symbol2)

            elif userInputList[result_1[i]] == symbol2:
                userInputList.insert(
                    result_1[i] - 1, (float(userInputList[result_1[i] - 1]) - float(userInputList[result_1[i] + 1])))
                del userInputList[result_1[i]: result_1[i] + 3]
                result_1.pop(i)
                userInputListLength -= 2
                result_1Length -= 1
                result_1 = findSymbolIndex(userInputList, symbol1, symbol2)
    return userInputList


def findSymbolIndex(userInputList, symbol1, symbol2):
    userInputListLength = len(userInputList)
    return [i for i in range(userInputListLength) if userInputList[i] == symbol1 or userInputList[i] == symbol2]
