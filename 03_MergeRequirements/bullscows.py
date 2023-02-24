

def bullscows(guess: str, secret: str) -> (int, int):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls +=1
        for i2 in range(len(secret)):
            if guess[i] == secret[i2]:
                cows += 1
                break
    return [bulls, cows]
