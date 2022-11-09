import actions as act


def callNum(sign):
    numbersDict = {'1': act.number1, '2': act.number2, '3': act.number3, '4': act.number4, '5': act.number5, '6': act.number6, '7': act.number7, '8': act.number8, '9': act.number9}
    numbersDict[sign]()


def callAlphabet(sign):
    alphabetDict = {'A': act.letterA,'B': act.letterB,'C': act.letterC, 'D': act.letterD, 'E': act.letterE, 'F': act.letterF, 'G': act.letterG, 'H': act.letterH, 'I': act.letterI, 'J': act.letterJ, 'K': act.letterK, 'L': act.letterL, 'M': act.letterM, 'N': act.letterN, 'O': act.letterO, 'P': act.letterP, 'Q': act.letterQ, 'R': act.letterR, 'S': act.letterS, 'T': act.letterT, 'U': act.letterU, 'V': act.letterV, 'W': act.letterW, 'X': act.letterX, 'Y': act.letterY, 'Z': act.letterZ}
    alphabetDict[sign]()


def callWords(sign):
    wordsDict = {"HELLO": act.wordHello(),"OK": act.wordOkay(),"BYE": act.wordBye()}
    wordsDict[sign]


def implementGesture(sign):
    signLength= len(sign)
    numbersList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    wordList = ["HELLO", "OK", "BYE"]

    if signLength == 1:
        num = 0
        for elem in numbersList:
            if elem == sign:
                callNum(sign)
                num = 1
                break
        if num==0:
            for elem in alphabetList:
                if elem == sign:
                    callAlphabet(sign)
                    break
    else:
        for elem in wordList:
            if elem == sign:
                callWords(sign)
                break
