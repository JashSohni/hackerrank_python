def minion_game(s):
    A=['A','E','I','O','U']
    input1 = list(s)
    flag = 0
    score1 = 0
    score2 = 0
    length=len(s)
    for i in range(0,length,1):
        for j in A:
            if input1[i] == j:
                score1 +=length - i 
                flag = 1
                break
        if flag == 0 :
            score2 +=length - i
        else:
            flag = 0
    
    if score1 > score2:
        print("Kevin "+str(score1))
    elif score2 > score1:
        print("Stuart "+str(score2))
    else:
        print("Draw")

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)