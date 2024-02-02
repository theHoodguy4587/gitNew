import random
def scN(x):
    high=x
    low=1
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else :
            guess=low    
    
        
        feedback=input(f'is number {guess} high, low or correct? ')
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print("yes I'm correct")  
    
scN(50)    