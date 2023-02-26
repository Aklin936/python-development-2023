import random
import argparse
import urllib3

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


def inform(format_string: str, bulls: int, cows: int) -> None:
    print("Быки: ", bulls,"Коровы: ", cows)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    random.seed()
    n = random.randint(0,len(words)-1)
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
    return trycount


def ask(prompt: str, valid: list[str] = None) -> str:
    if valid == None:
        print(prompt)
        answer = None
    else:
        print(prompt)
        while True:
            answer = input()
            f = False 
            for i in valid:
                if answer == i:
                    f = True
                    break
            if f:
                break
    return(answer)


parser = argparse.ArgumentParser()
parser.add_argument("dict", help="path to the dictionary", type=str)
parser.add_argument("length", help="length of the word", type=int)
args = parser.parse_args()
if (args.dict[:4] == 'http'):
    http = urllib3.PoolManager()
    r = http.request('GET', args.dict)
    dictionary = r.data.splitlines()
    for i in range(len(dictionary)):
        dictionary[i] = dictionary[i].decode('UTF-8')
else:
    f = open(args.dict, 'r')
    dictionary = f.read().splitlines()
    f.close()

temp = []
for i in dictionary:
    if len(i) == args.length:
        temp.append(i)

dictionary = temp
print(gameplay(ask, inform, dictionary))
