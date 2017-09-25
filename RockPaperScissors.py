#Rock Paper Scissors Game - Adv.

#Main() runs menu, repeat loop, and end message. can set number of games, difficulty
#choosing: ask for input, rock, paper, scissors
#comparing: paper beats rock, rock beats scissors, scissors beat paper,
#lookup table of win/lose/tie conditions, return condition, keep tally
#ending score display, victor, or time of game, depending.

import random as rn
#create tuple of win conditions, and extrapolate losses too
winConditions=(('rock','scissors'),('scissors','paper'),('paper','rock'))
border='='
totalMatchResults=[]

def rockpaperscissors():
    #declare totals
    winHumantotal=0
    winCPUtotal=0
    matchTotal=0
    print('Rocks, Papers, and Scissors')
    #continue loop check
    continueGame=True
    while continueGame:      
        gameDiff=input('Which difficulty would you like?\n(Easy, Normal, or Hard)\n')
        if gameDiff=='Easy' or gameDiff=='easy':
            #easy is against a computer choosing at random. No pattern except psuedo-random numbers
            gameVal=int(input('How many games would you like to play?\n'))            
            (newHwin,newCwin,newMatch)=gameEasy(gameVal)
        elif gameDiff=='Normal' or gameDiff=='normal':
            #hard mode will change its play based on your choices and long term trends, as well as changing its pattern over many matches
            gameVal=int(input('How many games would you like to play?\n'))            
            (newHwin,newCwin,newMatch)=gameNormal(gameVal)
        elif gameDiff=='Hard' or gameDiff=='hard':
            #hard mode will change its play based on your choices and long term trends, as well as changing its pattern over many matches
            gameVal=int(input('How many games would you like to play?\n'))            
            (newHwin,newCwin,newMatch)=gameHard(gameVal)        
        else:
            #badinput check
            continue
        winHumantotal+=newHwin
        winCPUtotal+=newCwin
        matchTotal+=newMatch
        continueGame=input('Would you like to play another game? (y/n)\n')
        if continueGame != 'y':
            continueGame=False
    #display totals
    print('You won',winHumantotal,'games, and the computer won',winCPUtotal,'games, with',(matchTotal-(winHumantotal+winCPUtotal)),'ties.')
    print('A total of',matchTotal,'games were played.')

