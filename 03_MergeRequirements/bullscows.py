import random
import argparse
import urllib3
from cowsay import cowsay, read_dot_cow
from io import StringIO

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
    cow = read_dot_cow(StringIO("""
$the_cow = <<EOC;
         $thoughts
          $thoughts
        .
               ╱▏▕╲
             ╱▏▏▏▕▕
             ▏▏▏▏▕▕
          ▕╲ ▏▏╲╲╱ ▔╲
          ▕▕ ╲╲╱ ╱▔▔▔
           ╲▔▔ ╱▔
            ▔▔▉╭━┓
           ╱▔▔┊╯╭┃
        ╱▔▔┈╭▅┓┊┳╯
        ▏╯┈┈┗━╯┊╰
        ╲━╯┊┊┊┊┊┊
         ▔▔▔╲┊┊┊

EOC
"""))
    print(cowsay("Быки: "+str(bulls)+", Коровы: "+str(cows), cowfile=cow))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    random.seed()
    n = random.randint(0,len(words)-1)
    secret = words[n]
    trycount = 0
    surrender = False
    while True:
        guess = ask("Введите слово: ", words)
        if (guess == '-'):
            surrender = True
            break
        bullcowsarr = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bullcowsarr[0], bullcowsarr[1])
        trycount += 1
        if bullcowsarr[0] == len(secret):
            break
    if surrender:
        print(secret)
    else:
        ask(str(trycount))
    return trycount


def ask(prompt: str, valid: list[str] = None) -> str:
    cow = read_dot_cow(StringIO("""
$the_cow = <<EOC;
         $thoughts
          $thoughts
        .
               ╱▏▕╲
             ╱▏▏▏▕▕
             ▏▏▏▏▕▕
          ▕╲ ▏▏╲╲╱ ▔╲
          ▕▕ ╲╲╱ ╱▔▔▔
           ╲▔▔ ╱▔
            ▔▔▉╭━┓
           ╱▔▔┊╯╭┃
        ╱▔▔┈╭▅┓┊┳╯
        ▏╯┈┈┗━╯┊╰
        ╲━╯┊┊┊┊┊┊
         ▔▔▔╲┊┊┊

EOC
"""))

    if valid == None:
        print(cowsay(prompt, cowfile=cow))
        answer = None
    else:
        print(cowsay(prompt, cowfile=cow))
        while True:
            answer = input()
            if (answer == '-'):
                return('-')
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
parser.add_argument("--length", help="length of the word", type=int, default = 5)
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
