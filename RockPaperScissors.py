import random

def rndom():
    user=input("enter rock 'r', paper 'p' or scissor 's' ")
    computer=random.choice(['r','p','s'])
    if user==computer:
        return "tie"
    if game(user,computer):
        return "you won"
    return "you lose"    
def game(op1,op2):
    if (op1=='r' and op2=='s') or (op1=='p' and op2=='r') or (op1=='s' and op2=='p'):
        return True      
print(rndom())       
        
    