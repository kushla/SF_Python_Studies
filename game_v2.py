"""Game where computer guesses a number"""

import numpy as np

def random_predict (number:int=1) -> int:
    """Randomly guess a number

    Args:
        number (int, optional): Computer thinks of this number. Defaults to 1.

    Returns:
        int: number of guesses
    """
    
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101) # Guessed number
        if number == predict_number:
            break # Cycle break
    
    return (count)

def score_game(random_predict) -> int:
    """Average of 1000 experiments number of attempts computer uses to guess correctly

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: average number of guesses
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print (f'This algorithm guesses the number on average in {score} attempts')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)