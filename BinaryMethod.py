#Binary Module
#This module handles all tasks relating to:
#text to binary
#binary to text

#This is broken down in a very step by step, module based process. NOTE: Not fast, but doesn't have to be


def binaryMethod(state):
    global asciiDictionary
    asciiDictionary=asciiDictionaryCreator()    
    print('Binary Method Encryption')
    print('This function will take either plaintext or binary numbers and convert them into the corresponding other.')
    badInput=True
    while badInput:
        choiceBinary=input("Are you entering text or numbers?:(Enter 'text' or 'numbers')\n")
        if choiceBinary=='text' or choiceBinary=='Text':
            badInput=False
            stringToNum=input('Please enter the text to be encrypted:\n')
            resultBinary=sentenceScrambler(stringToNum)
            print('This text translates into',resultBinary,'in Binary.')
        elif choiceBinary=='numbers' or choiceBinary=='Numbers':
            badInput=False
            stringbraw=str(input('Please give me a string of binary:\n'))
            stringb=stringbraw.replace(' ','')
            resultString=sentenceConstructor(stringb)
            print('This Binary translates into',resultString,'in text.')    
        else:
            print("Please enter either 'text' or 'numbers'.")
        
    
def asciiDictionaryCreator():
    #declare alphabet
    alphabet='abcdefghijklmnopqrstuvwxyz'
    #One time run, creates accurate ASCII dictionary of all letters [lower, upper, and ' '] to ascii.
    endUpper=False
    endLower=False
    #declare basic alphabet now
    #actual ASCII counts- I don't need to use these, I could start at 1 for this program, but for consitancy I keep it ASCII
    countLower=97
    countUpper=65
    #create dict
    asciiDictionary={}
    #Populate with upper, lower letters and space for 25 letters each
    for num in range(24):
        while endUpper==False:
            for letter in alphabet.upper():
                asciiDictionary[letter]=countUpper
                #increment count
                if countUpper<91:
                    countUpper+=1
                #check for hard end
                if letter=='Z':
                    endUpper=True
        while endLower==False:
            for letter in alphabet.lower():
                asciiDictionary[letter]=countLower
                #increment count
                if countLower<123:  
                    countLower+=1
                #check for hard end
                if letter=='z':
                    endLower=True
    #dont forget 'space', just hardcode, and oddballs rather then loop - numbers could be looped
    asciiDictionary[' ']=32
    asciiDictionary['!']=33
    asciiDictionary['"']=34
    asciiDictionary["'"]=39
    asciiDictionary['(']=40
    asciiDictionary[')']=41
    asciiDictionary[',']=44
    asciiDictionary['.']=46
    asciiDictionary[':']=58
    asciiDictionary[';']=59
    asciiDictionary['?']=63
    return(asciiDictionary)

def numberConstructor(string):
    #Takes a binary string, converts to digit
    #0=00000000, 255=11111111[addition of powers of 2][1+2+4+8+16+32+64+128]    
    total=0
    for digit in range(8):
        #get specific digit on code
        currentdigit=int(string[digit])
        #multiply by current power of 2
        value=(currentdigit*(2**(abs(digit-7))))
        total+=value
        #reverse for correct num
    return total
    
def binaryConstructor(number):
    #Takes a number, produces a full binary string
    #2**7,6,5,4,3,2,1,0
    subtracting=True
    binarystr=''
    while subtracting==True:
        nnumber=number
        for digit in range(8,0,-1):
            #get current value of binary digit to check
            binaryval=2**(digit-1)
            #print(binaryval)
            subBinVal=nnumber-binaryval
            if subBinVal>0: 
                #If can subtract, not past limit, correct 'digit'
                binarystr+='1'
                nnumber-=binaryval
            elif subBinVal<0:
                #if subtract too far, incorrect digit
                binarystr+='0'
            else:
                #If at 0, last digit applicable
                binarystr+='1'
                nnumber-=binaryval
                subtracting=False
        while len(binarystr)<8:
            #Fill to length with 0's
            binarystr+='0'
    return binarystr

def asciiLetterConstructor(lstring):
    letter=lstring
    #Can be suppressed to run chain with a sentence function
    #Letter -> number, then given as ascii
    #Get letter value from dictionary, return as ascii
    if letter in asciiDictionary:
        asciival=asciiDictionary.get(letter)
        return asciival
    else:
        return 33

def letterAsciiConstructor(number):
    #Number -> ASCII Letter, then to user
    #pops a dictionary into a list structure and pulls the indexed value out by referencing key
    if number in asciiDictionary.values():
        letter=list(asciiDictionary.keys())[list(asciiDictionary.values()).index(number)]
        return letter  
    else:
        return '!'
    
    
def asciiBinaryConstructor(lstring):
    letter=lstring
    #Takes a letter, turns it into binary
    #Number identified as ascii -> binary, then passed to user
    #give ascii letter to ascii constructor
    asciiletter=asciiLetterConstructor(letter)
    #gives ascii value to binary constructor
    binaryletter=binaryConstructor(asciiletter)
    return binaryletter
    
def binaryAsciiConstructor(string):
    #Takes a binary string, turns it into a number, turns into a letter
    #run the binary string into numberConstructor
    numbinary=numberConstructor(string)
    #run the number through letter constructor
    letterbinary=letterAsciiConstructor(numbinary)
    return letterbinary
  
def sentenceConstructor(binarynum):
    outstring=''
    binarystr=''
    count=0
    binarynum.strip('')
    #Takes numbers of binary, brings them back into letters, strings sentence together for user.
    for letter in range(len(binarynum)):
        #get bunches of 8, throw them into a list, run that list through binaryAsciiConstructor()
        if count<7:
            binarystr+=binarynum[letter]
            count+=1
        else:
            binarystr+=binarynum[letter]
            outletter=str(binaryAsciiConstructor(binarystr))
            binarystr=''
            outstring+=outletter
            count=0
    return outstring

 
def sentenceScrambler(string):
    #Takes, breaks string into letters, passes them into binary, returns string of converted text.
    outbinary=''
    #Takes string input, translates to binary.
    for letter in range(len(string)):
        binstring=asciiBinaryConstructor(string[letter])
        outbinary+=binstring+' '
    return outbinary.rstrip()