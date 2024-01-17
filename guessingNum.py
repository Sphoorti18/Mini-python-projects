import random

def guess():
    chosenWord=random.randint(1,100)
    return chosenWord

    
    
if __name__ == "__main__":
    print("I\'m thinking of a number b/t 1-100 and you\'ve to guess it right\n")
    correctNum=guess()
    while True:
        n=int(input("Take a guess and press \'0\' to exit\n "))
        if (n==correctNum):
            print("Yay! You guessed my number!")
        if (n==0):
            break
        
        
        
    
