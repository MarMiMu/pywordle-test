def display_board(words,scores):
    print(" "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", words[0][0] ," ","|"," ", words[0][1] ," ","|"," ", words[0][2] ," ","|"," ", words[0][3] ," ","|"," ", words[0][4] ," ")
    print(" ", scores[0][0]," ","|"," ", scores[0][1]," ","|"," ", scores[0][2]," ","|"," ", scores[0][3]," ","|"," ", scores[0][4]," ")
    print("-------------------------------------")
    print(" "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", words[1][0] ," ","|"," ", words[1][1] ," ","|"," ", words[1][2] ," ","|"," ", words[1][3] ," ","|"," ", words[1][4] ," ")
    print(" ", scores[1][0]," ","|"," ", scores[1][1]," ","|"," ", scores[1][2]," ","|"," ", scores[1][3]," ","|"," ", scores[1][4]," ")
    print("-------------------------------------")
    print(" "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", words[2][0] ," ","|"," ", words[2][1] ," ","|"," ", words[2][2] ," ","|"," ", words[2][3] ," ","|"," ", words[2][4] ," ")
    print(" ", scores[2][0]," ","|"," ", scores[2][1]," ","|"," ", scores[2][2]," ","|"," ", scores[2][3]," ","|"," ", scores[2][4]," ")
    print("-------------------------------------")
    print(" "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", words[3][0] ," ","|"," ", words[3][1] ," ","|"," ", words[3][2] ," ","|"," ", words[3][3] ," ","|"," ", words[3][4] ," ")
    print(" ", scores[3][0]," ","|"," ", scores[3][1]," ","|"," ", scores[3][2]," ","|"," ", scores[3][3]," ","|"," ", scores[3][4]," ")
    print("-------------------------------------")
    print(" "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", words[4][0] ," ","|"," ", words[4][1] ," ","|"," ", words[4][2] ," ","|"," ", words[4][3] ," ","|"," ", words[4][4] ," ")
    print(" ", scores[4][0]," ","|"," ", scores[4][1]," ","|"," ", scores[4][2]," ","|"," ", scores[4][3]," ","|"," ", scores[4][4]," ")
    print("-------------------------------------")
    print(" "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", words[5][0] ," ","|"," ", words[5][1] ," ","|"," ", words[5][2] ," ","|"," ", words[5][3] ," ","|"," ", words[5][4] ," ")
    print(" ", scores[5][0]," ","|"," ", scores[5][1]," ","|"," ", scores[5][2]," ","|"," ", scores[5][3]," ","|"," ", scores[5][4]," ")

def guess(words,scores,i):
    guess = input("Guess Word:")
    result = checkGuess(guess)
    words[i] = guess
    scores[i] = result
    evaluation = getEval(result)
    display_board(words,scores)
    print(evaluation)
    return guess 

def getEval(result):
    temp = 0
    for i in result:
        if i == "G":
            temp += 2
        if i == "Y":
            temp += 1
    return temp

def checkGuess(guess):
    answer = getanswer()
    result = ""
    for i in range(len(guess)):
        if guess[i] in answer:
            letter = 'Y'
            if guess[i] == answer[i]:
                letter = 'G'
        else:
            letter = '_'
        result = result + letter
    return result

def getanswer():
    answer = "moist"
    return answer

def isAnswer(guess):
    answer = getanswer()
    if guess == answer:
        return True
    else:
        return False

def main():
    win = False; 
    words = ["_____","_____","_____","_____","_____","_____"]
    scores= ["     ","     ","     ","     ","     ","     "]
    display_board(words,scores)
    counter = 0
    while (counter != 6 and win == False):
        attempt = guess(words,scores,counter)
        win = isAnswer(attempt)
        counter = counter + 1
        if win:
            print("Winner")

def word_guesses():
    word_list = ["apple","means","shape","shard","minds","shark","peace"]
    scores_list = []
    for i in word_list:
        res1 = checkGuess(i)
        res2 = getEval(res1)
        scores_list.append(res2)
    print(scores_list)

