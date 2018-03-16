## flcn 3/6/18
# ALL WORK AND NO PLAY MAKES JACK A DULL BOY
#This program is designed to closely recreate the paperwork
#from Jack in The Shining.
# - basic lined output
## 3/10/18
# Program can now output both lines, with spacing,
# and paragraphs with embedded indented sections.
# HOWEVER
# its stupid and only modifies a given phrase. It needs
# to actual print the phrase in real time. Also some functions need to be method'ed out to be
# easier to work with. Namely the character replace or duplicate. Needs
# to be less code but also properly double up letters -
# currently only doubles up if randomly selects same as next.
# ALSO
# needs to have a function to throw in a triangular structure - 
# drop first word, indent plus a space
#
# i.e: All work and no play makes jack a dull boy
#       work and no play makes jack a dull boy
#        and no play makes jack a dull boy
#         no play makes jack a dull boy
#          play makes jack a dull boy
#           makes jack a dull boy
#            jack a dull boy
#             a dull boy
#              dull boy
#               boy
#
# ALSO
# Function to handle spaces and newlines randomly added/not added.
# sometimes patterns, sometimes just random; ie can form paragraphs or consistent mistakes
# random newline indents


import random as rn

def jack():
    atOverlook = True    
    story = "All work and no play makes jack a dull boy"
    spacing = 1 # Spacing determines the number of lines to be skipped after an output
    mode = 0 # Mode determines the output mode; 0 is lined, 1 is paragraphs
    #message = input("Whats your story?\n")
    while(atOverlook):
        typeWriter(story, mode, spacing)

def typeWriter(message, lines, spacing):
    if lines:
        message = "     " + message + "     " # replace with a spacing padder; decides indent and fills to next line?
        print(allWorkNoPlayLines(message))
        for i in range(spacing):
            print("")        
    else:
        print(allWorkNoPlayParagraphs(message))
        for i in range(spacing):
            print("")
    
def allWorkNoPlayLines(message):
    #generates lines of typo'd text from an alphabet pool
    capitalError = 10
    firstTypo = 5
    secondTypo = 10
    thirdTypo = 15
    skippedLine = 50
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz     .,:';?/=+1234567890" + '"'
    #message = (' '*rn.randint(0, 3))*rn.randint(0, 4) + message
    if (not rn.randint(0, firstTypo)):
        if (not rn.randint(0, skippedLine)):
            message = ""
        else:
            index = rn.randint(0, len(message))
            if rn.randint(0, 2) == 1:
                message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index+1:]
            else:
                message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index:]
        if (not rn.randint(0, secondTypo)):
            if (not rn.randint(0, skippedLine)):
                message = ""
            else:                
                index = rn.randint(0, len(message))
                if rn.randint(0, 1):
                    message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index+1:]
                else:
                    message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index:] 
            if (not rn.randint(0, thirdTypo)):
                if (not rn.randint(0, skippedLine)):
                    message = ""
                else:                    
                    index = rn.randint(0, len(message))
                    if rn.randint(0, 1):
                        message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index+1:]
                    else:
                        message = message[:index] + alphabet[rn.randint(0, len(alphabet)-1)] + message[index:]
        
    return message

def allWorkNoPlayParagraphs(message):
    paragraph = ' '*rn.randint(0, 8)
    if rn.randint(0, 10):
        message += '.'
    if rn.randint(0, 3):
        message += ' '
    lines = rn.randint(0, 15) 
    if rn.randint(0, 20):
        for i in range(lines):
            if not rn.randint(0, 3):
                paragraph += allWorkNoPlayLines(message.upper())
            else:
                paragraph += allWorkNoPlayLines(message)
    else:
        for i in range(lines):
            if not rn.randint(0, 3):
                paragraph += "\t\t" + allWorkNoPlayLines(message.upper()) + "\n"
            else:
                paragraph += "\t\t" + allWorkNoPlayLines(message) + "\n"
    return paragraph

jack()
