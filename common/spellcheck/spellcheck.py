# coding:utf-8
import codecs

'''
    read and write file
'''
# read file, return dict


def readWordSet(file):
    fin = codecs.open(file, "r", "utf-8")
    wordSet = set()
    for line in fin.readlines():
        word = line.strip().lower()
        wordSet.add(word)
    fin.close()
    return wordSet


def readParameter(file):
    fin = codecs.open(file, "r", "utf-8")
    param = {}
    for line in fin.readlines():
        tokens = line.strip().lower().split("\t")
        if len(tokens[1].split(':')) >= 2:
            temp = {}
            for token in tokens[1].strip().split(" "):
                tempToken = token.split(':')
                temp[tempToken[0]] = tempToken[1]
            param[tokens[0]] = temp
        else:
            param[tokens[0]] = tokens[1]
    fin.close()
    return param

# write dict to a file


def writeFile(file, words):
    fout = codecs.open(file, "w", "utf-8")
    for k, v in words.items():
        if type(v) == dict:
            fout.write(k + "\t")
            for kk, vv in v.items():
                fout.write(kk + ":" + str(vv) + " ")
            fout.write("\n")
        else:
            fout.write(k + "\t" + str(v) + "\n")
    fout.close()

'''
    compute the minimum edit distance
    method: getCandidate(s, wordSet)
    input: s:string
           wordSet
    return: input string's candidates
'''


def f(c1, c2):
    if c1 == c2:
        return 0
    else:
        return 1


def editDistance(s1, s2):
    dist = [[0 for col in range(len(s2)+1)] for row in range(len(s1)+1)]
    for j in range(len(s2)+1):
        dist[0][j] = j
    for i in range(len(s1)+1):
        dist[i][0] = i
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            dist[i][j] = min(
                dist[i-1][j]+1, dist[i][j-1]+1, dist[i-1][j-1]+f(s1[i-1], s2[j-1]))
    return dist[len(s1)][len(s2)]


def getCandidate(s, wordSet):
    candis = []
    for word in wordSet:
        word = word.strip()
        if (abs(len(word)-len(s)) <= 1):
            if(editDistance(s, word) <= 1):
                candis.append(word)
    if len(candis) == 0:
        candis.append(s)
    return candis

'''
    train bigram, bayes estimation
    input: train file
           wordSet
    return bagOfword
           parameter
'''


def bigram(file, wordSet):
    fin = codecs.open(file, "r", "utf-8")
    bagOfWord = {}
    parameter = {}
    for line in fin.readlines():
        wordlist = line.lower().strip().split()
        for i in range(len(wordlist)-1):
            if wordlist[i] in wordSet and wordlist[i+1] in wordSet:
                if bagOfWord.has_key(wordlist[i]):  # update bagOfword
                    bagOfWord[wordlist[i]] += 1
                else:
                    bagOfWord[wordlist[i]] = 1

                if parameter.has_key(wordlist[i]):  # update parameter
                    temp = parameter[wordlist[i]]
                    if temp.has_key(wordlist[i+1]):
                        temp[wordlist[i+1]] += 1
                    else:
                        temp[wordlist[i + 1]] = 1
                    parameter[wordlist[i]] = temp
                else:
                    parameter[wordlist[i]] = {wordlist[i+1]: 1}
    fin.close()
    return bagOfWord, parameter


def score(qt, qt1, bagOfword, parameter):
    if parameter.has_key(qt):
        if parameter[qt].has_key(qt1):
            return 1.0 * int(parameter[qt][qt1]) / int(bagOfword[qt])
        else:
            return 1.0 / (int(bagOfword[qt]) + 15000)
    return 0


def spellCorret(instring, wordSet, bagOfword, parameter):
    if len(instring.strip()) == 0:
        return ""
    path = []
    result = []
    candidates = []
    wordList = instring.lower().strip().split()
    for i in range(len(wordList)):
        candidates.append(getCandidate(wordList[i], wordSet))

    # print "candidates:",candidates

    currentResult = [1.0/len(candidates[0]) for i in range(len(candidates[0]))]
    currentPath = [0 for i in range(len(candidates[0]))]
    result.append(currentResult)
    path.append(currentPath)
    for i in range(1,len(candidates)):
        currentResult = []
        currentPath = []
        for j in range(len(candidates[i])):
            # print "len(candidates)[i]:", len(candidates[i])
            qt1 = candidates[i][j]
            temp = 0
            preNode = 0
            for k in range(len(candidates[i-1])):
                qt=candidates[i-1][k]
                # print qt,qt1,path[i-1][k],score(qt, qt1, bagOfword, parameter )
                tempscore = result[i-1][k]*score(qt, qt1, bagOfword, parameter)
                if tempscore > temp:
                    temp = tempscore
                    preNode = k
            currentResult.append(temp)
            currentPath.append(preNode)
        result.append(currentResult)
        path.append(currentPath)

    # print "path: ",path
    # print "result:",result
    # backtrace
    temp = result[len(result)-1][0]
    preIndex = path[len(path)-1][0]
    correctInput = candidates[len(result) - 1][0]
    for i in range(1, len(result[len(result)-1])):
        if result[len(result)-1][i] > temp:
            temp = result[len(result)-1][i]
            preIndex = path[len(path)-1][i]
            correctInput = candidates[len(result) - 1][i]

    # print "preIndex:",preIndex
    for i in range(len(path)-2, -1, -1):
        correctInput = candidates[i][preIndex] + " " + correctInput
        preIndex = path[i][preIndex]
        # print "preIndex:", preIndex

    if correctInput == instring:
        correctInput = ""
    return correctInput

def train():
    wordSet = readWordSet("word.txt")  # 读词典
    bagOfword, parameter = bigram("contentBigram.dat", wordSet)  # 贝叶斯估计参数
    writeFile("bagOfword.txt", bagOfword)
    writeFile("parameter.txt", parameter)
    return wordSet, bagOfword, parameter

# def init():
#     wordSet = readWordSet("word.txt")
#     bagOfword = readParameter("bagOfword.txt")
#     parameter = readParameter("parameter.txt")
#     return wordSet,bagOfword,parameter

def init(word_path, bagOfword_path, param_path):
    wordSet = readWordSet(word_path)
    bagOfword = readParameter(bagOfword_path)
    parameter = readParameter(param_path)
    return wordSet, bagOfword, parameter

if __name__=='__main__':
    wordSet, bagOfword, parameter = init("word.txt", "bagOfword.txt", "parameter.txt")
    while True:
        str = raw_input("Please input the query: ")
        spellCorrect = spellCorret(str, wordSet, bagOfword, parameter)   #tesat
        print spellCorrect
