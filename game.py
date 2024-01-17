"""Game that guesses a number"""

import numpy as np

number = np.random.randint(1,101) # here we set the number to guess

# attempts
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number between 1 and 100: '))
    
    if predict_number > number:
        print ('The number should be smaller')
               
    elif predict_number < number:
        print ('The number should be larger')
        
    else:
        print (f'You are correct! It is {number}! You got is in {count} attempts')
        break # exit from the while cicle50