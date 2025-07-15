from Q1 import TrialDivisionTest
from Q2 import FermatTest
from Q4 import EulerTest
from Q5 import StrongTest
import numpy as np
import time
import matplotlib.pyplot as plt

def QuickPrimalityTest(N):
    ### Make sure N is odd
    if (N % 2 == 0):
        return False
    ### Is it better to use Trial Division?
    if (N < 100000):
        return TrialDivisionTest(N)
    
    if (not StrongTest(N, 2)): return False
    if (not StrongTest(N, 3)): return False
    
    # Does it need more tests
    if (N < 1373652): return True
    if (not StrongTest(N, 5)): return False

    # Does it need more tests
    if (N < 25326000): return True
    if (not StrongTest(N, 7)): return False

    # Does it need more tests
    if (N < 3215031750): return True
    if (not StrongTest(N, 11)): return False

    # Must be true now
    return True


def SpeedChecking():
    t = 100000
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    K = [i for i in range(1, 7)]
    fermatTimes = []
    eulerTimes = []
    strongTimes = []
    trialTimes = []
    for k in range(1, 7):
        
        print("$" + str(k) + "$, ", end= "")
        numbers = [ int(np.random.randint(10**k, 10**(k+1))) for i in range(t)]
        for i in range(t):
            if (numbers[i] % 2 == 0):
                numbers[i] = numbers[i] + 1

        start = time.time()

        for i in range(t):
            passesTest = FermatTest(numbers[i], primes[i % 24])

        fermatTimes.append(time.time() - start)
        start = time.time()

        for i in range(t):
            passesTest = EulerTest(numbers[i], primes[i % 24])

        eulerTimes.append(time.time() - start)
        start = time.time()

        for i in range(t):
            passesTest = StrongTest(numbers[i], primes[i % 24])

        strongTimes.append(time.time() - start)
        start = time.time()

        for i in range(t):
            prime = TrialDivisionTest(numbers[i])
        
        trialTimes.append(time.time() - start)


    ### Graph it

    X_axis = np.arange(len(K)) 
  
    plt.bar(X_axis - 0.3, fermatTimes, 0.2, label = 'Fermat')
    plt.bar(X_axis - 0.1, eulerTimes, 0.2, label = 'Euler') 
    plt.bar(X_axis + 0.1, strongTimes, 0.2, label = 'Strong')
    plt.bar(X_axis + 0.3, trialTimes, 0.2, label = 'Trial Division')

    #plt.rcParams['text.usetex'] = True
    
    plt.xticks(X_axis, K) 
    plt.xlabel("k") 
    plt.ylabel("Time taken (s)") 
    plt.title("") 
    plt.legend() 
    plt.show() 
    



def QuickTrialComparison ():
    t = 100000

    K = [i for i in range(1, 9)]
    trialTimes = []
    quickTimes = []
    for k in range(1, 9):
        
        print("$" + str(k) + "$, ", end= "")
        numbers = [ int(np.random.randint(10**k, 10**(k+1))) for i in range(t)]

        start = time.time()

        for i in range(t):
            QuickPrimalityTest(numbers[i])

        quickTimes.append(time.time()- start)
        start = time.time()

        for i in range(t):
            TrialDivisionTest(numbers[i])

        trialTimes.append(time.time()- start)

    ### Graph it

    X_axis = np.arange(len(K)) 
  
    plt.bar(X_axis - 0.2, quickTimes, 0.4, label = 'Quick Test')
    plt.bar(X_axis + 0.2, trialTimes, 0.4, label = 'Trial Division')

    #plt.rcParams['text.usetex'] = True
    
    plt.xticks(X_axis, K) 
    plt.xlabel("k") 
    plt.ylabel("Time taken (s)") 
    plt.title("") 
    plt.legend() 
    plt.show() 

if __name__ == "__main__":
    SpeedChecking()
    print()
    QuickTrialComparison()
    
