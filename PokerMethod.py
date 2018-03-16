#Poker Method
#Cory Cothrum
#5/15/2017

import random as rn

#Experimental Cipher method combining custom length ADFGVX grids
#and playing card suits, taking advantage of phrase swap even letters method

#Todo: rethink idea into 'poker hands' and print out hands and possibly noise. declare noise somewhow in key
#implement german day charts?
#jibberish letters/letter frequency stuffing? dual rows of values?

cardvalues='A234567890JQK'
#hearts clubs diamonds spades
cardsuits='HDCS'

def main():
    decksize=52
    #create initial deck of cards, use as constant
    carddeck=deckPrinter(decksize)
    cipherchart=chartCreator()

def deckPrinter(size):
    #create deck
    #empty list
    carddeck=[]
    for card in range(size):
        #print(carddeck)
        #'make' card, give it a value and suit, send to deck
        currentcard=[(cardvalues[card%len(cardvalues)],cardsuits[card%len(cardsuits)])]
        carddeck+=currentcard
    #print(carddeck,len(carddeck))
    #initially shuffle deck about 20 times
    cardDeckShuffle(carddeck,20)
    return carddeck
    
def cardDeckShuffle(deck,shuffles):
    randspot1=rn.randint(1,(len(deck)-1))
    lastcard=deck[51]
    #print(lastcard)
    #takes deck, randomly swaps
    for steps in range(shuffles):
        #print('Shuffling...')
        lastcard=deck[len(deck)-1]     
        for card in range(len(deck)*10):
            #print('card',card)
            #take top card, check if its the last card of the deck we started shuffling
            topcard=deck[0]              
            if topcard != lastcard:
                randspot1=rn.randint(1,len(deck)-1)
                topcard=deck.pop(0)
                deck.insert(randspot1,topcard)
            else:
                break
    
def chartCreator():
    #Chart relates to real 6x6 grid as index positions; first index if rox, second column. IE 00 ia AA, 01 is AD, 55 is XX, etc.
    #Using an existing code?
    loadchart=input('Do you have an existing chart you would like to use: (y/n)\n')
    if loadchart=='y' or loadchart=='Y':
        try:
            #load from file .txt with chart
            print('Please enter file path for chart: ')
        except:
            print('This is not a valid file path. Please enter valid file path.')
    else:
        #Get gridkey, can be anything from ADFGX [original German method], ADFGVX, or Hex values/Poem. Repeating values are tougher
        #global gridkey
        gridkeytop=cardvalues
        gridkeyside=cardsuits
        gridsize=(len(gridkeytop)*len(gridkeyside))
        print('The grid will be',gridsize,'slots (split in two).')
        #this list will be limited to len*len
        chartValues=[]
        charPool='abcdefghijklmnopqrstuvwxyz'
        charPoolRun=charPool
        #print(charPoolRun)
        #fill the grid [size of phrase*phrase] with charcters, repeat until full
        for item in range(gridsize):
            if len(charPoolRun)==0 and len(chartValues) != gridsize:
                charPoolRun=charPool      
            randnum=rn.randint(0,(len(charPoolRun)-1))
            chartValues.append(charPoolRun[randnum])
            charPoolRun=charPoolRun.replace((charPoolRun[randnum]),'')
        #print(charPoolRun)
        #print(chartValues)
        #delistify it-['', '']
        chartValues=str(chartValues).replace("'",'')
        chartValues=chartValues.replace(',','')
        chartValues=chartValues.replace(' ','')
        chartValues=chartValues.replace('[','')
        chartValues=chartValues.replace(']','')
    print(chartValues)
    return chartValues  

def phraseShift(message, phrase):
    print('')

#main()
#deckPrinter(52)
