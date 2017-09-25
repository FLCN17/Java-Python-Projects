#Vinegere Method

Alphabet='abcdefghijklmnopqrstuvwxyz'

def vinegereCipher(state):
    print('Vinegere Cipher Encryption')
    print('This function will take either plaintext\nor ciphertext and encipher/decipher them.\nThe Vinegere Cipher is the next evolution of the Caesar Cipher. It uses a key phrase shared between parties rather then a single value. The letters in the phrase then dictate the shift values.')
    badInput=True
    while badInput:
        choice=input("Are you entering plaintext or cipertext?:(Enter 'plain' or 'cipher')\n")
        if choice=='plain' or choice=='Plain':
            badInput=False
            print('Please enter the text to be encrypted, as well as the secret phrase:\n')
            plainText=input('Plaintext: ')
            secretPhrase=input('Secret Phrase: ')
            resultCipher=vinegereEncryption(plainText, secretPhrase)
            print('This text translates into',resultCipher,' after applying the phrase ', secretPhrase)
        elif choice=='cipher' or choice=='Cipher':
            badInput=False
            print('Please enter the text to be decrypted, as well as the secret phrase:\n')
            cipherText=input('Ciphertext: ')
            secretPhrase=input('Secret Phrase: ')
            resultPlain=vinegereDecryption(cipherText, secretPhrase)
            print('This message translates into',resultPlain) 
        else:
            print("Please enter either 'plain' or 'cipher'.")    
    
    
def vinegereEncryption(plainString,shiftPhrase):
    ciphertext=''
    phrasePOS=0
    plainString=plainString.lower()
    shiftPhrase=shiftPhrase.lower()
    for letter in range(len(plainString)):
        if phrasePOS >= (len(shiftPhrase)-1):
            phrasePOS=0
        else:
            shift=Alphabet.index(shiftPhrase[phrasePOS])
            phrasePOS+=1
        try:
            cipherletter=plainString[letter]
            letterPlain=Alphabet[(((Alphabet.index(cipherletter)))+shift)%26]          
            ciphertext+=letterPlain
        except:
            ciphertext+=plainString[letter]
            phrasePOS-=1
    return ciphertext
    
def vinegereDecryption(cipherString,shiftPhrase):
    plaintext=''
    phrasePOS=0
    shiftPhrase=shiftPhrase.lower()    
    for letter in range(len(cipherString)):
        if phrasePOS >= (len(shiftPhrase)-1):
            phrasePOS=0
        else:
            shift=Alphabet.index(shiftPhrase[phrasePOS])
            phrasePOS+=1        
        try:
            cipherletter=cipherString[letter]
            letterPlain=Alphabet[(((Alphabet.index(cipherletter))+26)-shift)%26]          
            plaintext+=letterPlain
        except:
            plaintext+=cipherString[letter]
            phrasePOS-=1
    return plaintext

