import random
def secret_num(x):
    randI=random.randint(1, x)
    guess=0
    while guess!=randI:
        guess=int(input(f'enter number between 1 and {x}: '))
        if guess<randI:
            print("nope that's too low")
        elif guess>randI:
            print("nope that's too high")
    
    print("yay! it's the number")
            
            
secret_num(10)       