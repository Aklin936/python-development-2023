import random

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


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    random.seed()
    n = random.randint(0,len(words))
    secret = words[n]
    trycount = 0
    while True:
        guess = ask("Введите слово: ", words)
        bullcowsarr = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bullcowsarr[0], bullcowsarr[1])
        trycount += 1
        if bullcowsarr[0] == len(secret):
            break
    ask(str(trycount))
