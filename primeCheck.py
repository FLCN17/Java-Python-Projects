#Prime checker
#Roughly checks if a given number is Prime.
import math
import random as rn
import time

def main():
    continueCheck=True
    #rangeChecker()
    #primeHunterGroup()
    #primeHunterTimer()
    #primeHunterSimpler()
    while continueCheck:
        #primeHunterSimpler()
        primeHunterTimer()
        continueCheck=input('Continue?\n')
        if continueCheck=='y' or continueCheck=='Y' or continueCheck=='':
            continueCheck=True
    
def isPrime(n):
    #Same as all before, but runs a seive as well.
    if n==1:
        return False
        
    elif n==2:
        return True
        
    elif n>2 and n%2==0:
        return False
    
    elif n>3 and n%3==0:
        return False
    
    elif n>5 and n%5==0:
        return False
    
    '''elif n>7 and n%7==0:
        return False'''
    
        
    max_divisor=math.floor(math.sqrt(n))
    for d in range(3,1+max_divisor,2):
        if n % d==0:
            return False
            
    return True


#Timing
def rangeChecker():
    Pranges=int(input('How many stretches of 10000 would you like to check for Primes?: '))
    listPrimes=[]
    totalPrimeCount=0
    primeCount=0
    lastPrimeCount=0
    totalTime=0
    #Checks for primes within a range of 10000 numbers at a time, and times itself between all of them.
    for loops in range(Pranges+1):
        t0=time.time()
        lowerRange=(loops-1)*10000
        if lowerRange<=0:
            lowerRange=1
        upperRange=loops*10000
        for n in range(lowerRange,upperRange):
            if isPrime(n):
                listPrimes+=[n]
                primeCount+=1
        t1=time.time()
        totalTime+=(t1-t0)
        #print('Time elapsed: ',t1-t0)
        #print('Primes between',lowerRange,'and',upperRange,':',primeCount)
        '''if (primeCount!=0) and (lastPrimeCount!=0):
            print('Ratio between last two ranges:',(lastPrimeCount/primeCount))
            print('or:',(primeCount/lastPrimeCount))'''
        totalPrimeCount+=primeCount
        #lastPrimeCount=primeCount
        primeCount=0
    print('Total primes below ',Pranges*10000,': ',totalPrimeCount,'.',sep='')
    print('Total time elsapsed:',totalTime,'.',sep='')
    print('The last Prime happens to be ',listPrimes[(len(listPrimes)-1)],'.',sep='')

#Make a function that takes a random x-digit number, and finds 100 primes after it.
def primeHunterGroup():
    lapTime=0
    totalTime=0
    listFoundPrimes=[]
    digits=int(input('Please enter a number of digits you would like these Primes to be: '))
    startingNumber=rn.randrange((10**(digits-1)),(10**digits))
    print('Starting with: ',startingNumber,'.',sep='')
    if isPrime(startingNumber):
        listFoundPrimes+=[startingNumber]
        print('And it is Prime.')
    while len(listFoundPrimes)<100:
        t0=time.time()
        if startingNumber%2==0:
            startingNumber+=1
        else:
            startingNumber+=(2*rn.randint(0,5))
        if isPrime(startingNumber):
            listFoundPrimes+=[startingNumber]
            t1=time.time()
            lapTime=(t1-t0)   
            print('Ding',len(listFoundPrimes),'|',lapTime)
            totalTime+=lapTime
            lapTime=0
    print('\n',len(listFoundPrimes),'Primes were found.')
    print(listFoundPrimes)
    print('Time elapsed:',totalTime)

def primeHunterSimpler():
    foundPrime=0
    digits=int(input('Please enter a number of digits you would like the Prime to be: '))
    if digits>0:
        startingNumber=rn.randrange((10**(digits-1)),(10**digits))
    else:
        startingNumber=1
    t0=time.time()
    if isPrime(startingNumber):
        foundPrime=startingNumber
        print('And it is Prime.')
        print(t1-t0)
    else:
        while foundPrime==0:
            if startingNumber%2==0:
                startingNumber+=1
            else:
                startingNumber+=(2*rn.randint(0,5))
            if isPrime(startingNumber):
                foundPrime=startingNumber
                t1=time.time()
                print(t1-t0)
                print('Ding')
    print(foundPrime)

def primeHunterTimer():
    #using a set digit range, run through it a certain amount of times and get the average time [totaltime/total primes], find gaps between them
    foundPrimes=[]
    primeGap=0
    totaltime=0
    lastnumber=0
    loops=int(input('How many primes would you like to average: '))
    digits=int(input('Please enter a number of digits you would like the Prime to be: '))
    if digits>0:
        startingNumber=rn.randrange((10**(digits-1)),(10**digits))
        #print(startingNumber)
    else:
        startingNumber=1   
    while len(foundPrimes)<(loops):
        lastnumber=startingNumber
        for item in range(loops):
            #print('loops')
            t0=time.time()
            if isPrime(startingNumber):
                #print(len(foundPrimes))
                if len(foundPrimes)<loops:
                    foundPrimes+=[startingNumber]
                    primeGap+=startingNumber-lastnumber
                t1=time.time()
                totaltime+=(t1-t0)
                startingNumber+=(2*rn.randint(0,5))
            else:
                if startingNumber%2==0:
                    startingNumber+=1
                else:
                    #startingNumber+=2
                    startingNumber+=(2*rn.randint(0,5))
    print('Time elapsed: ',totaltime,'. Average time: ',(totaltime/len(foundPrimes)),'.',sep='')
    print('Average number gap between primes: ',primeGap/len(foundPrimes),'.',sep='')
    print('Primes:', foundPrimes)

main()