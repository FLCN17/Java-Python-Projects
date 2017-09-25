#cory Cothrum
#8/2/2017
#Complete for encrypt/decrypt

Alphabet='abcdefghijklmnopqrstuvwxyz'

def caesarCipher(state):
    print('Caesar Cipher Encryption')
    print('This function will take either plaintext\nor ciphertext and encipher/decipher them.\nThe Caesar Cipher relies on keeping the shift value\nsecret and shared between parties.\nIt is needed for both encryption\nand decryption.')
    badInput=True
    while badInput:
        choice=input("Are you entering plaintext or cipertext?:(Enter 'plain' or 'cipher')\n")
        if choice=='plain' or choice=='Plain':
            badInput=False
            print('Please enter the text to be encrypted, as well as the shift value:\n')
            plainText=input('Plaintext: ')
            try:
                shiftValue=int(input('Shift Value: '))
            except:
                shiftValue=int(input('Shift Value: [Must be a number!]'))
            resultCipher=caesarEncryption(plainText, shiftValue)
            print('This text translates into',resultCipher,' after applying a shift of', shiftValue)
        
        elif choice=='cipher' or choice=='Cipher':
            badInput=False
            print('Please enter the text to be decrypted, as well as the shift value:\n')
            cipherText=input('Ciphertext: ')
            try:
                shiftValue=int(input('Shift Value: '))
            except:
                shiftValue=int(input('Shift Value: [Must be a number!]'))
            resultPlain=caesarDecryption(cipherText, shiftValue)
            print('This message translates into',resultPlain) 
        else:
            print("Please enter either 'plain' or 'cipher'.")
    
def caesarEncryption(plainString,shift):
    ciphertext=''
    plainString=plainString.lower()
    for letter in range(len(plainString)):
        try:
            cipherletter=plainString[letter]
            letterPlain=Alphabet[(((Alphabet.index(cipherletter)))+shift)%26]          
            ciphertext+=letterPlain
        except:
            ciphertext+=plainString[letter] 
    return ciphertext
    
def caesarDecryption(cipherString,shift):
    plaintext=''
    for letter in range(len(cipherString)):
        try:
            cipherletter=cipherString[letter]
            letterPlain=Alphabet[(((Alphabet.index(cipherletter))+26)-shift)%26]          
            plaintext+=letterPlain
        except:
            plaintext+=cipherString[letter]       
    return plaintext