def gameEasy(val):
    #declare local totals
    matchTotal=0
    winHuman=0
    winCPU=0
    #get the 'best out of' value by removing least part of number (5-2=3, 4-2=2, 3-1=2, etc.)
    winMajority=(val-val//2)
    #print(winMajority)
    if ((winHuman or winCPU) != winMajority):
        for match in range(val):
            print('Match #',match+1,sep='')
            #print('wins(cpu/human):',winCPU,'!',winHuman)
            #get players hand
            badinput=True
            while badinput:
                player1=int(input('1.Rock, 2.Paper, or 3.Scissors?: '))
                if player1==1:
                    badinput=False
                    player1='rock'                    
                elif player1==2:
                    badinput=False
                    player1='paper'                    
                elif player1==3:
                    badinput=False
                    player1='scissors'
                else:
                    badinput=True
            #get random hand from CPU
            player2=randCPU()
            #run through winConditions lookup, 
            #find current hand, check against CPU's, check converse, check if same, then check next value in lookup
            for item in range(len(winConditions)):
                #run through winConditions, get hand value at [item, 0] and check if comp won
                if (player1==winConditions[item][0] and player2==winConditions[item][1]):
                    #winState='win'
                    print('You won the hand! I chose ',player2,'.',sep='')
                    winHuman+=1
                    matchTotal+=1
                    break
                #check converse
                elif (player1==winConditions[item][1] and player2==winConditions[item][0]):
                    #winState='lose'
                    print('I beat you with ',player2,'!',sep='')
                    winCPU+=1
                    matchTotal+=1
                    break
                #check tie
                elif player1==player2:
                    #winState='tie'
                    print('We have a tie! I also chose',player2)
                    matchTotal+=1
                    break
    #check scores for who beat who or if tie, display results for this game
    if winHuman>winCPU:
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')
        print('You beat me...')
    elif winHuman<winCPU:
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')
        print('I win!')
    else:
        print('We have tied',val,' matches.')
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')      
    #return this game value to total game values
    return(winHuman,winCPU,matchTotal)

def gameNormal(val):
    lastHand='rock'
    lastState='init'
    matchTotal=0
    winHuman=0
    winCPU=0
    winMajority=(val-val//2)
    #print('best out of x')
    #print(winMajority)
    if ((winHuman or winCPU) != winMajority):
        for match in range(val):
            #check for majority win
            print('Match #',match+1,sep='')
            #print('wins(cpu/human):',winCPU,'!',winHuman)
            badinput=True
            while badinput:
                player1=int(input('1.Rock, 2.Paper, or 3.Scissors?: '))
                if player1==1:
                    badinput=False
                    player1='rock'                    
                elif player1==2:
                    badinput=False
                    player1='paper'                    
                elif player1==3:
                    badinput=False
                    player1='scissors'
                else:
                    badinput=True
            #Get player2 to choose hand
            player2=normalCPU(lastHand,lastState)
            #print(player2)
            for item in range(len(winConditions)):
                if (player1==winConditions[item][0] and player2==winConditions[item][1]):
                    #winState='win'
                    print('You won the hand! I chose ',player2,'.',sep='')
                    winHuman+=1
                    matchTotal+=1
                    lastHand=winConditions[item][1]
                    lastState='lose'
                    break
                elif (player1==winConditions[item][1] and player2==winConditions[item][0]):
                    #winState='lose'
                    print('I beat you with ',player2,'!',sep='')
                    winCPU+=1
                    matchTotal+=1
                    lastHand=winConditions[item][0]
                    lastState='win'
                    break
                elif player1==player2:
                    #winState='tie'
                    print('We have a tie! I also chose',player2)
                    matchTotal+=1
                    lastHand=player1
                    lastState='tie'
                    break
    if winHuman>winCPU:
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')
        print('You beat me...')
    elif winHuman<winCPU:
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')
        print('I win!')
    else:
        print('We have tied',val,' matches.')
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')
    return(winHuman,winCPU,matchTotal)

def gameHard(val):
    lastHand='rock'
    lastState='init'
    matchResults=[]
    matchTotal=0
    winHuman=0
    winCPU=0
    winMajority=(val-val//2)
    #print('best out of x')
    #print(winMajority)
    if ((winHuman or winCPU) != winMajority):
        for match in range(val):
            #check for majority win
            print('Match #',match+1,sep='')
            #print('wins(cpu/human):',winCPU,'!',winHuman)
            badinput=True
            while badinput:
                player1=int(input('1.Rock, 2.Paper, or 3.Scissors?: '))
                if player1==1:
                    badinput=False
                    player1='rock'                    
                elif player1==2:
                    badinput=False
                    player1='paper'                    
                elif player1==3:
                    badinput=False
                    player1='scissors'
                else:
                    badinput=True
            #Get player2 to choose hand
            player2=hardCPU(lastHand,lastState,matchResults)
            #print(player2)
            for item in range(len(winConditions)):
                if (player1==winConditions[item][0] and player2==winConditions[item][1]):
                    #winState='win'
                    print('You won the hand! I chose ',player2,'.',sep='')
                    winHuman+=1
                    matchTotal+=1
                    lastHand=winConditions[item][1]
                    lastState='lose'
                    break
                elif (player1==winConditions[item][1] and player2==winConditions[item][0]):
                    #winState='lose'
                    print('I beat you with ',player2,'!',sep='')
                    winCPU+=1
                    matchTotal+=1
                    lastHand=winConditions[item][0]
                    lastState='win'
                    break
                elif player1==player2:
                    #winState='tie'
                    print('We have a tie! I also chose',player2)
                    matchTotal+=1
                    lastHand=player1
                    lastState='tie'
                    break
    if winHuman>winCPU:
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')
        print('You beat me...')
    elif winHuman<winCPU:
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')
        print('I win!')
    else:
        print('We have tied',val,' matches.')
        print('You won ',winHuman,' out of ',val,' matches!',sep='')
        print('I won ',winCPU,' out of ',val,' matches!',sep='')
    return(winHuman,winCPU,matchTotal)

def randCPU():
    shake=rn.randint(0,2)
    if shake==0:
        hand='rock'
    elif shake==1:
        hand='scissors'
    else:
        hand='paper'
    #print(hand)
    return hand

def normalCPU(lastHand,lastState):
    #simple AI
    if lastState=='init':
        #starting state
        #50/50 based on likelyhood of rock being strongest, as well as opponent prempting that, so play counter to paper
        num=rn.randint(0,1)
        if num==0:
            hand='rock'
        else:
            hand='scissors'
    elif lastState=='win':
        #won last
        #even chance after winning of either: being able to choose same hand, or opponent countering that, so play counter
        num=rn.randint(0,1)
        if num==0:
            hand=lastHand
        else:
            if lastHand=='rock':
                hand='paper'
            elif lastHand=='paper':
                hand='scissors'
            else:
                hand='rock'
    elif lastState=='lose':
        #lost last
        #play the unplayed choice out of the last two played
        if lastHand=='rock':
            hand='scissors'
        elif lastHand=='paper':
            hand='rock'
        else:
            hand='paper'        
    else:
        #tied last
        #play anything
        hand=randCPU()
    return hand

def hardCPU(lasthand,laststate,resultlist):
    #simple AI
    if lastState=='init':
        #starting state
        #50/50 based on likelyhood of rock being strongest, as well as opponent prempting that, so play counter to paper
        num=rn.randint(0,1)
        if num==0:
            hand='rock'
        else:
            hand='scissors'
    elif lastState=='win':
        #won last
        #even chance after winning of either: being able to choose same hand, or opponent countering that, so play counter
        num=rn.randint(0,1)
        if num==0:
            hand=lastHand
        else:
            if lastHand=='rock':
                hand='paper'
            elif lastHand=='paper':
                hand='scissors'
            else:
                hand='rock'
    elif lastState=='lose':
        #lost last
        #play the unplayed choice out of the last two played
        if lastHand=='rock':
            hand='scissors'
        elif lastHand=='paper':
            hand='rock'
        else:
            hand='paper'        
    else:
        #tied last
        #play anything
        hand=randCPU()
    return hand


#mainstart
#main()
rockpaperscissors()
