import random

def winner(c, y):

    if c == y:
        return None

    elif c == 'r':
        if y=='p':
            return False
        elif y=='s':
            return True
    
    elif c == 'p':
        if y=='r':
            return False
        elif y=='s':
            return True
    
    elif c == 's':
        if y=='p':
            return False
        elif y=='r':
            return True

print('''\n* * *  ROCK   * * *\n* * *  PAPER  * * *\n* * * SCISSOR * * *\n''')

input('***Press Enter to Play***')

print('''\n\n* * * Computer's turn* * * \n\n * * * Thinking * * * \n\n * * * Computer Picked * * *\n\n ''')

input('***Press Enter to Continue***')

randNo = random.randint(1, 3) 
if randNo == 1:
    c = 'r'
elif randNo == 2:
    c = 'p'
elif randNo == 3:
    c = 's'

print('''\n\n***Your's Turn***\n***Pick Between***\n\n***Rock(r)***\n***Paper(p)***\n***Scissor(s)***\n\n''')

y=input('[r/p/s] :  ')

w=winner(c,y)

if c=='r':
    c='ROCK'
elif c=='p':
    c='PAPER'
elif c=='s':
    c='SCISSOR'

if y=='r':
    y='ROCK'
elif y=='p':
    y='PAPER'
elif y=='s':
    y='SCISSOR'

print(f"\nComputer Picked *** {c} ***\n")
print(f"You Picked *** {y} ***\n")
print('''\n\n***RESULT***\n''')

if w == None:
    print("*** tie!!! ***\n")
elif w:
    print("*** You Win!!! \n***")
else:
    print("*** You Lose!!! ***\n")

print('***Thank You For Playing***\n---Desined by AMLAN BISWAS\n')